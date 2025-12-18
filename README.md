# Career-Fair-Python-Simulation

This repository contains a Python-based simulation of a career fair matching
system. The project models employees, job postings, and companies, providing
tools to assess hiring suitability using structured data and vector-based
similarity measures.

At career fairs, candidates provide information about their skills, education,
and past experience, while recruiters seek the best matches for open positions.
This system is designed to make employee-job matching clear, fair, and
auditable. Each recommendation and score can be traced back to the underlying
data.

---

## Project Structure

The project is built with modular Python components:

### 1. Foundation (`utils.py`)
Functions to:
- Parse and normalize dash-separated strings into token lists  
- Build vocabularies and count vectors  
- Compute vector similarities using cosine similarity  

### 2. Data Models (`employee.py` & `job.py`)
- **Employee**: stores candidate information, skills, education, and job history  
- **Job**: stores job details, required skills, salary, and assigned employee  

### 3. Data Loader (`network.py`)
Reads CSV files with job postings and generates lists of `Job` objects.

### 4. Orchestrator (`company.py`)
- Computes skill and education similarity scores  
- Estimates hire success probabilities  
- Hires and fires employees based on quantitative metrics  

---

## Features & Learning Outcomes

- Model real-world entities using Python classes  
- Normalize and tokenize text data for analysis  
- Convert qualitative data into numeric vector representations  
- Implement cosine similarity, dot product, and Euclidean norms from scratch  
- Practice modular design for clean, maintainable code  
- Handle CSV input robustly  
- Produce auditable and reproducible hiring recommendations  

---

## Usage

1. Build and test the utilities in `utils.py`.  
2. Create `Employee` and `Job` objects to manage candidate and job data.  
3. Load job postings using `network.py`.  
4. Use `Company` to simulate hiring decisions and manage employees.  
