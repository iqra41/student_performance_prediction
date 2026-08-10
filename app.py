import streamlit as st
import pickle
import pandas as pd

# Load trained model
with open("model/student_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page settings
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Performance Prediction")
st.write("Enter student information to predict performance.")

st.divider()

# Student inputs
gender = st.selectbox(
    "Gender",
    ["M", "F"]
)

nationality = st.selectbox(
    "Nationality",
    [
        "KW",
        "Jordan",
        "Iraq",
        "Palestine",
        "Lebanon",
        "SaudiArabia",
        "Egypt",
        "USA",
        "Tunis",
        "Syria",
        "Iran",
        "Lybia"
    ]
)

place_of_birth = st.text_input(
    "Place of Birth",
    "Kuwait"
)

stage_id = st.selectbox(
    "Stage",
    ["lowerlevel", "MiddleSchool", "HighSchool"]
)

grade_id = st.selectbox(
    "Grade",
    [
        "G-01",
        "G-02",
        "G-03",
        "G-04",
        "G-05",
        "G-06",
        "G-07",
        "G-08",
        "G-09",
        "G-10",
        "G-11",
        "G-12"
    ]
)

section_id = st.selectbox(
    "Section",
    ["A", "B", "C"]
)

topic = st.selectbox(
    "Topic",
    [
        "English",
        "Spanish",
        "French",
        "Arabic",
        "Science",
        "Math",
        "History",
        "Biology",
        "Chemistry",
        "Geology",
        "IT"
    ]
)

semester = st.selectbox(
    "Semester",
    ["F", "S"]
)

relation = st.selectbox(
    "Relation",
    ["Father", "Mum"]
)

raised_hand = st.slider(
    "Raised Hands",
    0,
    100,
    50
)

visited_resources = st.slider(
    "Visited Resources",
    0,
    100,
    50
)

announcements_view = st.slider(
    "Announcements Viewed",
    0,
    100,
    50
)

discussion = st.slider(
    "Discussion",
    0,
    100,
    50
)

parent_answer = st.selectbox(
    "Parent Answer",
    ["Yes", "No"]
)

parent_satisfaction = st.selectbox(
    "Parent Satisfaction",
    ["Good", "Bad"]
)

absences = st.number_input(
    "Absences",
    min_value=0,
    max_value=100,
    value=5
)


# Prediction button
if st.button("🔮 Predict Performance"):

    input_data = pd.DataFrame({
        "gender": [gender],
        "NationalITy": [nationality],
        "PlaceofBirth": [place_of_birth],
        "StageID": [stage_id],
        "GradeID": [grade_id],
        "SectionID": [section_id],
        "Topic": [topic],
        "Semester": [semester],
        "Relation": [relation],
        "raisedhands": [raised_hand],
        "VisITedResources": [visited_resources],
        "AnnouncementsView": [announcements_view],
        "Discussion": [discussion],
        "ParentAnsweringSurvey": [parent_answer],
        "ParentschoolSatisfaction": [parent_satisfaction],
        "StudentAbsenceDays": [
            "Under-7-Days" if absences < 7 else "Above-7-Days"
        ]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"🎯 Predicted Student Performance: {prediction}")

    if prediction == "H":
        st.balloons()
        st.success("🌟 High Performance")

    elif prediction == "M":
        st.info("👍 Medium Performance")

    else:
        st.warning("📚 Low Performance")