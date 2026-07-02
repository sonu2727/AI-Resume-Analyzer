def generate_suggestions(score, missing_skills, resume_text):

    suggestions = []

    if score < 70:
        suggestions.append(
            "Improve your resume by adding more relevant technical skills."
        )

    if missing_skills:
        suggestions.append(
            "Add these skills if you know them: " +
            ", ".join(missing_skills)
        )

    if "github.com" not in resume_text.lower():
        suggestions.append(
            "Add your GitHub profile."
        )

    if "linkedin.com" not in resume_text.lower():
        suggestions.append(
            "Add your LinkedIn profile."
        )

    if "project" not in resume_text.lower():
        suggestions.append(
            "Include your academic or personal projects."
        )

    if "certification" not in resume_text.lower():
        suggestions.append(
            "Add relevant certifications."
        )

    return suggestions