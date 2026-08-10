import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Load dataset
data = pd.read_csv("data/student_data.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", data.shape)


# Remove unnecessary spaces from column names
data.columns = data.columns.str.strip()


# Target column
target = "Class"

# Separate features and target
X = data.drop(columns=[target])
y = data[target]


# Identify categorical and numerical columns
categorical_columns = X.select_dtypes(include=["object"]).columns.tolist()
numerical_columns = X.select_dtypes(exclude=["object"]).columns.tolist()


# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        )
    ],
    remainder="passthrough"
)


# Machine Learning model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Complete pipeline
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Train model
pipeline.fit(X_train, y_train)


# Predictions
y_pred = pipeline.predict(X_test)


# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("--------------------------------")
print("Student Performance Prediction")
print("--------------------------------")
print("Model Training Completed!")
print("Accuracy:", accuracy)


# Create model folder
os.makedirs("model", exist_ok=True)


# Save model
with open("model/student_model.pkl", "wb") as file:
    pickle.dump(pipeline, file)


print("Model saved successfully!")
print("Saved at: model/student_model.pkl")