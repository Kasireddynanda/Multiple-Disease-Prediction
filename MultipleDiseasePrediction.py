import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set Streamlit page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")
st.markdown(
    """
    <style>
    /* Background Gradient */
    body {
        background: linear-gradient(to right, #141E30, #243B55);
        color: white;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #1E1E2E;
        color: white;
    }

    /* Headings */
    h1, h2, h3, h4 {
        color: #00C9A7;
    }

    /* Buttons */
    .stButton>button {
        background-color: #00C9A7;
        color: white;
        font-size: 16px;
        padding: 8px;
        border-radius: 8px;
        transition: 0.3s ease-in-out;
    }

    .stButton>button:hover {
        background-color: #009688;
        transform: scale(1.05);
    }

    /* Input Fields */
    input {
        border-radius: 5px;
        padding: 8px;
    }
    
    /* Make it Fullscreen */
    [data-testid="stAppViewContainer"] {
        max-width: 100%;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

# Get the working directory of the script
working_dir = os.path.dirname(os.path.abspath(__file__))

# Define model paths
model_paths = {
    "diabetes": os.path.join(working_dir, "saved models", "diabetes_model.sav"),
    "heart": os.path.join(working_dir, "saved models", "heart_disease_model.sav"),
    "parkinsons": os.path.join(working_dir, "saved models", "parkinsons_model.sav"),
    "dementia": os.path.join(working_dir, "saved models", "dementia_model.sav"),
    "breast_cancer": os.path.join(working_dir, "saved models", "breast_cancer_model.sav"),
    "dry_eye": os.path.join(working_dir, "saved models", "DryEye_model.sav"),
    "obesity": os.path.join(working_dir, "saved models", "obesity_model.sav"),
    "kidney": os.path.join(working_dir, "saved models", "kidney_model.sav"),
}

# Load models safely
models = {}
for name, path in model_paths.items():
    try:
        models[name] = pickle.load(open(path, "rb"))
    except FileNotFoundError:
        st.error(f"Error: Model '{name}' not found! Check file paths.")
        st.stop()

# Sidebar navigation


# Sidebar with Nested Menu
with st.sidebar:
    main_selection = option_menu(
        "Multiple Disease Prediction System",
        ["Chronic Diseases", "Infectious Diseases","Neurological Disorders", "Cancer Diseases","Respiratory Diseases", "Mental Health Disorders"],
        menu_icon="hospital-fill",
        icons=["stethoscope", "plus-circle"],
        default_index=0,
    )

    if main_selection == "Chronic Diseases":
        chronic_selection = option_menu(
            "Chronic Diseases",
            ["Diabetes Prediction", "Heart Disease Prediction",
             "Obesity Prediction", "Kidney Prediction"],
            menu_icon="clipboard-heart",
            icons=['activity', 'heart', 'person', 'brain', 'droplet', 'eye', 'hand', 'kidney'],
            default_index=0,
            styles={
                "container": {"padding": "5px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px"},
                "nav-link-selected": {"background-color": "#007BFF", "color": "white"},  # Blue Selection Color
            }
        )
    if main_selection == "Infectious Diseases":
            chronic_selection = option_menu(
                "Infectious Diseases",
              ["Flu Prediction", "COVID-19 Prediction"],
                menu_icon="clipboard-heart",
                icons=['activity', 'heart', 'person', 'brain', 'droplet', 'eye', 'hand', 'kidney'],
                default_index=0,
                styles={
                    "container": {"padding": "5px"},
                    "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px"},
                    "nav-link-selected": {"background-color": "#007BFF", "color": "white"},  # Blue Selection Color
                }
            )
    if main_selection == "Neurological Disorders":
                chronic_selection = option_menu(
                    "Neurological Disorders",
                    ["Parkinsons Prediction",
                     "Dementia Prediction",],
                    menu_icon="clipboard-heart",
                    icons=['activity', 'heart', 'person', 'brain', 'droplet', 'eye', 'hand', 'kidney'],
                    default_index=0,
                    styles={
                        "container": {"padding": "5px"},
                        "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px"},
                        "nav-link-selected": {"background-color": "#007BFF", "color": "white"},  # Blue Selection Color
                    }
                )
    if main_selection == "Cancer Diseases":
             chronic_selection = option_menu(
                 "Cancer Diseases",
                 [ "Breast Cancer Prediction",],
                 menu_icon="clipboard-heart",
                 icons=['activity', 'heart', 'person', 'brain', 'droplet', 'eye', 'hand', 'kidney'],
                 default_index=0,
                 styles={
                     "container": {"padding": "5px"},
                     "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px"},
                     "nav-link-selected": {"background-color": "#007BFF", "color": "white"},  # Blue Selection Color
                 }
             )
                  
    if main_selection == "Respiratory Diseases":
             chronic_selection = option_menu(
                 "Respiratory Diseases",
                 ["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction",
                  "Dementia Prediction", "Breast Cancer Prediction", "Dry Eye Prediction",
                  "Obesity Prediction", "Kidney Prediction"],
                 menu_icon="clipboard-heart",
                 icons=['activity', 'heart', 'person', 'brain', 'droplet', 'eye', 'hand', 'kidney'],
                 default_index=0,
                 styles={
                     "container": {"padding": "5px"},
                     "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px"},
                     "nav-link-selected": {"background-color": "#007BFF", "color": "white"},  # Blue Selection Color
                 }
             )
    if main_selection == "Mental Health Disorders":
              chronic_selection = option_menu(
                  "Mental Health Disorders",
                  ["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction",
                   "Dementia Prediction", "Breast Cancer Prediction", "Dry Eye Prediction",
                   "Obesity Prediction", "Kidney Prediction"],
                  menu_icon="clipboard-heart",
                  icons=['activity', 'heart', 'person', 'brain', 'droplet', 'eye', 'hand', 'kidney'],
                  default_index=0,
                  styles={
                      "container": {"padding": "5px"},
                      "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px"},
                      "nav-link-selected": {"background-color": "#007BFF", "color": "white"},  # Blue Selection Color
                  }
              )
                

    elif main_selection == "Other Diseases":
        other_selection = option_menu(
            "Other Diseases",
            ["Flu Prediction", "COVID-19 Prediction"],
            menu_icon="virus",
            icons=['thermometer', 'shield-virus'],
            default_index=0,
            styles={
                "container": {"padding": "5px"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px"},
                "nav-link-selected": {"background-color": "#28A745", "color": "white"},  # Green Selection Color
            }
        )


# Function to validate and convert inputs
def validate_inputs(inputs):
    try:
        # Convert inputs to float, handling both strings and numbers
        validated_inputs = []
        for x in inputs:
            if isinstance(x, str):  # If the input is a string
                validated_inputs.append(float(x.strip()) if x.strip() else 0.0)
            else:  # If the input is already a number (e.g., int or float)
                validated_inputs.append(float(x))
        return validated_inputs
    except ValueError:
        st.error("Invalid input! Please enter numeric values only.")
        return None

### Diabetes Prediction
if chronic_selection == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        SkinThickness = st.text_input('Skin Thickness value')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Glucose = st.text_input('Glucose Level')
        Insulin = st.text_input('Insulin Level')
        Age = st.text_input('Age')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        BMI = st.text_input('BMI value')

    if st.button('Diabetes Test Result'):
        user_input = validate_inputs([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        if user_input:
            diab_prediction = models["diabetes"].predict([user_input])
            st.success('The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic')

### Heart Disease Prediction
if chronic_selection == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
        trestbps = st.text_input('Resting Blood Pressure')
        thalach = st.text_input('Maximum Heart Rate')

    with col2:
        sex = st.radio("Sex", [0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
        chol = st.text_input('Serum Cholesterol (mg/dl)')
        exang = st.radio("Exercise Induced Angina", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

    with col3:
        cp = st.text_input('Chest Pain Type')
        fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        oldpeak = st.text_input('ST Depression')

    if st.button('Heart Disease Test Result'):
        user_input = validate_inputs([age, sex, cp, trestbps, chol, fbs, thalach, exang, oldpeak])
        if user_input:
            heart_prediction = models["heart"].predict([user_input])
            st.success('The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease')

### Parkinson’s Prediction
if chronic_selection == 'Parkinsons Prediction':
    st.title('Parkinson’s Disease Prediction using ML')

    features = [
        'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)',
        'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)',
        'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR',
        'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
    ]
    
    user_inputs = [st.text_input(label) for label in features]

    if st.button('Parkinson’s Test Result'):
        user_input = validate_inputs(user_inputs)
        if user_input:
            parkinson_prediction = models["parkinsons"].predict([user_input])
            st.success('The person has Parkinson’s' if parkinson_prediction[0] == 1 else 'The person does not have Parkinson’s')

### Dementia Prediction
if chronic_selection == 'Dementia Prediction':
    st.title('Dementia Prediction using ML')

    features = [
        'Gender', 'Age', 'EDUC', 'Socioeconomic Status', 'Mini-Mental State Examination',
        'Clinical Dementia Rating', 'Estimated Total Intracranial Volume', 'Normalized Whole Brain Volume',
        'Atlas Scaling Factor'
    ]

    user_inputs = [st.text_input(label) for label in features]

    if st.button('Dementia Test Result'):
        user_input = validate_inputs(user_inputs)
        if user_input:
            dementia_prediction = models["dementia"].predict([user_input])
            st.success('The person has Dementia' if dementia_prediction[0] == 1 else 'The person does not have Dementia')

### Breast Cancer Prediction
if chronic_selection == 'Breast Cancer Prediction':
    st.title('Breast Cancer Prediction using ML')

    features = [
        'Radius_mean', 'Texture_mean', 'Perimeter_mean', 'Area_mean', 'Smoothness_mean', 
        'Compactness_mean', 'Concavity_mean', 'Concave points_mean', 'Symmetry_mean', 'Fractal_dimension_mean'
    ]

    user_inputs = [st.text_input(label) for label in features]

    if st.button('Breast Cancer Test Result'):
        user_input = validate_inputs(user_inputs)
        if user_input:
            cancer_prediction = models["breast_cancer"].predict([user_input])
            st.success('The person has Breast Cancer' if cancer_prediction[0] == 1 else 'The person does not have Breast Cancer')

### Dry Eye Prediction
if chronic_selection == 'Dry Eye Prediction':
    st.title('Dry Eye Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.radio("Gender", [0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
        age = st.text_input('Age')
        sleep_duration = st.text_input('Sleep Duration')
        sleep_quality = st.text_input('Sleep Quality')
        stress_level = st.text_input('Stress Level')

    with col2:
        heart_rate = st.text_input('Heart Rate')
        daily_steps = st.text_input('Daily Steps')
        physical_activity = st.text_input('Physical Activity')
        height = st.text_input('Height')
        weight = st.slider('Weight', 0, 150)

    with col3:
        sleep_disorder = st.text_input('Sleep Disorder')
        wake_up_during_night = st.text_input('Wake Up During Night')
        feel_sleepy_during_day = st.text_input('Feel Sleepy During Day')
        caffeine_consumption = st.text_input('Caffeine Consumption')
        alcohol_consumption = st.text_input('Alcohol Consumption')

    if st.button('Dry Eye Test Result'):
        user_input = validate_inputs([gender, age, sleep_duration, sleep_quality, stress_level, heart_rate, daily_steps, physical_activity, height, weight, sleep_disorder, wake_up_during_night, feel_sleepy_during_day, caffeine_consumption, alcohol_consumption])
        if user_input:
            dryeye_prediction = models["dry_eye"].predict([user_input])
            st.success('The person has Dry Eye' if dryeye_prediction[0] == 1 else 'The person does not have Dry Eye')

### Obesity Prediction
if chronic_selection == 'Obesity Prediction':
    st.title('Obesity Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
        gender = st.radio("Gender", [0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
        height = st.text_input('Height')

    with col2:
        weight = st.slider('Weight', 0, 150)
        bmi = st.text_input('BMI')
        physical_activity_level = st.text_input('Physical Activity Level')

    if st.button('Obesity Test Result'):
        user_input = validate_inputs([age, gender, height, weight, bmi, physical_activity_level])
        if user_input:
            obesity_prediction = models["obesity"].predict([user_input])
            st.success('The person is Obese' if obesity_prediction[0] == 1 else 'The person is not obese')

### Kidney Prediction
if chronic_selection == 'Kidney Prediction':
    st.title('Kidney Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
        gender = st.radio("Gender", [0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
        bmi = st.text_input('BMI')
        smoking = st.text_input('Smoking')

    with col2:
        alcohol_consumption = st.text_input('Alcohol Consumption')
        physical_activity = st.text_input('Physical Activity')
        diet_quality = st.text_input('Diet Quality')
        sleep_quality = st.text_input('Sleep Quality')

    with col3:
        urinary_tract_infections = st.text_input('Urinary Tract Infections')
        systolic_bp = st.text_input('Systolic BP')
        diastolic_bp = st.text_input('Diastolic BP')
        fasting_blood_sugar = st.text_input('Fasting Blood Sugar')

    if st.button('Kidney Test Result'):
        user_input = validate_inputs([age, gender, bmi, smoking, alcohol_consumption, physical_activity, diet_quality, sleep_quality, urinary_tract_infections, systolic_bp, diastolic_bp, fasting_blood_sugar])
        if user_input:
            kidney_prediction = models["kidney"].predict([user_input])
            st.success('The person has Chronic Kidney disease' if kidney_prediction[0] == 1 else 'The person does not have Chronic Kidney disease')