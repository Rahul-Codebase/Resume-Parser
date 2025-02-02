# Resume-Parser
# A Python-based resume parser that extracts key details from resumes in multiple formats.

from resume_parser import resumeparse
import os

def scan_resume(resume):
    if not os.path.exists(resume):
        print(f"The file {resume} does not exist.")
        return

    try:
        data = resumeparse.read_file(resume)
        if not data:
            print("No data found in the resume.")
            return
        for i, j in data.items():
            print(f"{i}:>>{j}")
    except Exception as e:
        print(f"An error occurred while processing the resume: {e}")
        
scan_resume("Rahul Sharma.docx")
