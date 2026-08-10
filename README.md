# 🎓 Student Performance Prediction

## 📌 About the Project

Student Performance Prediction is a Machine Learning project that predicts a student's academic performance based on educational, behavioral, and demographic information.

The project uses the **xAPI-Edu-Data** dataset and a **Random Forest Classifier** to classify students into High, Medium, or Low performance categories.

## 🚀 Features

- 🎓 Student performance prediction
- 🤖 Machine Learning classification
- 🌲 Random Forest Classifier
- 🎯 High, Medium, and Low performance prediction
- 🌐 Interactive Streamlit web application
- 📊 Model accuracy evaluation

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Pickle
- VS Code

## 🧠 Machine Learning Model

**Algorithm:** Random Forest Classifier

**Accuracy:** 79.17%

The model predicts:

- 🟢 H → High Performance
- 🟡 M → Medium Performance
- 🔴 L → Low Performance

## 📊 Dataset

This project uses the **xAPI-Edu-Data** student academic performance dataset.

The dataset contains information such as:

- Gender
- Nationality
- Place of Birth
- Stage
- Grade
- Section
- Topic
- Semester
- Raised Hands
- Visited Resources
- Announcements Viewed
- Discussion
- Parent Answer
- Parent Satisfaction
- Student Absence Days

## 📂 Project Structure

```text
STUDENT_PERFORMANCE_PREDICTION/
│
├── data/
│   └── student_data.csv
│
├── model/
│   └── student_model.pkl
│
├── app.py
├── train.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## ▶️ Train the Model

Run the following command:

```bash
python train.py
```

The trained model will be saved as:

```text
model/student_model.pkl
```

## 🌐 Run the Web Application

Run:

```bash
python -m streamlit run app.py
```

The Student Performance Prediction web application will open in your browser.

## 🎯 Example Prediction

The application takes student information as input and predicts the student's performance.

Example:

```text
Predicted Student Performance: M

Medium Performance
```

## 📈 Results

The Random Forest Classifier achieved approximately **79.17% accuracy** on the test data.

## 👩‍💻 Author

**Iqra Razzaq**

Machine Learning & AI Enthusiast

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Create a Pull Request

## ⭐ Support

If you find this project useful, please give it a ⭐ star on GitHub.

---

### 🎓 Student Performance Prediction

**Built with Python, Machine Learning & Streamlit**