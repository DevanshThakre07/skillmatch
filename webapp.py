import streamlit as st
from pdfextractor import text_extractor
import google.generativeai as genai
import os

# configure the model
key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-2.5-flash-lite')

resume_text = job_desc = None 

st.title('Resume')
file = st.sidebar.file_uploader('Resume',type = ['pdf'])
# flag = st.button('Click')
if file:
    resume_text = text_extractor(file)

    # st.write(resume_text)

# lest define the main page
st.title('AI assited skill matching tool')

st.markdown('This application will match your resume and the job description and will create a discriptive report')
# st.title(tips)

job_desc = st.text_area('Copy and past job desc',max_chars=10000)

prompt = f'''Assume that you are a expert in skill math from two different file. You need to macth the following resume with the job description 
provided by the 
resume = {resume_text}
job description = {job_desc}
Your output should be as follows:
* Give a brief desciption of the applicant in 3 to 5 lines.
* Give a range expected ATS score along with the maching and non matching wards 
* Give the chances of getting shortlisted for this possition in percentage.
* Perform SWOT analysis and discuss each and everthing in bullet points 
* Suggested what all improvemets can be resume in order to get better ATS and include percentage 
* Also create two customised resumes as per the job description provid
* perpare a one page resume in such a format that can be copied and pasted in world
* Use bullet points and tables where ever required
'''

button = st.button('click')
if job_desc:
    if resume_text:
        response = model.generate_content(prompt)
        st.write(response.text)
    else :
        print('something is miss')