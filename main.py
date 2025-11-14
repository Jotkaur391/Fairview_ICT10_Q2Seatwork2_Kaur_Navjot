from pyscript import document

def compute_order(event):
    # Get student name
    fname = document.getElementById("cust_fname").value or "N/A"
    lname = document.getElementById("cust_lname").value or "N/A"

    # Get grades (convert empty inputs to 0)
    grades = {
        "Math": float(document.getElementById("item1").value or 0),
        "English": float(document.getElementById("item2").value or 0),
        "Science": float(document.getElementById("item3").value or 0),
        "Filipino": float(document.getElementById("item4").value or 0),
        "PE": float(document.getElementById("item5").value or 0),
        "ICT": float(document.getElementById("item6").value or 0),
    }

    # Compute general average
    total = sum(grades.values())
    gwa = total / len(grades)

    # Build summary text
    grade_list = "\n".join([f"📘 {subj}: {grade}" for subj, grade in grades.items()])

    summary_text = f"""
📚 STUDENT SUMMARY

👤 Name: {fname} {lname}

📝 Grades:
{grade_list}

🎓 GENERAL AVERAGE: {gwa:.2f}
"""

    # Display summary
    document.getElementById("summary").innerText = summary_text
