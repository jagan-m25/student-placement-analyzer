import streamlit as st

st.title("🎓 Student Placement Predictor")

st.write("Enter your details below")

name = st.text_input("Student Name")
cgpa = st.number_input("CGPA", 0.0, 10.0, 7.0)
python_score = st.number_input("Python Score", 0, 100, 50)
communication = st.number_input("Communication Score", 0, 100, 50)
internship = st.selectbox("Internship Completed?", ["Yes", "No"])
projects = st.number_input("Number of Projects", 0, 20, 1)

if st.button("Predict Placement"):
    st.success("Prediction system is ready!")