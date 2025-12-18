# Morgan Yu 261294882
# All code limited to 79 characters per line using wordWrapColumn in VS Code
# Global variables and modules

from job import Job

# Question 3 CSV loader: network.py 
# This module handles loading job data from a CSV file and creating Job objects.

# Part 3.1 create_job_list

from job import Job

def create_job_list(csv_filename):
    """
    Reads a CSV file containing job data and returns a list of Job objects.

    Parameters:
    csv_filename (str): The path to the CSV file to be read.

    Returns:
    list: A list of Job objects created from the CSV data.

    Behavior:
    Opens the CSV file, reads each line, splits the line into job title,
    keywords, and salary. Skips any malformed rows or rows with invalid
    salary data. Returns all successfully parsed Job objects.
    """
    jobs = []
    try:
        # Attempt to open the CSV file for reading
        f = open(csv_filename, 'r')
        for line in f:
            # Remove leading/trailing whitespace from the line
            line = line.strip()
            # Split the line by commas into parts
            parts = line.split(',')
            if len(parts) == 3:
                title = parts[0]
                keyword_string = parts[1]
                salary_string = parts[2]
                try:
                    # Convert salary string to float
                    salary = float(salary_string)
                    keyword = []
                    # Split keyword string by '-' and parse each keyword
                    temp_keyword = keyword_string.split('-')
                    index = 0
                    while index < len(temp_keyword):
                        # Strip whitespace from each keyword and add to list
                        keyword.append(temp_keyword[index].strip())
                        index += 1
                    # Create a Job object and append to jobs list
                    job = Job(title, keyword, salary)
                    jobs.append(job)
                except Exception as e:
                    # Handle exceptions during salary conversion or keyword parsing
                    print('Exception caught:', e)
        f.close()
    except Exception as e:
        # Handle exceptions during file opening
        print('Exception caught:', e)

    return jobs