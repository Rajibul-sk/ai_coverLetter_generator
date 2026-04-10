import streamlit as st
import google.generativeai as genai
genai.configure(api_key = "AIzaSyA5A5h2GM7clsbYFUCp64_xim_yN5jK4SY")
use_model = genai.GenerativeModel("gemini-2.5-flash")
st.title("AI-Powered Cover Letter Generator")
job_title = st.text_input("Enter Job Title")
resume_summary = st.text_area("Enter Resume Summary")
if st.button("Generate Cover Letter"):
    if job_title and resume_summary:
        prompt = f"Write A Cover Letter for {job_title} using these resume points: {resume_summary}"
        response = use_model.generate_content(prompt)
        st.write(response.text)
else:
    st.warning("Please provide both job title and resume summary.")