import matplotlib.pyplot as plt


def plot_skill_chart(matched, missing):

    matched_count = len(matched)
    missing_count = len(missing)

    fig, ax = plt.subplots(figsize=(5, 5))

    # Prevent crash when both lists are empty
    if matched_count == 0 and missing_count == 0:
        ax.text(
            0.5,
            0.5,
            "No skills to display",
            ha="center",
            va="center",
            fontsize=14
        )
        ax.axis("off")
        return fig

    labels = ["Matched Skills", "Missing Skills"]
    values = [matched_count, missing_count]

    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title("Resume Skill Analysis")

    return fig