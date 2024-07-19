from abc import ABC, abstractmethod

class DuplicateTagNameException(BaseException):
    def __str__(self) -> str:
        return "Error: Tag already exists"

class DuplicateAdsNameException(BaseException):
    def __str__(self) -> str:
        return "Error: Ad already exists"

class DuplicatePlaceNameException(BaseException):
    def __str__(self) -> str:
        return "Error: Place already exists"

class TagNotFoundException(BaseException):
    def __str__(self) -> str:
        return "Error: Tag not found"

class PlaceDoesNotExist(BaseException):
    def __str__(self) -> str:
        return "Error: Place not found"

class AdsDoesNotExist(BaseException):
    def __str__(self) -> str:
        return "Error: Ads not found"

class AddsPlaceCommon(ABC):
    objects = []
    last_id = 0

    def __init__(self, name, cpc, tags) -> None:
        self.name = name
        self.cpc = cpc
        self.tags = tags
        self.id = None

    @classmethod
    def _get_id(cls):
        cls.last_id += 1
        return cls.last_id

    def save(self):
        if self._is_not_duplicate(self.name):
            if Tag.exist(self.tags):
                self.id = self._get_id()
                self.__class__.append_to_objects(self)
            else:
                raise TagNotFoundException
        else:
            raise self.get_duplicate_exception()

    @classmethod
    def append_to_objects(cls, obj):
        cls.objects.append(obj)

    @classmethod
    def _is_not_duplicate(cls, name):
        return name not in [x.name for x in cls.objects]

    def success_message(self):
        return f"Done: {self.__class__.__name__.title()} {self.id} is {self.name}."

    @classmethod
    def list(cls):
        return f"{cls.__name__.upper()}s: {' '.join([x.name for x in sorted(cls.objects, key=lambda x: x.id)])}"

    @classmethod
    def exist(cls, names):
        existed_names = [x.name for x in cls.objects]
        for name in names:
            if name not in existed_names:
                return False
        return True

    @abstractmethod
    def get_duplicate_exception(self):
        pass

    def suggest(self):
        ids = map(lambda z: str(z[0]),
                  sorted([(x.id, self.proper(x.cpc, self.cpc, x.tags, self.tags))
                         for x in self.suggest_objects.objects], key=lambda y: y[1],
                         reverse=True))
        return f"SUGGEST-{self.suggest_objects.__name__.upper()}: {' '.join(list(ids))}"

    @staticmethod
    def proper(cpci, cpcj, tagsi, tagsj):
        tagsi = set(tagsi)
        tagsj = set(tagsj)
        common = len(tagsj.intersection(tagsi))
        diff = len(tagsi - tagsj)
        return 1 / max(1, abs(cpci - cpcj)) * (common - diff)

class Place(AddsPlaceCommon):
    suggest_objects = None
    duplicate_exception = DuplicatePlaceNameException
    does_not_exist_exception = PlaceDoesNotExist

    def get_duplicate_exception(self):
        return self.duplicate_exception

class Ad(AddsPlaceCommon):
    suggest_objects = Place
    duplicate_exception = DuplicateAdsNameException
    does_not_exist_exception = AdsDoesNotExist

    def get_duplicate_exception(self):
        return self.duplicate_exception

class Tag:
    duplicate_exception = DuplicateTagNameException
    objects = []

    @classmethod
    def add_tag(cls, name):
        if cls._is_not_duplicate(name):
            tag = Tag(name)
            tag.id = AddsPlaceCommon._get_id()
            cls.objects.append(tag)
            print(tag.success_message())
        else:
            raise cls.duplicate_exception

    def save(self):
        if self._is_not_duplicate(self.name):
            self.id = AddsPlaceCommon._get_id()
            self.__class__.objects.append(self)
        else:
            raise self.duplicate_exception

    @classmethod
    def _is_not_duplicate(cls, name):
        return name not in [x.name for x in cls.objects]

    def success_message(self):
        return f"Done: Tag {self.id} is {self.name}."

    @classmethod
    def list(cls):
        return f"TAGS: {' '.join([x.name for x in sorted(cls.objects, key=lambda x: x.id)])}"

    @classmethod
    def exist(cls, names):
        existed_names = [x.name for x in cls.objects]
        for name in names:
            if name not in existed_names:
                return False
        return True


class Ad(AddsPlaceCommon):
    def __init__(self, tag_manager):
        super().__init__(name=None, cpc=None, tags=None)
        self.tag_manager = tag_manager

    def add_ad(self, name, cpc, tag_names):
        ad = Ad(name, cpc, tag_names)
        try:
            ad.save()
            print(ad.success_message())
        except DuplicateAdsNameException as e:
            print(e)
        except TagNotFoundException as e:
            print(e)

    def list_all_ads(self):
        print(Ad.list())

class Place(AddsPlaceCommon):
    def __init__(self, tag_manager, ad_manager):
        super().__init__(name=None, cpc=None, tags=None)
        self.tag_manager = tag_manager
        self.ad_manager = ad_manager

    def add_place(self, name, cpc, tag_names):
        place = Place(name, cpc, tag_names)
        try:
            place.save()
            print(place.success_message())
        except DuplicatePlaceNameException as e:
            print(e)
        except TagNotFoundException as e:
            print(e)

    def list_all_places(self):
        print(Place.list())

    def suggest_ads(self, place_id):
        try:
            place = Place.get(place_id)
            print(place.suggest())
        except PlaceDoesNotExist as e:
            print(e)

    def suggest_places(self, ad_id):
        try:
            ad = Ad.get(ad_id)
            print(ad.suggest())
        except AdsDoesNotExist as e:
            print(e)

    def match_ad_place(self, ad_id, place_id):
        try:
            ad = Ad.get(ad_id)
            place = Place.get(place_id)
            Ad.objects.remove(ad)
            Place.objects.remove(place)
            print(f"Done: {ad.id} matched to {place.id}")
        except AdsDoesNotExist as e:
            print(e)
        except PlaceDoesNotExist as e:
            print(e)

def main():
    # Create the necessary objects
    tag_manager = Tag()
    ad_manager = Ad(tag_manager)
    place_manager = Place(tag_manager, ad_manager)

    # Read the number of requests
    n = int(input())

    # Process the requests
    for _ in range(n):
        request = input().split()
        if request[0] == "ADD-TAG":
            tag_manager.add_tag(request[2])
        elif request[0] == "TAG-LIST":
            tag_manager.list_all_tags()
        elif request[0] == "ADD-ADS":
            ad_manager.add_ad(request[2], int(request[4]), request[6:])
        elif request[0] == "ADS-LIST":
            ad_manager.list_all_ads()
        elif request[0] == "ADD-PLACE":
            place_manager.add_place(request[2], int(request[4]), request[6:])
        elif request[0] == "PLACE-LIST":
            place_manager.list_all_places()
        elif request[0] == "SUGGEST-ADS":
            place_manager.suggest_ads(int(request[2]))
        elif request[0] == "SUGGEST-PLACE":
            place_manager.suggest_places(int(request[2]))
        elif request[0] == "MATCH":
            place_manager.match_ad_place(int(request[2]), int(request[4]))
        else:
            print("Error: Invalid request")

if __name__ == "__main__":
    main()