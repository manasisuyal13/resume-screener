import fitz  # PyMuPDF for PDF
import docx  # For Word documents
from fuzzywuzzy import fuzz

# ---------- STEP 1: Load text from files ----------

def load_text_from_pdf(path):
    """Extract text from a PDF file."""
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.lower().strip()

def load_text_from_docx(path):
    """Extract text from a DOCX file."""
    doc = docx.Document(path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text.lower().strip()

def load_text(path):
    """Determine file type and load text accordingly."""
    if path.endswith('.pdf'):
        return load_text_from_pdf(path)
    elif path.endswith('.docx'):
        return load_text_from_docx(path)
    else:
        raise ValueError("Unsupported file type. Please upload a PDF or DOCX file.")

# ---------- STEP 2: Define skills to match ----------

SKILLS = [
    "python", "sql", "machine learning", "deep learning", "nlp",
    "data analysis", "pandas", "tensorflow", "pytorch", "cloud",
    "git", "opencv", "flask", "power bi"
]

# ---------- STEP 3: Extract skills from text ----------

def extract_skills(text):
    found = []
    for skill in SKILLS:
        if skill in text:
            found.append(skill)
    return found

# ---------- STEP 4: Generate score report ----------

def generate_match_score(resume, jd):
    resume_skills = extract_skills(resume)
    jd_skills = extract_skills(jd)

    common_skills = set(resume_skills) & set(jd_skills)
    total_jd_skills = len(set(jd_skills))

    skill_match_pct = (len(common_skills) / total_jd_skills) * 100 if total_jd_skills else 0
    similarity_score = fuzz.token_set_ratio(resume, jd)

    report = f"""
📄 Resume Screening Report
-----------------------------
✅ Matched Skills: {list(common_skills)}
🎯 Skill Match %: {skill_match_pct:.2f}%
🔁 Text Similarity: {similarity_score}%

Total Resume Skills Found: {len(resume_skills)}
Total JD Skills Required: {total_jd_skills}
"""
    return report

# ---------- STEP 5: Main ----------

if __name__ == "__main__":
    print("Please upload your resume (PDF or DOCX format):")
    resume_path = input("Enter the path to your resume file: ")

    try:
        # Load and process the resume
        resume_text = load_text(resume_path)
        
        # You can hardcode a job description for testing or ask for input from the user
        jd_text = """
        Job Description: Data Analyst
        Required Skills: Python, SQL, Machine Learning, Data Analysis, Deep Learning
        """

        # Generate the matching report
        report = generate_match_score(resume_text, jd_text)

        # Print the report
        print(report)
        
        # Save the report to a file
        with open("score_report.txt", "w") as f:
            f.write(report)

        print("✅ Screening complete. Check 'score_report.txt' for the details.")

    except Exception as e:
        print(f"Error: {e}")
