import network
from employee import Employee
from job import Job
import utils
import math

#2.3 Class Company

class Company:
    '''
    A Company owns a booth and keeps track of people hired during the fair and
    roles that are still open
    '''

    #2.3.1 Required methods

    #2.3.1.1 __init__

    def __init__(self,name,location,employees,jobs_csv=None):
        """
        This constructor creates a company, stores its location and initial
        employees, and optionally loads open jobs from a CSV by calling create
        job list from network.py
        """

        #Attributes
        self.name=name
        self.location=location
        self.employees=employees
        self.jobs_csv=jobs_csv

        #Load jobs from CSV if filename provided,otherwise create empty job list
        if jobs_csv is not None:
            self.jobs = network.create_job_list(jobs_csv)
        else:
            self.jobs = []
    
    #2.3.1.2 __str__

    def __str__(self):
        '''
        This method returns a multi line summary that includes the company
        name,location,and counts of employees and open jobs for quick booth
        status boards
        '''

        #String output
        summary = "Name: "+self.name+"\n" \
                  "Location: "+self.location+"\n" \
                  "Number of employees: "+str(len(self.employees))+"\n" \
                  "Number of available jobs: "+str(len(self.jobs))

        return summary
    
    #2.3.1.3 skills_similarity

    def skills_similarity(self, job, employee):
        '''
        Calculate skills similarity between a job and employee
        '''

        #Tokenize employee skills using get_list
        emp_tokens=utils.get_list(employee.skills)
        
        #Tokenize job keywords using get_list
        job_tokens=utils.get_list(job.keywords)
        
        #Build shared vocabulary 
        vocab = []
        for token in emp_tokens:
            if token not in vocab:
                vocab.append(token)
        for token in job_tokens:
            if token not in vocab:
                vocab.append(token)
        
        #Create count vectors using utils.vectorize
        x_emp=utils.vectorize(emp_tokens,vocab)
        x_job=utils.vectorize(job_tokens,vocab)
        
        #Calculate and return cosine similarity
        skill_sim=utils.cosine_similarity(x_emp,x_job)
        return skill_sim

    #2.3.1.4 education_similarity

    def education_similarity(self, employee):
        '''
        Calculate education similarity between an employee and the company
        '''

        #Education domain
        education_domain=["none","high school","bachelors","masters","phd"]
        
        #Create one-hot vector for the employee
        employee_vector=[0,0,0,0,0]
        employee_index=education_domain.index(employee.education)
        employee_vector[employee_index]=1
        
        #Create count vector by counting employees assigned to jobs
        company_vector=[0,0,0,0,0]
        for job in self.jobs:
            if job.employee is not None:
                emp_index=education_domain.index(job.employee.education)
                company_vector[emp_index]=company_vector[emp_index]+1
        
        #Zero out all entries below the employee's level
        i=0
        while i<employee_index:
            company_vector[i]=0
            i+=1
        
        # Calculate and return cosine similarity
        education_sim=utils.cosine_similarity(employee_vector,company_vector)
        return education_sim

    #2.3.1.5 estimate_hire_success

    def estimate_hire_success(self, job, employee):
        '''
        Calculates a hiring score by combining skills similarity and education
        similarity using a weighted average. Returns 0.0 if the job is already
        filled
        '''

        # If job already has an assigned employee, return 0.0
        if job.employee is not None:
            return 0.0
        
        # Calculate skills similarity
        s_skills = self.skills_similarity(job, employee)
        
        # Calculate education similarity
        s_education = self.education_similarity(employee)
        
        # Compute weighted average
        score = 0.8 * s_skills + 0.2 * s_education
        
        # Round to two decimals and return
        return round(score, 2)

    #2.3.1.6 hire

    def hire(self,job_candidates):
        '''
        Hires the best eligible candidate for each job reference provided.
        Processes jobs in dictionary insertion order and returns a dictionary
        mapping job references to hired employees (or None).
        '''

        result = {}
        
        #Process each job reference in insertion order
        for job_ref in job_candidates:

            #Find the job with this reference
            job=None
            i=0
            while i<len(self.jobs) and job is None:
                if self.jobs[i].ref==job_ref:
                    job=self.jobs[i]
                i+=1
            
            #If job reference is unknown,store None
            if job is None:
                result[job_ref]=None

            #If job already has an employee, store that employee
            elif job.employee is not None:
                result[job_ref] = job.employee

            #Find the best eligible candidate
            else:
                best_candidate=None
                best_score=-1
                
                candidates=job_candidates[job_ref]
                for candidate in candidates:
                    # Skip candidates who already have a current job
                    if candidate.cur_job is None:

                        #Calculate hiring score
                        score=self.estimate_hire_success(job,candidate)
                        
                        #Keep strictly highest score
                        if score>best_score:
                            best_score=score
                            best_candidate=candidate
                
                #If a best candidate was found, hire them
                if best_candidate is not None:

                    #Set candidate's current job to the job title
                    best_candidate.cur_job=job.title
                    
                    #Assign candidate to the job
                    job.employee=best_candidate
                    
                    #Add candidate to company's employee list
                    self.employees.append(best_candidate)
                    
                    #Store in result
                    result[job_ref]=best_candidate
                else:

                    #No eligible candidate found
                    result[job_ref]=None
        
        return result

    #2.3.1.7 fire
    def fire(self, employee):
        '''
        Removes the given employee from their current job at the company.
        Raises AssertionError if the employee is not part of the organization
        '''

        #Check if employee is in the company's employee list
        employee_found=False
        for emp in self.employees:
            if emp is employee:
                employee_found=True
        
        #If employee is not part of the organization, raise AssertionError
        if not employee_found:
            raise AssertionError("Employee isn't a part of the organization")
        
        #Find the job this employee is assigned to and clear it
        for job in self.jobs:
            if job.employee is employee:
                job.employee=None
        
        #Clear the employee's current job
        employee.cur_job=None
        
        #Remove employee from the company's employee list
        new_employees=[]
        for emp in self.employees:
            if emp is not employee:
                new_employees.append(emp)
        self.employees=new_employees