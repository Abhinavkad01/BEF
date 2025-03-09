#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
from datetime import datetime

def home():
    st.title("Welcome to HelloWallet India")
    
    # Social Proof & FOMO
    st.markdown("### Join 5,00,000+ Indians securing their financial future with HelloWallet")
    st.markdown("Your friends in Mumbai and Delhi are already using HelloWallet! Don’t be left behind.")
    
    # Loss Aversion Prompt
    st.warning("Every day you delay, you lose ₹500 in unoptimized savings. Don't wait!")
    
    # Framing Effect
    if st.button("Get Your Free Financial Health Report"):
        st.session_state["page"] = "signup"
        st.rerun()

def signup():
    st.title("Sign Up for HelloWallet")
    
    # Precommitment Bias
    choice = st.radio("Do you want to take control of your finances?", ["Yes, I want to save more", "No, I am okay losing money"])
    if choice == "Yes, I want to save more":
        st.session_state["page"] = "details"
        st.rerun()
    elif choice == "No, I am okay losing money":
        st.error("Think again! Financial security starts today.")

def details():
    st.title("Complete Your Sign-Up in 3 Easy Steps")
    
    # Step 1: Phone Number
    phone = st.text_input("Enter your phone number (OTP will be sent)")
    if phone:
        st.session_state["page"] = "otp"
        st.rerun()

def otp():
    st.title("Verify Your OTP")
    otp_code = st.text_input("Enter OTP sent to your phone")
    if otp_code:
        st.session_state["page"] = "goals"
        st.rerun()

def goals():
    st.title("Set Your Financial Goals")
    goal = st.selectbox("What’s your biggest financial goal?", ["Save for Home", "Reduce Expenses", "Increase Investments"])
    if st.button("Continue"):
        st.session_state["page"] = "dashboard"
        st.rerun()

def dashboard():
    st.title("Your Personalized Financial Dashboard")
    st.success("Congratulations! Your savings journey starts now!")
    st.markdown("You have been auto-enrolled into a free personal finance course.")
    
    # Gamification Reward
    st.balloons()
    st.success("First ₹500 saved! Keep going!")

def main():
    if "page" not in st.session_state:
        st.session_state["page"] = "home"
    
    if st.session_state["page"] == "home":
        home()
    elif st.session_state["page"] == "signup":
        signup()
    elif st.session_state["page"] == "details":
        details()
    elif st.session_state["page"] == "otp":
        otp()
    elif st.session_state["page"] == "goals":
        goals()
    elif st.session_state["page"] == "dashboard":
        dashboard()

if __name__ == "__main__":
    main()
