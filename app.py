import streamlit as st
import pandas as pd
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import os





names=["naman","kapil","john"]
username=["naman","kaps","john"]

file_path = Path(__file__).parent/"hashed_pw.pkl"
with file_path.open("rb") as file:
    password=pickle.load(file)

authenticator=stauth.Authenticate(names,username,password,"med","abc")
name,authentication_status,usernames = authenticator.login("Login","main")

if authentication_status ==False:
    st.error("please enter correct credentials")
if authentication_status==None:
    st.warning("please enter the credentials")
if authentication_status :

    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_dir, "Heart_Model.sav")

    heart_model = pickle.load(open(model_path, 'rb'))
    liver_model = pickle.load(open("liver.sav", 'rb'))
    diabetes_model = pickle.load(open("Diabetes_Model.sav", 'rb'))

    def show_index_page():

        st.title('Diabetes')
        st.image("image/diabetes.png", use_column_width=True)
        st.markdown('Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. Blood glucose is your main source of energy and comes from the food you eat. Insulin, a hormone made by the pancreas, helps glucose from food get into your cells to be used for energy.')

        st.header('What health problems can people with diabetes develop?')
        st.markdown('Over time, high blood glucose leads to problems such as:')
        st.markdown('- Heart disease')
        st.markdown('- Stroke')
        st.markdown('- Kidney disease')
        st.markdown('- Eye problems')
        st.markdown('- Dental disease')
        st.markdown('- Nerve damage')
        st.markdown('- Foot problems')

        st.header('How to manage diabetes?')
        st.markdown('To manage diabetes effectively, individuals can:')
        st.markdown('- Maintain a healthy diet')
        st.markdown('- Engage in regular physical activity')
        st.markdown('- Monitor blood glucose levels regularly')
        st.markdown('- Take prescribed medications as directed by healthcare providers')

        
        st.markdown('---')

        # Heart Disease section
        st.title('Heart Disease 🩺')
        st.image("image/heart.png", use_column_width=True)
        st.header('Overview')
        st.markdown('Heart disease describes a range of conditions that affect your heart. Diseases under the heart disease umbrella include blood vessel diseases, such as coronary artery disease; heart rhythm problems (arrhythmias); and heart defects you\'re born with (congenital heart defects), among others.')
        st.markdown('The term "heart disease" is often used interchangeably with the term "cardiovascular disease." Cardiovascular disease generally refers to conditions that involve narrowed or blocked blood vessels that can lead to a heart attack, chest pain (angina) or stroke. Other heart conditions, such as those that affect your heart\'s muscle, valves or rhythm, also are considered forms of heart disease.')
        st.markdown('Many forms of heart disease can be prevented or treated with healthy lifestyle choices.')

        st.header('Symptoms')
        st.markdown('Common symptoms of heart disease include:')
        st.markdown('- Chest pain, chest tightness, chest pressure and chest discomfort (angina)')
        st.markdown('- Shortness of breath')
        st.markdown('- Pain, numbness, weakness or coldness in your legs or arms if the blood vessels in those parts of your body are narrowed')
        st.markdown('- Pain in the neck, jaw, throat, upper abdomen or back')

        st.header('Prevention')
        st.markdown('To prevent heart disease, individuals can:')
        st.markdown('- Maintain a healthy diet low in saturated fats, cholesterol, and sodium')
        st.markdown('- Engage in regular physical activity')
        st.markdown('- Avoid smoking and limit alcohol consumption')
        st.markdown('- Manage stress effectively')

        st.markdown('---')

        st.title("Liver Disease Prediction")
        st.image("image/liver.png", use_column_width=True)
        st.markdown(
            "Liver disease refers to any condition that causes liver inflammation or damage, "
            "which may impair liver function and lead to serious complications. "
            "Liver disease can be inherited (genetic) or caused by a variety of factors that damage the liver, "
            "such as viruses and alcohol use. "
            "Obesity is also associated with liver damage. "
            "Over time, damage to the liver results in scarring (cirrhosis), "
            "which can lead to liver failure, a life-threatening condition."
        )

        st.header("Symptoms of Liver Disease")
        st.markdown(
            "- Jaundice (yellowing of the skin and eyes)\n"
            "- Abdominal pain and swelling\n"
            "- Swelling in the legs and ankles\n"
            "- Itchy skin\n"
            "- Dark urine color\n"
            "- Pale stool color\n"
            "- Chronic fatigue\n"
            "- Nausea or vomiting\n"
            "- Loss of appetite\n"
            "- Easy bruising\n"
            "- Weight loss\n"
            "- Weakness\n"
            "- Confusion, disorientation or trouble concentrating"
        )

        st.header("Prevention of Liver Disease")
        st.markdown(
            "- Limit alcohol consumption\n"
            "- Avoid risky behavior\n"
            "- Get vaccinated\n"
            "- Use medications wisely\n"
            "- Avoid contact with other people's blood and body fluids\n"
            "- Take care with aerosol sprays\n"
            "- Protect your skin\n"
            "- Maintain a healthy weight\n"
            "- Eat a healthy diet\n"
            "- Exercise regularly\n"
            "- Avoid toxins"
        )

        st.markdown("---")

        
        
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
    def get_liver_user_inputs():
        st.subheader('Liver Disease - User Input Features')
        age = st.number_input('Age', min_value=10, max_value=100, value=40)
        gender = st.radio('Gender', ['Male', 'Female'])
        total_bilirubin = st.number_input('Total Bilirubin', min_value=0.0, max_value=30.0, value=5.0)
        direct_bilirubin = st.number_input('Direct Bilirubin', min_value=0.0, max_value=20.0, value=2.0)
        alkphos_alkaline_phosphotase = st.number_input('Alkphos Alkaline Phosphotase', min_value=0, max_value=2000, value=150)
        sgpt_alamine_aminotransferase = st.number_input('Sgpt Alamine Aminotransferase', min_value=0, max_value=2000, value=100)
        sgot_aspartate_aminotransferase = st.number_input('Sgot Aspartate Aminotransferase', min_value=0, max_value=2000, value=100)
        total_proteins = st.number_input('Total Proteins', min_value=0.0, max_value=10.0, value=6.0)
        alb_albumin = st.number_input('ALB Albumin', min_value=0.0, max_value=10.0, value=3.0)
        ag_ratio_albumin_and_globulin_ratio = st.number_input('A/G Ratio Albumin and Globulin Ratio', min_value=0.0, max_value=10.0, value=1.0)

        # Encoding gender
        gender_mapping = {'Male': 1, 'Female': 0}

        # Create DataFrame with user inputs
        user_inputs = pd.DataFrame({
            'Age': [age],
            'Gender': [gender_mapping[gender]],
            'Total_Bilirubin': [total_bilirubin],
            'Direct_Bilirubin': [direct_bilirubin],
            'Alkaline_Phosphotase': [alkphos_alkaline_phosphotase],
            'Alamine_Aminotransferase': [sgpt_alamine_aminotransferase],
            'Aspartate_Aminotransferase': [sgot_aspartate_aminotransferase],
            'Total_Protiens': [total_proteins],
            'Albumin': [alb_albumin],
            'Albumin_and_Globulin_Ratio': [ag_ratio_albumin_and_globulin_ratio]
        })
        return user_inputs
    # Function to take user inputs for diabetes prediction
    def predict_liver_disease(user_inputs):
            liver_prediction = liver_model.predict(user_inputs)[0]
            if liver_prediction == 0:
                st.write('Person does not have liver disease.')
            else:
                st.write('Person has high chances of liver disease')
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
    
    authenticator.logout("logout","sidebar")
            
    
    st.sidebar.title(f"Welcome {name}")
    # Sidebar tabs for heart disease and diabetes
    selected_tab = st.sidebar.selectbox('Select prediction type:', ('Home','Heart Disease', 'Diabetes',"Liver disease"))
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
    elif selected_tab== 'Diabetes':
        st.header('Diabetes Prediction')
        user_input = get_diabetes_user_inputs()
        st.write(user_input)
        if st.button('Predict Diabetes'):
            diabetes_prediction = diabetes_model.predict(user_input)[0]
            if diabetes_prediction == 0:
                st.write('Person does not have diabetes.')
            else:
                st.write('Person has high chances of diabetes')
    elif selected_tab=="Liver disease":
        st.header('Liver Disease Prediction')
        user_input = get_liver_user_inputs()
        st.write(user_input)
        if st.button('Predict Liver Disease'):
            predict_liver_disease(user_input)
        
    
    
    else:
        show_index_page()
