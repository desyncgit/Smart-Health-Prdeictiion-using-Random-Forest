import streamlit as st
import joblib
import pandas as pd
import time
import base64

# loading model and list of symptoms
model = joblib.load(r"C:\Users\d3cip\OneDrive\Documents\MinorProject\saved_model\random_f.joblib")
symptoms_list = [
    'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills',
    'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting',
    'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety',
    'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat',
    'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating',
    'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite',
    'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever',
    'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
    'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
    'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
    'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
    'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
    'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
    'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
    'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
    'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
    'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
    'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
    'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
    'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria',
    'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances',
    'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding',
    'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum',
    'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads',
    'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails',
    'blister', 'red_sore_around_nose', 'yellow_crust_ooze'
]


# Set the background image using st.image
background_image_path = "C:/Users/d3cip/Downloads/image_medi.jpg"
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/jpeg;base64,{base64.b64encode(open(background_image_path, "rb").read()).decode()});
        background-size: cover;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        color: #ecf0f1;
        font-family: 'Arial', sans-serif;
    }}

    h1, h2 {{
        color: #2ecc71; /* Green color */
        animation: pulse 2s infinite;
    }}

    .stTextInput {{
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 8px;
        padding: 0.5rem;
        margin: 0.5rem 0;
    }}

    .stMultiselect label {{
        color: #ecf0f1;
    }}

    .stButton {{
        background-color: #3498db;
        color: #fff;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        margin-top: 1rem;
        transition: transform 0.3s ease-in-out;
    }}

    .stButton:hover {{
        background-color: #2980b9;
        transform: scale(1.1);
    }}

    @keyframes pulse {{
        0% {{
            transform: scale(1);
        }}
        50% {{
            transform: scale(1.05);
        }}
        100% {{
            transform: scale(1);
        }}
    }}

    .pulse {{
        animation: pulse 2s infinite;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# start of streamlit UI
st.title("Medi+ - The Smart Healthcare Assistor")
st.header("Please enter your symptoms 🩺")

symptoms = st.multiselect('Enter your symptoms so that we can get you a primary diagnosis:', [*symptoms_list], key='symptoms')

# creating dataframe for accepting testing values
prediction_value = [0 for i in range(131)]  # Adjusted to 131
for sym in symptoms:
    index = symptoms_list.index(sym)
    # assigning encoded value to testing frame
    prediction_value[index] = 1

# convert list to Pandas dataframe and transpose it for model evaluation
query = pd.DataFrame(prediction_value).T
prediction = model.predict(query)

# evaluation and confirmation
if st.button("Evaluate"):
    with st.spinner('Predicting output...'):
        time.sleep(1)
        if symptoms:
            st.success("Prediction complete!")
            st.write("The diagnosis we have reached is: ")
            st.error(*prediction)
            st.write("Please consult your nearest health administrator soon, take care! 🏥")

        else:
            st.info("Please enter at least one symptom before clicking evaluate!")




