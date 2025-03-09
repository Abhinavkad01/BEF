#!/usr/bin/env python
# coding: utf-8

# In[2]:

import streamlit as st
import time

# Page Configurations
st.set_page_config(page_title="Financial Wellness Platform", layout="wide", page_icon="💰")

# Custom Styling
def set_styles():
    st.markdown(
        """
        <style>
        body {font-family: 'Arial', sans-serif; background-color: #f4f4f9;}
        .stButton>button {background: linear-gradient(135deg, #ff8c00, #ff4500); color: white; font-size: 18px; 
                          border-radius: 8px; padding: 12px; font-weight: bold; transition: 0.3s; width: 100%;}
        .stButton>button:hover {transform: scale(1.05); cursor: pointer;}
        .hero-text {text-align: center; font-size: 30px; font-weight: bold; margin-bottom: 20px; color: #333;}
        .stMetric {text-align: center; font-weight: bold; font-size: 20px;}
        .cta-container {text-align: center; margin-top: 20px;}
        .cta-container button {padding: 12px 24px; border-radius: 8px; font-size: 18px;}
        .metric-box {background: white; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);}
        </style>
        """, unsafe_allow_html=True
    )

set_styles()

# Navigation Menu
menu = ["🏠 Home", "🔐 Sign-Up", "📊 Dashboard", "🔮 Simulator", "✍️ Pledge"]
choice = st.sidebar.radio("Navigate", menu)

# Home Page
def home():
    st.markdown("<div class='hero-text'>💰 Transform Your Finances: Next-Level Money Management</div>", unsafe_allow_html=True)
    st.image("https://source.unsplash.com/1000x400/?finance,money", use_container_width=True)
    
    st.markdown("### 🌟 Over ₹500 Cr Saved by Our Users")
    st.success("**Avoid impulse spending & grow your wealth effortlessly.**")
    
    st.markdown("### ✅ Recommended by top financial experts")
    st.image("https://source.unsplash.com/600x200/?bank,finance", use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("📉 **₹15,000/year lost due to poor spending habits**")
    with col2:
        if st.button("🚀 Start Tracking - No Bank Details Needed"):
            st.success("Redirecting to Sign-Up...")
            time.sleep(1)
            st.experimental_rerun()

# Sign-Up Page
def signup():
    st.markdown("<div class='hero-text'>🔐 Create Your Account</div>", unsafe_allow_html=True)
    email = st.text_input("📧 Email Address")
    password = st.text_input("🔒 Password", type="password")
    if st.button("Sign Up"):
        if email and password:
            st.success("✅ Registration Successful! Redirecting to Dashboard...")
            time.sleep(1)
            st.experimental_rerun()
        else:
            st.error("⚠️ Please enter valid details.")

# Simulator Page
def simulator():
    st.markdown("<div class='hero-text'>🔮 Financial Planning Simulator</div>", unsafe_allow_html=True)
    income = st.number_input("💰 Monthly Income (₹)", min_value=1000, value=50000, step=500)
    expenses = st.number_input("📉 Monthly Expenses (₹)", min_value=0, value=20000, step=500)
    savings = income - expenses
    st.metric(label="💾 Estimated Monthly Savings", value=f"₹{savings}")
    if savings < 0:
        st.warning("⚠️ Your expenses exceed your income. Consider reducing unnecessary spending!")
    else:
        st.success("🎯 You're on track! Keep optimizing your savings.")

# Pledge Page
def pledge():
    st.markdown("<div class='hero-text'>✍️ Commitment Pledge</div>", unsafe_allow_html=True)
    st.subheader("Record a video message for your future self!")
    st.text_area("Hey, future me! Stick to this plan!")
    
    if st.button("📜 Save Video Message"):
        st.success("✅ Your message is saved! We will remind you periodically! 🎯")

# Dashboard with Leaderboard
def dashboard():
    st.markdown("<div class='hero-text'>📊 Your Personalized Savings Dashboard</div>", unsafe_allow_html=True)
    st.subheader("🔥 You're on a **5-day savings streak!** Keep going! 🏆")
    
    st.progress(60)  # Endowed Progress Effect
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container():
            st.markdown('<div class="metric-box">💰 **Total Savings:** ₹25,000 <br> 📈 +₹1,500 this month</div>', unsafe_allow_html=True)
    with col2:
        with st.container():
            st.markdown('<div class="metric-box">📉 **Unnecessary Expenses Cut:** ₹8,000 <br> 🔽 -₹500 this week</div>', unsafe_allow_html=True)
    
    st.success("**Your savings are in the top 20% of users your age! 🎉**")

# WhatsApp Integration
def whatsapp_tips():
    st.sidebar.markdown("📩 **Receive Weekly Savings Tips via WhatsApp!**")
    phone = st.sidebar.text_input("Enter Your WhatsApp Number")
    if st.sidebar.button("Subscribe"):
        if phone:
            st.sidebar.success("✅ Subscribed! Get ready for weekly financial insights! 💡")
        else:
            st.sidebar.error("⚠️ Please enter a valid number!")

# Main App Logic
def main():
    whatsapp_tips()
    if choice == "🏠 Home":
        home()
    elif choice == "🔐 Sign-Up":
        signup()
    elif choice == "📊 Dashboard":
        dashboard()
    elif choice == "🔮 Simulator":
        simulator()
    elif choice == "✍️ Pledge":
        pledge()

if __name__ == "__main__":
    main()
