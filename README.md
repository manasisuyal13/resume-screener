# 📄 Resume Screener using NLP & Fuzzy Matching

This project is a Python-based Resume Screening tool designed to automate the process of shortlisting candidates by evaluating the similarity of their resumes to a given job description. It efficiently parses `.pdf` and `.docx` files, extracts textual content, and calculates a relevance score using fuzzy matching techniques — helping recruiters quickly identify top candidates.

---

## 🚀 Key Features

- 📄 **Multi-format Resume Support**: Accepts both `.pdf` and `.docx` resumes.
- 🧠 **NLP + Fuzzy Matching**: Uses natural language preprocessing and fuzzy logic to compute resume relevance.
- ⚙️ **Automated Ranking**: Sorts all resumes by their similarity scores and highlights the top candidates.
- 🔎 **Keyword-aware Matching**: Takes into account job-specific skills and keywords for accurate screening.
- 📂 **Easy Folder-Based Setup**: Just drop your resumes in a folder and it works out-of-the-box.

---

## 📁 Project Structure

```
resume-screener/
│
├── resume_screener.py         # Main Python script for screening logic
├── job_description.txt        # Contains target job description or keyword set
├── resumes/                   # Folder where all resumes are stored
└── README.md                  # This file
```

---

## ⚙️ How It Works

1. **Text Extraction**: The script extracts text from each resume file using `pdfplumber` for PDFs and `python-docx` for Word documents.
2. **Job Description Parsing**: It reads the job description from a text file and tokenizes it into relevant keywords.
3. **Fuzzy Matching**: Each resume is compared against the job description using `fuzzywuzzy`’s ratio scoring.
4. **Scoring & Ranking**: The resumes are scored, sorted in descending order of similarity, and the results are displayed in the terminal.

---

## 💻 Setup & Installation

Follow these simple steps to get the project running on your machine:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/resume-screener.git
   cd resume-screener
   ```

2. **Install Required Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   Or install individually:
   ```bash
   pip install pdfplumber python-docx fuzzywuzzy nltk
   ```

3. **Prepare Your Files**
   - Place all resumes inside the `resumes/` directory.
   - Paste your job description or required keywords into `job_description.txt`.

4. **Run the Screener**
   ```bash
   python resume_screener.py
   ```

---

## 🧪 Sample Output

```
Processing 5 resumes...

Rohit_SDE.pdf: Score = 87.45%
Aarti_Analyst.docx: Score = 75.80%
Mohit_ML.pdf: Score = 67.20%

Top 3 resumes:
1. Rohit_SDE.pdf — 87.45%
2. Aarti_Analyst.docx — 75.80%
3. Mohit_ML.pdf — 67.20%
```

---

## 🛠 Technologies Used

- **Python 3** – Core scripting language
- **pdfplumber** – Extracts text from PDFs
- **python-docx** – Parses DOCX files
- **fuzzywuzzy** – Implements fuzzy string comparison
- **NLTK** – Used for tokenization and text preprocessing

---

## 💡 Potential Enhancements

- Export ranked results to CSV or Excel
- Add Streamlit GUI for visual interaction
- Introduce weight-based keyword importance
- Integrate external APIs or cloud storage
- Add resume parsing via NLP-based named entity recognition (NER)

---

## 👩‍💻 Author

**Manasi Suyal**  
🎓 B.Tech CSE | AI & Data Enthusiast  
📧 [manasisuyal2003@gmail.com](mailto:manasisuyal2003@gmail.com)  
🔗 [GitHub](https://github.com/manasisuyal13) • [LinkedIn](https://www.linkedin.com/in/manasi-suyal-95a64621b/)

---
