import streamlit as st

# Title and description
st.title("AUDIT-C Alcohol Use Screening Calculator")
st.write("""
### Welcome to the AUDIT-C Alcohol Use Screening Calculator
The AUDIT-C is a brief screening tool to identify individuals with risky drinking behavior. 
Answer the following questions about your alcohol consumption to calculate your AUDIT-C score and assess your risk.
""")

# Questions for AUDIT-C
q1 = st.radio(
    "1. How often do you have a drink containing alcohol?",
    ("Never", "Monthly or less", "2-4 times a month", "2-3 times a week", "4 or more times a week")
)

q2 = st.radio(
    "2. How many standard drinks containing alcohol do you have on a typical day when you are drinking?",
    ("1 or 2", "3 or 4", "5 or 6", "7 to 9", "10 or more")
)

q3 = st.radio(
    "3. How often do you have six or more drinks on one occasion?",
    ("Never", "Less than monthly", "Monthly", "Weekly", "Daily or almost daily")
)

# Scoring logic for AUDIT-C
def calculate_audit_c(q1, q2, q3):
    score_q1 = {"Never": 0, "Monthly or less": 1, "2-4 times a month": 2, "2-3 times a week": 3, "4 or more times a week": 4}
    score_q2 = {"1 or 2": 0, "3 or 4": 1, "5 or 6": 2, "7 to 9": 3, "10 or more": 4}
    score_q3 = {"Never": 0, "Less than monthly": 1, "Monthly": 2, "Weekly": 3, "Daily or almost daily": 4}
    
    total_score = score_q1[q1] + score_q2[q2] + score_q3[q3]
    return total_score

# Calculate and display AUDIT-C score
audit_c_score = calculate_audit_c(q1, q2, q3)
st.subheader(f"Your AUDIT-C Score: {audit_c_score}")

# Interpretation of the score
if audit_c_score >= 8:
    st.write("You are at high risk of alcohol-related problems and should seek professional advice.")
elif audit_c_score >= 4:
    st.write("You may be at risk of alcohol-related problems. Consider speaking to a healthcare provider.")
else:
    st.write("You are at low risk of alcohol-related problems.")

