#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import time
import random

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
        .metric-box {background: white; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);}
        .progress-text {text-align: center; font-size: 18px; font-weight: bold; color: #0077b6;}
        </style>
        """, unsafe_allow_html=True
    )

set_styles()

# Navigation Menu
menu = ["🏠 Home", "🔐 Sign-Up", "📊 Dashboard", "🔮 Simulator", "✍️ Pledge"]
choice = st.sidebar.radio("Navigate", menu)

def home():
    st.markdown("<div class='hero-text'>💰 Join 32,567 Smart Savers – Are You Next?</div>", unsafe_allow_html=True)
    st.image("https://source.unsplash.com/1000x400/?finance,money", use_column_width=True)
    
    st.markdown("### 🌟 Over ₹500 Cr Saved by Our Users")
    st.success("**Every month, you're losing ₹15,000 to impulse spending. Start saving now!**")
    
    if st.button("🚀 Start Tracking – No Bank Details Needed"):
        st.success("Redirecting to Sign-Up...")
        time.sleep(1)
        st.experimental_rerun()

def signup():
    st.markdown("<div class='hero-text'>📩 Join & Take Control of Your Finances</div>", unsafe_allow_html=True)
    st.subheader("🎁 Get ₹100 Cashback After 3 Months of Saving!")
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 Name")
        email = st.text_input("✉️ Email")
    with col2:
        income = st.number_input("💵 Monthly Income (₹)", min_value=1000, step=500)
    
    progress = 0
    if name:
        progress += 40
    if email:
        progress += 40
    if income > 1000:
        progress += 20
    
    st.progress(progress)
    st.markdown(f"<p class='progress-text'>{progress}% Completed!</p>", unsafe_allow_html=True)
    
    if st.button("✅ Join & Start Saving!"):
        if name and email:
            st.success(f"🎉 Welcome, {name}! Redirecting to Dashboard...")
            time.sleep(1)
            st.experimental_rerun()
        else:
            st.error("⚠️ Please fill out all fields!")

def dashboard():
    st.markdown("<div class='hero-text'>📊 Your Personalized Savings Dashboard</div>", unsafe_allow_html=True)
    streak = random.randint(1, 30)
    st.subheader(f"🔥 You’re on a **{streak}-day savings streak!** Keep going! 🏆")
    
    st.progress(min(streak * 3, 100))  # Endowed Progress Effect
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="metric-box">💰 **Total Savings:** ₹25,000 <br> 📈 +₹1,500 this month</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-box">📉 **Missed Savings:** ₹8,000 <br> 😟 You could have saved ₹500 more this week!</div>', unsafe_allow_html=True)
    
    st.success("**Your savings are in the top 20% of users your age! 🎉**")

def simulator():
    st.markdown("<div class='hero-text'>🔮 Future Wealth Simulator</div>", unsafe_allow_html=True)
    
    amount = st.slider("💸 Monthly Savings (₹)", 1000, 50000, 10000)
    years = st.slider("📅 Investment Duration (Years)", 1, 20, 5)
    expected_return = st.slider("📈 Expected Annual Return (%)", 4, 15, 8)
    
    future_savings = amount * ((1 + expected_return / 100) ** years - 1) / (expected_return / 100) * 12
    
    goal_items = ["🏝️ Trip to Bali", "📱 Latest iPhone", "🚗 Dream Car", "🏡 Home Down Payment"]
    goal = random.choice(goal_items)
    
    st.success(f"🎯 If you save ₹{amount}/month, you'll have **₹{round(future_savings, 2)}** in {years} years – enough for a **{goal}!** 💰")
    st.image("https://source.unsplash.com/800x300/?success,goal", use_column_width=True)

def pledge():
    st.markdown("<div class='hero-text'>✍️ Your Savings Commitment</div>", unsafe_allow_html=True)
    
    goal_options = ["Save ₹5,000 every month", "Invest 20% of salary", "Cut down online shopping"]
    pledge_text = st.selectbox("Choose a Savings Pledge", goal_options)
    
    if st.button("📜 Save Pledge"):
        st.success("✅ Pledge Saved! Stay committed to your goals! 🎯")

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
