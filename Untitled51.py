#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import time

def main():
    st.set_page_config(page_title="HelloWallet - Financial Wellness", page_icon="💰", layout="wide")
    
    # Custom Styling
    st.markdown("""
        <style>
            .main-container {
                background-color: #f5f7fa;
            }
            .title {
                font-size: 40px;
                font-weight: bold;
                color: #2c3e50;
            }
            .subtitle {
                font-size: 24px;
                color: #34495e;
            }
            .cta-button {
                background-color: #27ae60;
                color: white;
                font-size: 18px;
                font-weight: bold;
                padding: 12px 20px;
                border-radius: 8px;
            }
        </style>
    """, unsafe_allow_html=True)
    
    home()

def home():
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>Take Control of Your Financial Future</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Join over <b>500,000+</b> Indians already saving smarter with HelloWallet!</p>", unsafe_allow_html=True)
    
    st.image("https://source.unsplash.com/1200x400/?finance,money", use_column_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Why Choose HelloWallet?")
        st.write("✅ Save money effortlessly with AI-driven budgeting")
        st.write("✅ Get free financial health reports")
        st.write("✅ Reduce hidden expenses & optimize savings")
        st.write("✅ Trusted by top financial experts & influencers")
        
    with col2:
        st.markdown("### Exclusive Offer!")
        st.success("Get ₹2,000 worth of smart budgeting tools for FREE! 🎉")
        st.button("Claim Your Free Trial", key="signup_button")
        
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Get Started Now!"):
        sign_up()

def sign_up():
    st.markdown("### Sign Up in 30 Seconds")
    phone = st.text_input("Enter Your Phone Number for OTP Verification")
    if phone:
        with st.spinner("Sending OTP..."):
            time.sleep(2)
        otp = st.text_input("Enter OTP Sent to Your Phone", type="password")
        if otp:
            with st.spinner("Verifying..."):
                time.sleep(2)
            st.success("You're all set! Your savings journey starts now! 🎯")

def dashboard():
    st.title("Your Financial Dashboard")
    st.write("Track your savings, set goals, and grow your wealth.")
    st.metric(label="Total Savings", value="₹50,000", delta="+₹5,000 this month")
    st.progress(70)
    
    st.button("Optimize My Expenses")
    st.button("View My Financial Health Report")
    
if __name__ == "__main__":
    main()
