import streamlit as st
import pandas as pd
import numpy as np
import qrcode
from io import BytesIO

# -------------------------------------------
# Step 1: Generate QR Code for the App URL
# -------------------------------------------
app_url = "http://localhost:8501"  # Replace with deployed URL after hosting
qr = qrcode.make(app_url)
buf = BytesIO()
qr.save(buf, format="PNG")
st.image(buf.getvalue(), caption="Scan to Open Voter Registration Form")

# -------------------------------------------
# Step 2: Initialize Session State to Store Data
# -------------------------------------------
if "voter_data" not in st.session_state:
    st.session_state.voter_data = []

# -------------------------------------------
# Step 3: Create the Application Form
# -------------------------------------------
st.title("🗳️ Voter Registration Form")

with st.form("voter_form", clear_on_submit=True):
    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=18, max_value=120, step=1)
    gender = st.radio("Gender", ["Male", "Female", "Other"])
    address = st.text_area("Residential Address")
    aadhar = st.text_input("Aadhar Number (last 4 digits)")
    state = st.selectbox("Select Your State", ["Tamil Nadu", "Karnataka", "Kerala", "Telangana", "Andhra Pradesh", "Other"])
    submit_btn = st.form_submit_button("Submit Application")

# -------------------------------------------
# Step 4: Store Data in List / NumPy Array / Pandas DataFrame
# -------------------------------------------
if submit_btn:
    voter_entry = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Address": address,
        "Aadhar_Last4": aadhar,
        "State": state
    }

    # Add to session list
    st.session_state.voter_data.append(voter_entry)
    st.success(f"✅ Voter registration submitted for {name}!")

# -------------------------------------------
# Step 5: Display Data as a Pandas DataFrame
# -------------------------------------------
if len(st.session_state.voter_data) > 0:
    st.subheader("📋 Registered Voter List")
    df = pd.DataFrame(st.session_state.voter_data)

    # Convert to NumPy for demonstration
    np_data = np.array(df)
    st.dataframe(df)

    # Optional: Save to CSV
    df.to_csv("voter_list.csv", index=False)
    st.download_button("📥 Download CSV", df.to_csv(index=False), "voter_list.csv")

    st.caption("Data stored in Pandas DataFrame and NumPy array format.")
