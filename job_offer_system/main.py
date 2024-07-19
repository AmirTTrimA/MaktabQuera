"""
Job Offer System
"""

from enum import Enum

class TimeCondition(Enum):
    """
    Time Condition Enum
    """
    FULLTIME = "FULLTIME"
    PARTTIME = "PARTTIME"
    PROJECT = "PROJECT"

class Job:
    """
    Job Class
    """
    def __init__(self) -> None:
        self.skill  = []
        self.name = ''
        self.min_age = 18
        self.max_age = 60
        self.time_cond = TimeCondition
        self.salary = 1000

    # Properties

    @property
    def skill(self):
        """
        skill property
        """
        return self.skill

    @property
    def name(self):
        """
        name property
        """
        return self.name

    @property
    def min_age(self):
        """
        min_age property
        """
        return self.min_age

    @property
    def max_age(self):
        """
        max_age property
        """
        return self.max_age

    @property
    def time_cond(self):
        """
        time_cond property
        """
        return self.time_cond

    @property
    def salary(self):
        """
        salary property
        """
        return self.salary

    # Setters

    @skill.setter
    def skill(self, *skill):
        self.skill.append(skill)

    @name.setter
    def name(self, name):
        if self.check_name(name):
            self.name = name
        else:
            # Name Error Exception
            pass

    @min_age.setter
    def min_age(self, min_age, max_age):
        if self.check_age(min_age, max_age):
            self.min_age = min_age
        else:
            # Age Violation Exception
            pass

    @max_age.setter
    def max_age(self, min_age, max_age):
        if self.check_age(min_age, max_age):
            self.max_age = max_age
        else:
            # Age Violation Exception
            pass

    @time_cond.setter
    def time_cond(self, cond):
        if self.check_time_cond(cond):
            self.time_cond = cond
        else:
            # Time Condition Error
            pass

    @salary.setter
    def salary(self, salary):
        if self.check_salary(salary):
            self.salary = salary
        else:
            # Salary Amount Exception
            pass

    def check_name(self, name):
        """
        to check whether the name is correct
        """
        if not 1 <= len(name) <= 10:
            return False
        if not name.isalpha():
            return False
        return True


    def check_age(self, min_age, max_age):
        """
        to check whether ages are correct
        """
        if (min_age < 0 or min_age > 200) and (max_age < 0 or max_age > 200):
            return False
        else:
            if min_age > max_age:
                return False
            else:
                return True


    def check_time_cond(self, time_cond):
        """
        to check whether the time condition is correct
        """
        if (time_cond == TimeCondition.FULLTIME or
            time_cond == TimeCondition.PARTTIME or
            time_cond == TimeCondition.PROJECT):
            return True
        else:
            return False

    def check_salary(self, salary):
        """
        to check whether the salary is correct
        """
        if salary < 0:
            return False
        if salary >= 1_000_000_000:
            return False
        if salary % 1000 != 0:
            return False
        return True

class User:
    """
    User Class
    """
    def __init__(self) -> None:
        self.skill = []
        self.name = ''
        self.age = 0
        self.time_cond = ['full', 'part', 'proj']
        self.salary = 1000
