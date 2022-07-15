import streamlit as st
import pickle
import pandas as pd


st.set_page_config(page_title="Predict", page_icon="📈")

@st.cache
def load_model():
    with open('model/diabetes_model.pkl', 'rb') as file:
        data = pickle.load(file)

    return data


model = load_model()

st.title("Simple Diabetes Prediction")
    
st.write("""### We need some Data to Predict whether you have Diabetes or not""")
st.write("""##### This model has only about 70% accuracy since it was trained with a small dataset""")


pregnancies = st.number_input('Pregnancies', min_value=0)
glucose = st.number_input('Glucose', min_value=0)
bloodPressure = st.number_input('BloodPressure', min_value=0)
skinThickness = st.number_input('Skin Thickness', min_value=0)
insulin = st.number_input('Insulin', min_value=0)
bmi = st.slider('BMI', 0.0, 100.0, 0.01)
diabetesPedigreeFunction = st.slider('Diabetes Pedigree Function', 0.00, 1.00, 0.01)
age = st.slider("Age", 5, 100, 20)


data = {'Pregnancies': pregnancies, 'Glucose': glucose, 'BloodPressure': bloodPressure, 'SkinThickness': skinThickness,
        'Insulin': insulin, 'BMI': bmi, 'DiabetesPedigreeFunction': diabetesPedigreeFunction, 'Age': age}

df = pd.DataFrame(data, index=[0])

# Submit button
submitted = st.button("Predict my Diagnosis")

if submitted:
    predict = model.predict(df)

    if (predict[0] == 1):
        st.write("""#### 🎉Congratulations you are not diabetic🎉 """)
        st.balloons()
    else:
        st.write("""#### I'm afraid you are diabetic 😔""")
        st.snow()