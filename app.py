import streamlit as st
import pandas as pd
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import os





names=["naman","kapil"]
username=["naman","kaps"]

file_path = Path(__file__).parent/"hashed_pw.pkl"
with file_path.open("rb") as file:
    password=pickle.load(file)

authenticator=stauth.Authenticate(names,username,password,"med","abc",cookie_expiry_days=1)

name,authentication_status,usernames = authenticator.login("Login","main")

if authentication_status ==False:
    st.error("please enter correct credentials")
if authentication_status==None:
    st.warning("please enter the credentials")
if authentication_status :

    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_dir, "Heart_Model.sav")

    heart_model = pickle.load(open(model_path, 'rb'))
    
    diabetes_model = pickle.load(open("Diabetes_Model.sav", 'rb'))

    # Function to take user inputs for heart disease prediction
    def get_heart_user_inputs():
        st.subheader('Heart Disease - User Input Features')
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

    # Function to take user inputs for diabetes prediction
    def get_diabetes_user_inputs():
        st.subheader('Diabetes - User Input Features')
        preg = st.number_input('Pregnancies', min_value=0, max_value=17, value=3)
        glucose = st.number_input('Glucose', min_value=0, max_value=199, value=117)
        bp = st.number_input('Blood Pressure (mm Hg)', min_value=0, max_value=122, value=72)
        skin_thickness = st.number_input('Skin Thickness (mm)', min_value=0, max_value=99, value=23)
        insulin = st.number_input('Insulin (mu U/ml)', min_value=0, max_value=846, value=30)
        bmi = st.number_input('BMI', min_value=0.0, max_value=67.1, value=32.0)
        dpf = st.number_input('Diabetes Pedigree Function', min_value=0.078, max_value=2.42, value=0.3725)
        age = st.number_input('Age', min_value=21, max_value=81, value=29)

        # Create DataFrame with user inputs
        user_inputs = pd.DataFrame({'Pregnancies': [preg],
                                    'Glucose': [glucose],
                                    'BloodPressure': [bp],
                                    'SkinThickness': [skin_thickness],
                                    'Insulin': [insulin],
                                    'BMI': [bmi],
                                    'DiabetesPedigreeFunction': [dpf],
                                    'Age': [age]})
        return user_inputs

    # Title and description
    st.title('Health Prediction')

    try:
        authenticator.logout("Logout","sidebar")
    except KeyError:
        st.warning("The logout cookie does not exist.")
    st.sidebar.title(f"Welcome {name}")
    # Sidebar tabs for heart disease and diabetes
    selected_tab = st.sidebar.selectbox('Select prediction type:', ('Heart Disease', 'Diabetes'))
    # Prediction based on selected tab
    if selected_tab == 'Heart Disease':
        st.header('Heart Disease Prediction')
        user_input = get_heart_user_inputs()
        st.write(user_input)
        if st.button('Predict Heart Disease'):
            heart_prediction = heart_model.predict(user_input)[0]
            if heart_prediction == 0:
                st.write('Person does not have heart disease.')
            else:
                st.write('Person has high chances of heart disease')
    else:
        st.header('Diabetes Prediction')
        user_input = get_diabetes_user_inputs()
        st.write(user_input)
        if st.button('Predict Diabetes'):
            diabetes_prediction = diabetes_model.predict(user_input)[0]
            if diabetes_prediction == 0:
                st.write('Person does not have diabetes.')
            else:
                st.write('Person has high chances of diabetes')
