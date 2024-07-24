"""
Job Offer System
"""
from enum import Enum
from math import floor

class JobAndUserError(Exception):
    """Base class for exceptions in this module."""

class FullNameError(JobAndUserError):
    """Exception raised for invalid names."""
    def __init__(self, message="Invalid name"):
        self.message = message
        super().__init__(self.message)

class AgeIntervalError(JobAndUserError):
    """Exception raised for invalid age."""
    def __init__(self, message="Invalid age interval"):
        self.message = message
        super().__init__(self.message)

class AgeError(JobAndUserError):
    """Exception raised for invalid age."""
    def __init__(self, message="Invalid age"):
        self.message = message
        super().__init__(self.message)

class TimeConditionError(JobAndUserError):
    """Exception raised for invalid time conditions."""
    def __init__(self, message="invalid timetype"):
        self.message = message
        super().__init__(self.message)

class SalaryError(JobAndUserError):
    """Exception raised for invalid salary."""
    def __init__(self, message="Invalid salary"):
        self.message = message
        super().__init__(self.message)

class TimeCondition(Enum):
    """Time Condition Enum"""
    FULLTIME = 'FULLTIME'
    PARTTIME = 'PARTTIME'
    PROJECT = 'PROJECT'

class Job:
    """Job Class"""
    _id_counter = 1
    jobs = []

    def __init__(self, name, min_age, max_age, time_condition, salary) -> None:
        self.id = None
        self._skills = []
        self._name = self.name = name
        self.__temp_age = int(max_age)
        self._min_age = self.min_age = min_age
        self._max_age = self.max_age = max_age
        self._time_condition = self.time_condition = time_condition
        self._salary = self.salary = salary
        self.views = 0
        self.skill_views = {}

    def __str__(self) -> str:
        return (
                f'User {self.id}: Name: {self.name},'
                f'Min Age: {self.min_age}, Max Age: {self.max_age},'
                f'Views: {self.views}'
                f'Time Condition: {self.time_condition}, Salary: {self.salary}'
                )

    def validate(self):
        """Validate job attributes."""
        self.id = Job._id_counter
        Job._id_counter += 1

        if not self._check_name(self.name):
            raise FullNameError()
        if not self._check_age(self.min_age, self.max_age):
            raise AgeError()
        if not self._check_time_condition(self.time_condition):
            raise TimeConditionError()
        if not self._check_salary(self.salary):
            raise SalaryError()

    def increment_view(self, skill):
        """Increment view count for the job and associated skill."""
        self.views += 1
        # print(self.name,self.views)
        if skill in self.skill_views:
            self.skill_views[skill] += 1
        else:
            self.skill_views[skill] = 1

    # Properties

    @property
    def skills(self):
        """Skills property."""
        return self._skills

    @property
    def name(self):
        """Name property."""
        return self._name

    @property
    def min_age(self):
        """Minimum age property."""
        return self._min_age

    @property
    def max_age(self):
        """Maximum age property."""
        return self._max_age

    @property
    def time_condition(self):
        """Time condition property."""
        return self._time_condition

    @property
    def salary(self):
        """Salary property."""
        return self._salary

    # Setters

    @skills.setter
    def skills(self, *skills):
        """Set skills property."""
        self._skills.extend(skills)

    @name.setter
    def name(self, name):
        """Set name property."""
        if self._check_name(name):
            self._name = name
        else:
            raise FullNameError()

    @min_age.setter
    def min_age(self, min_age):
        """Set minimum age property."""
        if self._check_age(min_age, self.__temp_age):
            self._min_age = min_age
        else:
            raise AgeIntervalError()

    @max_age.setter
    def max_age(self, max_age):
        """Set maximum age property."""
        if self._check_age(self.min_age, max_age):
            self._max_age = max_age
        else:
            raise AgeIntervalError()

    @time_condition.setter
    def time_condition(self, condition):
        """Set time condition property."""
        if self._check_time_condition(condition):
            self._time_condition = condition
        else:
            raise TimeConditionError()

    @salary.setter
    def salary(self, salary):
        """Set salary property."""
        if self._check_salary(salary):
            self._salary = salary
        else:
            raise SalaryError()

    def _check_name(self, name):
        """Check whether the name is valid."""
        if not 1 <= len(name) <= 10:
            return False
        if not name.isalpha():
            return False
        return True

    def _check_age(self, min_age, max_age):
        """Check whether ages are valid."""
        if (min_age < 0 or min_age > 200) or (max_age < 0 or max_age > 200):
            return False
        if min_age > max_age:
            return False
        return True

    def _check_time_condition(self, time_condition):
        """Check whether the time condition is valid."""
        if time_condition in TimeCondition:
            return True
        return False

    def _check_salary(self, salary):
        """Check whether the salary is valid."""
        if salary < 0 or salary >= 1_000_000_000 or salary % 1000 != 0:
            return False
        return True

class User:
    """User Class"""
    _id_counter = 1
    users = []

    def __init__(self, name, age, time_condition, salary) -> None:
        self.id = None
        self._skills = []
        self._name = self.name = name
        self._age = self.age = age
        self._time_condition = self.time_condition = time_condition
        self._salary = self.salary = salary
        self.total_views = 0
        self.skill_views = {}

    def __str__(self) -> str:
        return (
                f'User {self.id}: Name: {self.name},'
                f'Age: {self.age}, Time Condition: {self.time_condition},'
                f'Salary: {self.salary}'
                )

    def validate(self):
        """Validate user attributes."""
        self.id = User._id_counter
        User._id_counter += 1

        if not self._check_name(self.name):
            raise FullNameError()
        if not self._check_age(self.age):
            raise AgeError()
        if not self._check_time_condition(self.time_condition):
            raise TimeConditionError()
        if not self._check_salary(self.salary):
            raise SalaryError()

    # def view_job(self, job_id, joblist):
    #     """User views a job, incrementing its view count even if the user has no skills."""
    #     if job_id not in joblist:
    #         print("invalid index")
    #         return

    #     job = joblist[job_id]

    #     if not self._skills:
    #         job.increment_view(None)
    #     # self.total_views += 1

    #     if self._skills:
    #         print(self._skills)
    #         for skill in self._skills:
    #             # print(skill)
    #             job.increment_view(skill)
    #             if skill in self.skill_views:
    #                 self.skill_views[skill] += 1
    #             else:
    #                 self.skill_views[skill] = 1

        # print("tracked")

    def view_job(self, job_id, joblist):
        """User views a job, incrementing its view count even if the user has no skills."""
        if job_id not in joblist:
            print("invalid index")
            return

        job = joblist[job_id]

        # if not self._skills:
        #     job.increment_view(None)
        #     # self.total_views += 1

        # Track skill views
        skill_viewed = False  # Flag to track if a skill match occurred
        for skill in self._skills:
            if skill in job._skills:  # Check if the job has the user's skill
                job.increment_view(skill)  # Increment view count for the job with the skill
                skill_viewed = True  # Mark that a skill view occurred
                if skill in self.skill_views:
                    self.skill_views[skill] += 1
                else:
                    self.skill_views[skill] = 1

        # If no skill views occurred, ensure the skill view count remains zero
        if not skill_viewed:
            job.increment_view(None)
            for skill in self._skills:
                if skill not in self.skill_views:
                    self.skill_views[skill] = 0  # Explicitly set to zero if no views occurred

        print("tracked")

    def score_system(self, user, job):
        """The score system to determine the score of a user based on his attributes"""
        score = 0
        def age_score():
            user_age = user.age
            min_age = job.min_age
            max_age = job.max_age
            if (
                (user_age > min_age or user_age == min_age) and
                (user_age < max_age or user_age == max_age)
                ):
                agescore = min(max_age-user_age, user_age-min_age)
            elif user_age < min_age:
                agescore = user_age - min_age
            elif user_age > max_age:
                agescore = max_age - user_age
            return agescore
        def skill_score():
            user_skill = user.skills
            job_skill = job.skills
            skillscore = 0
            for skill in job_skill:
                if skill in user_skill:
                    skillscore += 3
                else:
                    skillscore -= 1
            return skillscore
        def time_score():
            user_time = user.time_condition
            job_time = job.time_condition
            timescore = 0
            if job_time == 'FULLTIME':
                if user_time == 'FULLTIME':
                    timescore = 10
                elif user_time == 'PARTTIME':
                    timescore = 5
                elif user_time == 'PROJECT':
                    timescore = 4
            if job_time == 'PARTTIME':
                if user_time == 'FULLTIME':
                    timescore = 5
                elif user_time == 'PARTTIME':
                    timescore = 10
                elif user_time == 'PROJECT':
                    timescore = 5
            if job_time == 'PROJECT':
                if user_time == 'FULLTIME':
                    timescore = 4
                elif user_time == 'PARTTIME':
                    timescore = 5
                elif user_time == 'PROJECT':
                    timescore = 10
            return timescore
        def salary_score():
            user_salary = user.salary
            job_salary = job.salary
            salaryscore = 0
            salaryscore = floor( 1000 / max( abs( user_salary - job_salary ), 1))
            return salaryscore
        score += age_score()
        score += skill_score()
        score += time_score()
        score += salary_score()
        score *= 1000
        score += job.id
        return score

    # Properties

    @property
    def skills(self):
        """Skills property."""
        return self._skills

    @property
    def name(self):
        """Name property."""
        return self._name

    @property
    def age(self):
        """Age property."""
        return self._age

    @property
    def time_condition(self):
        """Time condition property."""
        return self._time_condition

    @property
    def salary(self):
        """Salary property."""
        return self._salary

    # Setters

    @skills.setter
    def skills(self, *skills):
        """Set skills property."""
        self._skills.extend(skills)

    @name.setter
    def name(self, name):
        """Set name property."""
        if self._check_name(name):
            self._name = name
        else:
            raise FullNameError()

    @age.setter
    def age(self, age):
        """Set age property."""
        if self._check_age(age):
            self._age = age
        else:
            raise AgeError()

    @time_condition.setter
    def time_condition(self, condition):
        """Set time condition property."""
        if self._check_time_condition(condition):
            self._time_condition = condition
        else:
            raise TimeConditionError()

    @salary.setter
    def salary(self, salary):
        """Set salary property."""
        if self._check_salary(salary):
            self._salary = salary
        else:
            raise SalaryError()

    def _check_name(self, name):
        """Check whether the name is valid."""
        if not 1 <= len(name) <= 10:
            return False
        if not name.isalpha():
            return False
        return True

    def _check_age(self, age):
        """Check whether the age is valid."""
        if age < 0 or age > 200:
            return False
        return True

    def _check_time_condition(self, time_condition):
        """Check whether the time condition is valid."""
        if time_condition in TimeCondition:
            return True
        return False

    def _check_salary(self, salary):
        """Check whether the salary is valid."""
        if salary < 0 or salary >= 1_000_000_000 or salary % 1000 != 0:
            return False
        return True

def job_status(job_id, jobs):
    """Display the status of a job."""
    if job_id not in jobs:
        print("invalid index")
        return

    job = jobs[job_id]
    total_views = job.views
    skill_views = job.skill_views

    all_skills = job._skills
    skill_views_output = []

    for skill in all_skills:
        count = skill_views.get(skill, 0)
        skill_views_output.append(f"{skill},{count}")

    skills_output = ", ".join(skill_views_output)

    if all_skills:
        print(f"{job.name}-{total_views}-({skills_output})")
    else:
        print(f"{job.name}-{total_views}-")

def user_status(user_id, users):
    """Display the status of a user."""
    if user_id not in users:
        print("invalid index")
        return

    user = users[user_id]
    total_views = user.total_views
    skill_views = user.skill_views

    all_skills = user._skills
    skill_views_output = []

    for skill in all_skills:
        count = skill_views.get(skill, 0)
        skill_views_output.append(f"{skill},{count}")

    skills_output = ", ".join(skill_views_output)

    if all_skills:
        print(f"{user.name}-({skills_output})")
    else:
        print(f"{user.name}-")

def add_job_skill(job_id, skill):
    """adding job skills"""
    if job_id not in jobs:
        raise JobAndUserError("invalid index")

    if skill not in global_skills_set:
        raise JobAndUserError("invalid skill")

    job = jobs[job_id]
    if skill in job.skills:
        raise JobAndUserError("repeated skill")

    job.skills.append(skill)
    print("skill added")

def add_user_skill(user_id, skill):
    """adding user skills"""
    if user_id not in users:
        raise JobAndUserError("invalid index")

    if skill not in global_skills_set:
        raise JobAndUserError("invalid skill")

    user = users[user_id]
    if skill in user.skills:
        raise JobAndUserError("repeated skill")

    user.skills.append(skill)
    print("skill added")


users = {}
jobs = {}

num_skills = int(input())
global_skills = input().split()[:num_skills]

global_skills_set = set(global_skills)

n = int(input())
for _ in range(n):
    command, *data = input().split()

    try:
        if command == "ADD-JOB":
            job = Job(data[0], int(data[1]), int(data[2]), data[3], int(data[4]))
            job.validate()
            jobs[job.id] = job
            print(f"job id is {job.id}")

        elif command == "ADD-USER":
            user = User(data[0], int(data[1]), data[2], int(data[3]))
            user.validate()
            users[user.id] = user
            print(f"user id is {user.id}")

        elif command == "ADD-JOB-SKILL":
            add_job_skill(int(data[0]), data[1])

        elif command == "ADD-USER-SKILL":
            add_user_skill(int(data[0]), data[1])
        elif command == "VIEW":
            user_id = int(data[0])
            job_id = int(data[1])
            if user_id in users:
                users[user_id].view_job(job_id, jobs)
            else:
                print("invalid index")

        elif command == "JOB-STATUS":
            job_id = int(data[0])
            job_status(job_id, jobs)

        elif command == "USER-STATUS":
            user_id = int(data[0])
            user_status(user_id, users)

        elif command == "GET-JOBLIST":
            user_id = int(data[0])

            if user_id not in users:
                print("invalid index")
                continue

            user = users[user_id]
            job_scores = []

            for job_id, job in jobs.items():
                score = user.score_system(user, job)
                job_scores.append((job, score))

            job_scores.sort(key=lambda x: x[1], reverse=True)

            top_jobs = job_scores[:5]

            output = []
            for job, score in top_jobs:
                output.append(f"({job.id},{score})")
            print(''.join(output))
    except JobAndUserError as e:
        print(e)
