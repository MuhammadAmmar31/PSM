import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔐 Password Strength Checker")
st.markdown("""
## Welcome to the ultimate Password Strength Checker! 👋
Use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
We will give you helpful tips to create a **Strong Password** 🔒
""")

# Password history storage (simple list to keep last 3 passwords)
if 'password_history' not in st.session_state:
    st.session_state.password_history = []

password = st.text_input("**Enter Your Password**", type="password")

feedback = []
score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
        
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both upper and lower case characters.")
        
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")
        
    if re.search(r'[!@#$%&*]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (!@#$%&*).")

    if score == 4:
        feedback.append("😃 Your password is strong! 🎉")
    elif score == 3:
        feedback.append("🙂 Your password is medium strength. It could be stronger.")
    else:
        feedback.append("😟 Your Password is weak. Please make it stronger.")
    
    # Store password in history
    if password not in st.session_state.password_history:
        st.session_state.password_history.append(password)
        if len(st.session_state.password_history) > 3:
            st.session_state.password_history.pop(0)  # Keep only the last 3 passwords
    
    st.markdown("## Improvement Suggestions")
    for tip in feedback:
        st.write(tip)
else:
    st.info("Please enter your password to get started.")

# Display password history
if st.session_state.password_history:
    st.markdown("## Password History (Last 3)")
    for i, past_password in enumerate(st.session_state.password_history, 1):
        st.write(f"{i}. {past_password}")
