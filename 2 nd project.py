import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

# ------------------ SAMPLE DATA ------------------
data = {
    "amount": [100, 2000, 150, 5000, 300, 10000, 250, 8000],
    "transactions_per_day": [1, 10, 2, 15, 3, 20, 2, 18],
    "foreign_transaction": [0, 1, 0, 1, 0, 1, 0, 1],
    "fraud": [0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[["amount", "transactions_per_day", "foreign_transaction"]]
y = df["fraud"]

model = LogisticRegression()
model.fit(X, y)

# ------------------ STREAMLIT UI ------------------

st.set_page_config(page_title="Fraud Detection System", layout="centered")

st.title("💳 Fraud Detection System")
st.write("Enter transaction details to predict fraud.")

amount = st.number_input("Transaction Amount (₹)", min_value=0)
transactions = st.number_input("Transactions per Day", min_value=0)
foreign = st.selectbox("Foreign Transaction?", ["No", "Yes"])

foreign_value = 1 if foreign == "Yes" else 0

if st.button("Check Fraud"):
    input_data = [[amount, transactions, foreign_value]]
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction is Legitimate")
