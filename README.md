# FuzzyWuzzyLogic

This tool contains a Python script for matching skills and experiences from a resume with reference skills and experiences using the FuzzyWuzzy library.

## Description

The script reads content from a JSON file containing resume data, including skills and work experiences. It then calculates similarity scores between the skills and experiences from the resume and predefined reference skills and experiences using the FuzzyWuzzy library.

## Usage

1. Ensure you have Python installed on your system.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Prepare your resume data in JSON format and save it as `resume.json`.
4. Run the Python script `resume_matching.py`.
5. The script will output matching experiences with high similarity scores and similarity scores for skills.

## Requirements

- Python 3.x
- FuzzyWuzzy library

## Files

- `resume_matching.py`: Python script for matching skills and experiences.
- `resume.json`: Sample resume data in JSON format.
- `requirements.txt`: List of required Python libraries.
