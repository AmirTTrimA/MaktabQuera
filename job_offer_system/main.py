"""
Job Offer System
"""
from enum import Enum

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
    def __init__(self, message="Invalid timetype"):
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
        self.views = 0  # Track total views
        self.skill_views = {}  # Track views per skill

    def __str__(self) -> str:
        return f'User {self.id}: Name: {self.name}, Min Age: {self.min_age}, Max Age: {self.max_age}, Time Condition: {self.time_condition}, Salary: {self.salary}'

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
        self.total_views = 0  # Track total job views
        self.skill_views = {}  # Track views per skill

    def __str__(self) -> str:
        return f'User {self.id}: Name: {self.name}, Age: {self.age}, Time Condition: {self.time_condition}, Salary: {self.salary}'

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

    def view_job(self, job_id, joblist):
        """User views a job, incrementing its view count based on all of the user's skills."""
        # print(f"Current jobs: {joblist}")  # Debug print
        if job_id not in joblist:
            print("invalid index")  # Job does not exist
            return
        job = joblist[job_id]

        # Check if the user has any skills to use for viewing
        # print(f"User Skills for {self.name}: {self._skills}")  # Debug print
        if not self._skills:
            print("invalid index")  # No skills to view the job
            return

        # Increment view count for each of the user's skills
        for skill in self._skills:
            job.increment_view(skill)  # Increment view using the user's skill
            self.total_views += 1  # Increment total views for the user
            if skill in self.skill_views:
                self.skill_views[skill] += 1
            else:
                self.skill_views[skill] = 1

        print("tracked")

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
        print(f"invalid index")
        return

    job = jobs[job_id]
    total_views = job.views
    skill_views = job.skill_views

    # Prepare a list of all skills with their view counts
    all_skills = job._skills  # Assuming _skills holds all skills for the job
    skill_views_output = []

    for skill in all_skills:
        count = skill_views.get(skill, 0)  # Default to 0 if skill has no views
        skill_views_output.append(f"{skill},{count}")

    # Prepare the final output
    skills_output = ", ".join(skill_views_output)

    if all_skills:
        print(f"{job.name}-{total_views}-({skills_output})")
    else:
        print(f"{job.name}-{total_views}-")  # No skills, just show job name and total views

def user_status(user_id, users):
    """Display the status of a user."""
    if user_id not in users:
        print(f"invalid index")
        return

    user = users[user_id]
    total_views = user.total_views
    skill_views = user.skill_views

    # Prepare a list of all skills with their view counts
    all_skills = user._skills  # Assuming _skills holds all skills for the user
    skill_views_output = []

    for skill in all_skills:
        count = skill_views.get(skill, 0)  # Default to 0 if skill has no views
        skill_views_output.append(f"{skill},{count}")

    # Prepare the final output
    skills_output = ", ".join(skill_views_output)

    if all_skills:
        print(f"{user.name}-({skills_output})")
    else:
        print(f"{user.name}-")  # No skills, just show user name



def add_job_skill(job_id, skill):
    # Check if job_id exists
    if job_id not in jobs:
        raise JobAndUserError("invalid index")

    # Check if skill is in global skills
    if skill not in global_skills_set:
        raise JobAndUserError("Invalid skill")

    # Check if the skill is already associated with the job
    job = jobs[job_id]
    if skill in job.skills:  # Assuming job.skills is a list or set of skills
        raise JobAndUserError("repeated skill")

    # If all checks pass, add the skill to the job
    job.skills.append(skill)  # or use job.skills.add(skill) if it's a set
    print("skill added")

def add_user_skill(user_id, skill):
    # Check if user_id exists
    if user_id not in users:
        raise JobAndUserError("invalid index")

    # Check if skill is in global skills
    if skill not in global_skills_set:
        raise JobAndUserError("Invalid skill")

    # Check if the skill is already associated with the user
    user = users[user_id]
    if skill in user.skills:  # Assuming user.skills is a list or set of skills
        raise JobAndUserError("repeated skill")

    # If all checks pass, add the skill to the user
    user.skills.append(skill)  # or use user.skills.add(skill) if it's a set
    print("skill added")


users = {}
jobs = {}

# Read the number of global skills
num_skills = int(input())
global_skills = input().split()[:num_skills]  # Read the skills list

# Assuming you have a list or set to store global skills
global_skills_set = set(global_skills)  # Use a set for unique skills

n = int(input())
for _ in range(n):
    command, *data = input().split()

    try:
        if command == "ADD-JOB":
            job = Job(data[0], int(data[1]), int(data[2]), data[3], int(data[4]))
            job.validate()  # Validate must be called before adding to jobs
            jobs[job.id] = job
            # print(job)
            print(f"job id is {job.id}")

        elif command == "ADD-USER":
            user = User(data[0], int(data[1]), data[2], int(data[3]))
            user.validate()  # Validate must be called before adding to users
            users[user.id] = user
            # print(user)
            print(f"user id is {user.id}")

        elif command == "ADD-JOB-SKILL":
            add_job_skill(int(data[0]), data[1])  # Ensure ID is an integer

        elif command == "ADD-USER-SKILL":
            add_user_skill(int(data[0]), data[1])  # Ensure ID is an integer

        elif command == "VIEW": # if a user doesn't have any skills and view a job, beacause of the no skill situation it will be a invalid index error
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

    except JobAndUserError as e:
        print(e)  # Print the error message

# print(jobs)
# print(users)
