"""
Job Offer System
"""
from enum import Enum

class JobError(Exception):
    """Base class for exceptions in this module."""

class FullNameError(JobError):
    """Exception raised for invalid names."""
    def __init__(self, message="Invalid name"):
        self.message = message
        super().__init__(self.message)

class AgeError(JobError):
    """Exception raised for invalid age."""
    def __init__(self, message="Invalid age"):
        self.message = message
        super().__init__(self.message)

class TimeConditionError(JobError):
    """Exception raised for invalid time conditions."""
    def __init__(self, message="Invalid time condition"):
        self.message = message
        super().__init__(self.message)

class SalaryError(JobError):
    """Exception raised for invalid salary."""
    def __init__(self, message="Invalid salary"):
        self.message = message
        super().__init__(self.message)

class TimeCondition(Enum):
    """Time Condition Enum"""
    FULLTIME = "FULLTIME"
    PARTTIME = "PARTTIME"
    PROJECT = "PROJECT"

class Job:
    """Job Class"""
    _id_counter = 1

    def __init__(self) -> None:
        self.id = Job._id_counter
        Job._id_counter += 1
        self._skills = []
        self._name = ''
        self._min_age = 18
        self._max_age = 60
        self._time_condition = TimeCondition.FULLTIME  # Default time condition
        self._salary = 1000

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
        if self._check_age(min_age, self._max_age):
            self._min_age = min_age
        else:
            raise AgeError()

    @max_age.setter
    def max_age(self, max_age):
        """Set maximum age property."""
        if self._check_age(self._min_age, max_age):
            self._max_age = max_age
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

    def _check_age(self, min_age, max_age):
        """Check whether ages are valid."""
        if (min_age < 0 or min_age > 200) or (max_age < 0 or max_age > 200):
            return False
        if min_age > max_age:
            return False
        return True

    def _check_time_condition(self, time_condition):
        """Check whether the time condition is valid."""
        return time_condition in (TimeCondition.FULLTIME,
                                   TimeCondition.PARTTIME,
                                   TimeCondition.PROJECT)

    def _check_salary(self, salary):
        """Check whether the salary is valid."""
        if salary < 0 or salary >= 1_000_000_000 or salary % 1000 != 0:
            return False
        return True

class User:
    """User Class"""
    _id_counter = 1

    def __init__(self) -> None:
        self.id = User._id_counter
        User._id_counter += 1
        self._skills = []
        self._name = ''  # Initialize _name directly
        self._age = 0  # Initialize _age directly
        self._time_condition = 'FULLTIME'  # Initialize _time_condition directly
        self._salary = 1000  # Initialize _salary directly

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
        return time_condition in (TimeCondition.FULLTIME,
                                   TimeCondition.PARTTIME,
                                   TimeCondition.PROJECT)

    def _check_salary(self, salary):
        """Check whether the salary is valid."""
        if salary < 0 or salary >= 1_000_000_000 or salary % 1000 != 0:
            return False
        return True
