# 📄 AI Resume Analyzer

An AI-powered Resume Analyzer built with **Python** and **Streamlit** that analyzes resumes, compares them with a job description, calculates an ATS score, and provides personalized improvement suggestions.

## ✨ Features

* Upload Resume in PDF format
* Extract resume text automatically
* Extract candidate details (Name, Email, Phone Number)
* Detect technical skills from the resume
* Compare resume with a Job Description
* Calculate ATS (Applicant Tracking System) Score
* Calculate Resume Similarity Score
* Display Matched and Missing Skills
* Generate Resume Improvement Suggestions
* Visualize Skill Analysis with Charts

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* Matplotlib
* PyMuPDF

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── skills.csv
├── requirements.txt
├── .gitignore
├── README.md
│
└── utils/
    ├── ats.py
    ├── charts.py
    ├── parser.py
    ├── pdf_reader.py
    ├── similarity.py
    ├── skills.py
    └── suggestions.py
```

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/sonu2727/AI-Resume-Analyzer.git
```

2. Open the project folder:

```bash
cd AI-Resume-Analyzer
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
streamlit run app.py
```

## 📊 How It Works

1. Upload a PDF resume.
2. Paste the job description.
3. Click **Analyze Resume**.
4. View:

   * Candidate Information
   * ATS Score
   * Resume Similarity Score
   * Detected Skills
   * Matched Skills
   * Missing Skills
   * Resume Suggestions
   * Skill Analysis Chart

## 🎯 Future Improvements

* AI-powered resume rewriting
* PDF report generation
* Advanced NLP-based skill extraction
* Interview question generation
* Improved ATS scoring model

## 👩‍💻 Author

**Sakshi Prajapati**

GitHub: https://github.com/sonu2727
