import streamlit as st
import pandas as pd
import joblib  


model = joblib.load("credit_model.pkl") 

st.title("💳 Credit Risk Prediction App")

st.markdown("""
This tool predicts whether a loan applicant is a **high** or **low** credit risk based on key personal and financial information.
""")


st.markdown("### Age")
age = st.slider("", 18, 75, 30)

st.markdown("### Sex")
sex = st.selectbox("", ["male", "female"])

st.markdown("### Job Type")
job = st.selectbox("", [0, 1, 2, 3])

st.markdown("### Housing")
housing = st.selectbox("", ["own", "rent", "free"])

st.markdown("### Saving Account")
saving_account = st.selectbox("", ["little", "moderate", "rich", "quite rich", "no saving"])

st.markdown("### Checking Account")
checking_account = st.selectbox("", ["little", "moderate", "rich", "no checking"])

st.markdown("### Credit Amount (€)")
credit_amount = st.number_input("", 250, 20000, 3000)

st.markdown("### Duration (months)")
duration = st.slider("", 6, 72, 24)

st.markdown("### Loan Purpose")
purpose = st.selectbox("", ["radio/TV", "education", "furniture/equipment", "car", "business", "domestic appliance", "repairs", "vacation/others"])

st.markdown("<br><br>", unsafe_allow_html=True)


if st.button("🔍 Predict Credit Risk"):
    # Prepare input for prediction
    input_data = pd.DataFrame([{
        'Age': age,
        'Sex': sex,
        'Job': job,
        'Housing': housing,
        'Saving accounts': saving_account,
        'Checking account': checking_account,
        'Credit amount': credit_amount,
        'Duration': duration,
        'Purpose': purpose
    }])

    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0]

    st.subheader("📊 Prediction Result:")
    if prediction == 1:
        st.error(f"High Credit Risk 🚨 (Confidence: {proba[1]*100:.2f}%)")
    else:
        st.success(f"Low Credit Risk ✅ (Confidence: {proba[0]*100:.2f}%)")
