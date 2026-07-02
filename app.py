import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.skills import extract_skills
from utils.ats import calculate_ats_score
from utils.similarity import calculate_similarity
from utils.charts import plot_skill_chart
from utils.parser import extract_name, extract_email, extract_phone
from utils.suggestions import generate_suggestions
# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ----------------------------
# Title
# ----------------------------
st.title("📄 AI Resume Analyzer")
st.write("Analyze your resume and compare it with a Job Description using AI.")

st.divider()

# ----------------------------
# Upload Resume
# ----------------------------
resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# ----------------------------
# Upload Job Description
# ----------------------------
job_description = st.text_area(
    "Paste Job Description Here",
    height=200
)

# ----------------------------
# Analyze Button
# ----------------------------
if st.button("Analyze Resume"):

    if resume_file is None:
        st.error("Please upload your resume.")
    elif job_description.strip() == "":
        st.error("Please paste a Job Description.")
    else:
        st.success("Everything looks good!")
        st.write("Resume Uploaded:", resume_file.name)

        st.subheader("Job Description")
        st.write(job_description)

        resume_text = extract_text_from_pdf(resume_file)


        candidate_name = extract_name(resume_text)
        candidate_email = extract_email(resume_text)
        candidate_phone = extract_phone(resume_text)




        skills = extract_skills(resume_text)
        score, matched_skills, missing_skills = calculate_ats_score(
            resume_text,
            job_description
        )


        suggestions = generate_suggestions(
        score,
        missing_skills,
        resume_text
        )
        
        st.write("Matched Skills:", matched_skills)
        st.write("Missing Skills:", missing_skills)

        chart = plot_skill_chart(
        matched_skills,
        missing_skills
        )

        similarity = calculate_similarity(
        resume_text,
        job_description
        )

        st.subheader("Candidate Information")

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Name:**", candidate_name)
            st.write("**Email:**", candidate_email)

        with col2:
            st.write("**Phone:**", candidate_phone)

        st.subheader("Detected Skills")

        if skills:
            for skill in skills:
                st.success(skill)

        else:
            st.warning("No skills detected.")

        st.subheader("ATS Score")

        st.progress(score / 100)

        st.metric(
            label="Resume Score",
            value=f"{score}%"
        )

        st.subheader("Resume Similarity")

        st.progress(similarity / 100)

        st.metric(
            label="Similarity Score",
            value=f"{similarity}%"
        )



        st.subheader("Matched Skills")

        if matched_skills:
            st.write(", ".join(matched_skills))
        else:
            st.warning("No matched skills found.")



        st.subheader("Missing Skills")

        if missing_skills:
            st.write(", ".join(missing_skills))
        else:
            st.success("No missing skills 🎉")

        st.subheader("💡 Resume Suggestions")

        if suggestions:
            for suggestion in suggestions:
                st.info(suggestion)
        else:
            st.success("Your resume looks good!")
        st.subheader("Skill Analysis Chart")

        st.pyplot(chart)


        st.subheader("Extracted Resume Text")


        st.text_area(
            "Resume Content",
            resume_text,
            height=350
        )
        st.subheader("Detected Skills")

