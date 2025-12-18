# Morgan Yu 261294882
# All code limited to 79 characters per line using wordWrapColumn in VS Code
# Global variables and modules

from utils import get_list
from employee import Employee

# Question 2 The data model: employee.py, job.py, company.py
# Part 2.2 Class Job (in job.py)

class Job:
    """
    Represents a job position with a title, keywords describing the job,
    a salary, and an optional associated Employee. 

    Attributes:
        nb_jobs (int): Class-level counter tracking number of Job instances.
        ref (int): Unique reference number for each Job instance.
        title (str): The job title.
        keywords (str): Dash-separated string of keywords related to the job.
        salary (float): The salary for the job; must be non-negative.
        employee (Employee or None): The employee assigned to the job, if any.
    """

    # 2.2.1 Required methods
    # 2.2.1.1 __init__ 
    
    # Class attribute
    nb_jobs = 0

    def __init__(self, title, keywords, salary, employee = None):
        """
        Initializes a Job instance.

        Args:
            title (str): The job title.
            keywords (str): Dash-separated keywords describing the job.
            salary (float): The salary for the job; must be non-negative.
            employee (Employee or None): The employee assigned to the job.

        The class attribute nb_jobs is incremented to assign a unique reference
        number to each Job instance.

        Raises:
            ValueError: If salary is negative.
        """
        # Validate salary is non-negative
        if salary < 0:
            raise ValueError('Salary cannot be negative')
        
        # Increment class counter and assign ref
        Job.nb_jobs += 1  # increment the number of Job instances created
        self.ref = Job.nb_jobs  # assign unique reference number

        # Instance attributes
        self.title = title
        self.keywords = keywords  # dash-separated string
        self.salary = salary
        self.employee = employee  # Employee object or None
    
    # Part 2.2.1.2 __str__
    def __str__(self):
        """
        Returns a string representation of the Job instance.

        The keywords string is converted to a list using get_list for display.
        The employee is displayed by name if assigned, otherwise 'None'.
        """
        # Convert keywords string to list for display
        keywords_list = get_list(self.keywords)
            
        # Construct output string with job details
        s = 'Reference: ' + str(self.ref) + '\n'
        s += 'Title: ' + self.title + '\n'
        s += 'Keywords: ' + str(keywords_list) + '\n'
        s += 'Salary: ' + str(self.salary) + '\n'
        s += 'Employee: ' + (self.employee.name if self.employee is not None else 'None')

        return s 
        

# description = 'optimize - fraud - detection - software - poker'
# job1 = Job('Fraud Analytics Manager', description, 120000)
# print(job1)

# empl = Employee('James', 0, 'M', 'high school', 'Spy', 'Martial artist')
# job2 = Job('Poker Player', description, 5000, empl)
# print(job2)