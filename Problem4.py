import streamlit as st
from sklearn.ensemble import RandomForestClassifier

def main()
    st.title("Wine Quality Prediction")
    Fixed_Acidity = st.slider('Fixed Acidity', min_value=4.6, max_value=14.2, value=6)
    volatile_acidity = st.slider('Volatile Acidity', min_value=0.12, max_value=1.10, value=0.5)
    citric_acid = st.slider('Citric Acid', min_value=0, max_value=1.0, value=0.3)
    residual_sugar = st.slider('Residual Sugar', min_value=0.9, max_value= 15.5, value=6)
    chlorides = st.slider('chlorides', min_value=0.12, max_value=0.346, value=0.045)
    f_SO2 = st.slider('Free SO2', min_value=2, max_value=72, value=35)
    t_SO2 = st.slider('Total SO2', min_value=9, max_value=289, value=138)
    density = st.slider('Density', min_value=0.99,max_value= 1.036, value=0.995)
    pH = st.slider('pH', min_value=2.74, max_value=3.82, value=3.18)
    sulphates = st.sider('Sulphates', min_value=0.33, max_value=1.08, value=0.65)
    alcohol = st.slider('Alcohol', min_value=8.4, max_value=14.2, value=10.42)

def predicted_rf()
    
    r_rf_classifier= RandomForestClassifier(n_estimators= 1000, criterion="entropy") 
    r_rf_classifier.fit(r_x_train, r_y_train)
    # refereed scikit-learn documentation

