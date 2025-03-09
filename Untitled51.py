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

def home():
    st.markdown("<div class='hero-text'>💰 Transform Your Finances: Next-Level Money Management</div>", unsafe_allow_html=True)
    st.image("https://source.unsplash.com/1000x400/?finance,money", use_container_width=True)
    
    st.markdown("### 🌟 Over ₹500 Cr Saved by Our Users")
    st.success("**Avoid impulse spending & grow your wealth effortlessly.**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("📉 **₹15,000/year lost due to poor spending habits**")
    with col2:
        if st.button("🚀 Start Tracking - No Bank Details Needed"):
            st.success("Redirecting to Sign-Up...")
            time.sleep(1)
            st.experimental_rerun()

def signup():
    st.markdown("<div class='hero-text'>📩 Sign-Up & Take Control of Your Finances</div>", unsafe_allow_html=True)
    st.subheader("🎁 Join now & get ₹100 Cashback After 3 Months!")

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 Name", help="Enter your full name")
        email = st.text_input("✉️ Email", help="Enter a valid email address")
    with col2:
        income = st.number_input("💵 Monthly Income (₹)", min_value=1000, step=500, help="Your estimated monthly income")
    
    if st.button("✅ Join & Start Saving!"):
        if name and email:
            st.success(f"🎉 Welcome, {name}! Redirecting to Dashboard...")
            time.sleep(1)
            st.experimental_rerun()
        else:
            st.error("⚠️ Please fill out all fields!")

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

def simulator():
    st.markdown("<div class='hero-text'>🔮 Future Wealth Simulator</div>", unsafe_allow_html=True)
    
    amount = st.slider("💸 Monthly Savings (₹)", 1000, 50000, 10000)
    years = st.slider("📅 Investment Duration (Years)", 1, 20, 5)
    expected_return = st.slider("📈 Expected Annual Return (%)", 4, 15, 8)
    
    # Future Savings Calculation
    future_savings = amount * ((1 + expected_return / 100) ** years - 1) / (expected_return / 100) * 12
    
    st.success(f"🎯 If you save ₹{amount}/month, you'll have **₹{round(future_savings, 2)}** in {years} years! 💰")
    st.image("https://source.unsplash.com/800x300/?success,goal", use_container_width=True)

def pledge():
    st.markdown("<div class='hero-text'>✍️ Commitment Pledge</div>", unsafe_allow_html=True)
    
    pledge_text = st.text_area("Write your personal savings pledge (e.g., I will save 20% of my income)")
    
    if st.button("📜 Save Pledge"):
        if pledge_text:
            st.success("✅ Pledge Saved! Stay committed to your goals! 🎯")
        else:
            st.warning("⚠️ Please enter your pledge before saving!")

# Main App Logic
def main():
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
