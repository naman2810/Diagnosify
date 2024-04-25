import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
import pickle

# Load the trained models
random_forest_model = pickle.load(open("/Users/namanranka/Desktop/diagnosify/Models/Random_Forest_Model.sav", 'rb'))
#mlp_model = pickle.load(open('MLP_Model.sav', 'rb'))

# Function to take user inputs
# Function to take user inputs
def get_user_inputs():
    st.subheader('User Input Features')
    age = st.number_input('Age', min_value=20, max_value=100, value=40)
    sex = st.radio('Sex', ['Male', 'Female'])
    cp = st.radio('Chest Pain Type (cp)', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
    trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=90, max_value=200, value=120)
    chol = st.number_input('Cholesterol (mg/dl)', min_value=100, max_value=600, value=200)
    fbs = st.radio('Fasting Blood Sugar > 120 mg/dl (fbs)', ['Yes', 'No'])
    restecg = st.radio('Resting Electrocardiographic Results (restecg)', ['Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'])
    thalach = st.number_input('Maximum Heart Rate Achieved (bpm)', min_value=60, max_value=220, value=150)
    exang = st.radio('Exercise Induced Angina (exang)', ['Yes', 'No'])
    oldpeak = st.number_input('ST Depression Induced by Exercise Relative to Rest', min_value=0.0, max_value=6.2, value=1.0)
    slope = st.radio('Slope of the Peak Exercise ST Segment (slope)', ['Upsloping', 'Flat', 'Downsloping'])
    ca = st.number_input('Number of Major Vessels Colored by Flourosopy', min_value=0, max_value=4, value=1)
    thal = st.radio('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])

    # Encoding categorical features
    sex_mapping = {'Male': 1, 'Female': 0}
    cp_mapping = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3}
    fbs_mapping = {'Yes': 1, 'No': 0}
    restecg_mapping = {'Normal': 0, 'ST-T Wave Abnormality': 1, 'Left Ventricular Hypertrophy': 2}
    exang_mapping = {'Yes': 1, 'No': 0}
    slope_mapping = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
    thal_mapping = {'Normal': 1, 'Fixed Defect': 2, 'Reversible Defect': 3}

    # Create DataFrame with user inputs
    user_inputs = pd.DataFrame({'age': [age],
                                'sex': [sex_mapping[sex]],
                                'cp': [cp_mapping[cp]],
                                'trestbps': [trestbps],
                                'chol': [chol],
                                'fbs': [fbs_mapping[fbs]],
                                'restecg': [restecg_mapping[restecg]],
                                'thalach': [thalach],
                                'exang': [exang_mapping[exang]],
                                'oldpeak': [oldpeak],
                                'slope': [slope_mapping[slope]],
                                'ca': [ca],
                                'thal': [thal_mapping[thal]]})
    return user_inputs


# Title and description
st.title('Heart Disease Prediction')
st.write('This app predicts the likelihood of heart disease based on user input features.')

# User inputs

user_input = get_user_inputs()
st.write(user_input)

# Prediction
st.header('Prediction')
if st.button('Predict'):
    rf_prediction = random_forest_model.predict(user_input)[0]
    if rf_prediction == 0:
        st.write('Person does not have heart disease.')
    else:
        st.write('Person has high chances of heart disease')
