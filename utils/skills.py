import pandas as pd

def extract_skills(text):
    skills_df = pd.read_csv("skills.csv")

    text = text.lower()

    found_skills = []

    for skill in skills_df["Skill"]:
        skill = str(skill).strip()

        if skill.lower() in text:
            found_skills.append(skill)

    print("TEXT:", text)
    print("FOUND SKILLS:", found_skills)

    return sorted(set(found_skills))