import google.generativeai as genai
import os
import csv
import time
genai.configure(api_key=os.getenv('GOOGLE_GEMINI_API'))
config_mode='resume'

model= genai.GenerativeModel('gemini-2.0-flash')

def generate_gemini_response(prompt_text):
    """
    Sends a text prompt to the Gemini model and returns the response.
    """
    try:
        response = model.generate_content(prompt_text)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"
def load_resume_corpus(fname='Long Format RPatel - Director of Data Science.txt'):
    textResume=""
    with open("data/"+fname,'r') as fin:
        lines=fin.readlines()
        for l in lines:
            if l=='\n':continue
            textResume+=l+'\n' 
    return textResume
def Build_CoT_Prompt(csv_dict):
    Chain_Thought_prompt=""
    Chain_Thought_prompt+="You are a job seeker with expertise in %s.\n" %csv_dict['Expertise']
    Task="Write a new tailored %s based on the listed job overview, role, skills and requirements. \n" \
            "Use my attached resume to find source material on skills and accomplishments.\
            Use a tone that will stand out to a recruiter looking for a %s role." %(config_mode,csv_dict['Role Type'])

    Chain_Thought_prompt+=Task

    Chain_Thought_prompt+="This is my resume to use as resource to build a tailored %s: " %config_mode
    Chain_Thought_prompt+=textResume #Machine readable format
    Chain_Thought_prompt+="The job overview:\n %s " %csv_dict['Overview']
    Chain_Thought_prompt+="The job skills as a bulleted list:\n %s " %csv_dict['Job Skills']
    Chain_Thought_prompt+="The job requirements as a bulleted list:\n %s " %csv_dict['Job Requirements']
    return Chain_Thought_prompt

if __name__=='__main__':
    print("Evaluating Job Description and Supporting Materials: %s" %config_mode)
    #This is its own function
    textResume=load_resume_corpus()
    print(textResume)
    #Main loop over jobs
    with open("data/JobDesc.csv",'r') as fin:
        reader=csv.DictReader(fin)
        #Print job and company 
        for row in reader:
            Chain_Thought_prompt=Build_CoT_Prompt(row)
            #Use this as chain of thought builder
            with open("output/RPatel_%s_%s.txt" %(config_mode,row['Company']),'w') as fout:
                print(row['Company'])
                response_text=generate_gemini_response(Chain_Thought_prompt)
                fout.write(response_text)
            time.sleep(3)