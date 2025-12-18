"""
Employee data model for the career fair system.

This module defines the Employee class, which represents a candidate with
demographic information, education level, skills, and job history.
"""
# Morgan Yu 261294882
# All code limited to 79 characters per line using wordWrapColumn in VS Code
# Global variables and modules

from utils import get_list

# Question 2 The data model: employee.py, job.py, company.py
# Part 2.1 Class Employee (in employee.py)
class Employee:
    """
    Represents a candidate attending the career fair.

    An Employee stores identifying information, education level, previous
    jobs, skills, and an optional current job. The class also provides
    utilities to display the employee profile and update job history.
    """

    # Part 2.1.1 Attributes
    def __init__(self, name, age, gender, education, prev_jobs, skills, cur_job = None):
        """
        Initialize a new Employee object.

        Parameters:
        name (str): Employee name.
        age (int): Age in years, must be between 0 and 120.
        gender (str): Gender identifier ('m', 'f', or 'x'), case insensitive.
        education (str or False): Education level or False (treated as 'none').
        prev_jobs (str): Dash-separated string of previous job titles.
        skills (str): Dash-separated string of skills.
        cur_job (str or None): Current job title, if any.

        Raises:
        ValueError: If age, gender, or education are invalid.
        """
        # Check that age is within the valid range
        if not (0 <= age <= 120):
            raise ValueError('Enter a valid age')
        
        # Check that gender is one of the allowed values (case insensitive)
        allowed_genders = {'m', 'f', 'x'}
        if gender.lower() not in allowed_genders:
            raise ValueError('Enter a valid gender')
        
        # Check that education is valid, handle False as 'none'
        allowed_education = {'none', 'high school', 'bachelors', 'masters', 'phd'}
        # Handle False as "none" since there is an input False in 2.2.1.2 __str__
        if education is False:
            education = 'none'
        elif type(education) is str:
            education = education.lower()
        else:
            raise ValueError('Enter a valid education')
        
        if education.lower() not in allowed_education:
            raise ValueError('Enter a valid education')


        self.name = name
        self.age = age
        self.gender = gender.lower()  # normalized lowercase
        self.education = education.lower()  # normalized lowercase
        self.prev_jobs = prev_jobs  # dash-separated string
        self.skills = skills  # dash-separated string
        self.cur_job = cur_job  # string or None
    
    # Part 2.1.2.2 __str__
    def __str__(self):
        """
        Return a human-readable string summary of the employee.

        The output includes normalized fields and converts dash-separated
        skills and previous jobs into lists using get_list.
        """
        # Convert dash-separated strings into lists for display
        skills_list = get_list(self.skills)
        prev_jobs_list = get_list(self.prev_jobs)


        s = ''
        s += 'Name: ' + self.name + '\n'
        s += 'Age: ' + str(self.age) + '\n'
        s += 'Gender: ' + self.gender + '\n'
        s += 'Highest education: ' + self.education + '\n'
        s += 'Skills: ' + str(skills_list) + '\n'
        s += 'Previous jobs: ' + str(prev_jobs_list) + '\n'
        s += 'Current job: ' + str(self.cur_job)
        
        return s
    
    # Part 2.1.2.3 add_prev_job
    def add_prev_job(self, job):
        """
        Append a new job title to the employee's previous jobs.

        Parameters:
        job (str): Job title to add.

        Raises:
        TypeError: If job is not a string.
        """
        # Check that the input job is a string
        if type(job) != str:
            raise TypeError("Error in Class Employee: The input job should be a string")
        
        # Normalize job title to lowercase
        job = job.lower()

        # If there are no previous jobs, set prev_jobs to job; else append
        if self.prev_jobs.strip() == "":
            self.prev_jobs = job
        
        else:
            self.prev_jobs += "-" + job




# c1 = Employee('James Bond', 35, 'M', 'high school', 'Spy', 'Martial artist-Knife mastery-spy-driver-card player')
# print(c1)

# c1.add_prev_job('Security Analyst')
# print(c1)


              

              
