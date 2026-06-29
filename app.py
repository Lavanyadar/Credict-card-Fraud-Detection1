import streamlit as st
import numpy as np
import tensorflow as tf

# Load model
model = tf.keras.models.load_model("model.keras")

st.set_page_config(
    page_title="Fraud Detection",
    page_icon="💳"
)

st.title("💳 Credit Card Fraud Detection")

st.write("Enter 32 feature values:")

features = []

for i in range(32):
    value = st.number_input(
        f"Feature {i+1}",
        value=0.0,
        format="%.6f"
    )
    features.append(value)

if st.button("Predict"):

    input_data = np.array([features], dtype=np.float32)

    prediction = model.predict(input_data, verbose=0)

    probability = float(prediction[0][0])

    st.subheader("Prediction Result")
    st.write(f"Fraud Probability: {probability:.4f}")

    if probability >= 0.5:
        st.error("⚠️ Fraudulent Transaction")
    else:
        st.success("✅ Legitimate Transaction")
        