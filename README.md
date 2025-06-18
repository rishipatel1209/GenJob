# GenJob
A simple python script that uses the Gemini Generative AI API, to create either a resume or a cover letter.  The main inputs of the algorithm are: 
1. A txt file for a machine readable version of your resume
2. A csv file with a breakdown of the Job Desc in terms of the following columns:
* Company,Category,Position,Expertise,Overview.Job Skills,Job Requirements,Role Type
* These are stored in the ``data/`` folder

The script turns the input information into a prompt sent to Gemini-Flash 2.0. The output information is stored in the ``output/`` folder.

# Main Requirements
```
pip install google-generativeai
```
Use your API key (passed as an environment variable)

# Gen AI Prompt

The main compenents are : 
1. The role and expertise of the job seeker
2. Pass the text resume in long format: make it as long as possible to pull a large corpus of possible skill sets
3. Job Desc as divided into components: Overview, a soft-skillset, and a list of job requirements. 