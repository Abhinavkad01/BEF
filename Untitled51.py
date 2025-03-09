#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import time

# Set up page configuration
st.set_page_config(page_title="Financial Wellness Platform", layout="wide")

# Custom Styling
def set_styles():
    st.markdown(
        """
        <style>
        body {font-family: 'Arial', sans-serif;}
        .stButton>button {background-color: #ff8c00; color: white; font-size: 16px; border-radius: 8px; padding: 10px;}
        .stMetric {text-align: center; font-weight: bold;}
        </style>
        """, unsafe_allow_html=True
    )

set_styles()

# Navigation menu
menu = ["Home", "Sign-Up", "Dashboard", "Simulator", "Pledge"]
choice = st.sidebar.selectbox("Navigate", menu)

def home():
    st.title("💰 Smart Money Management, Simplified")
    st.markdown("### 🌟 Over ₹500 Cr Saved by Our Users")
    st.image("https://source.unsplash.com/1000x400/?finance,money")
    st.success("**Avoid impulse spending & grow your wealth effortlessly.**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("📈 **₹15,000/year lost due to poor spending habits**")
    with col2:
        if st.button("🚀 Start Tracking in 30 Seconds - No Bank Details Needed"):
            st.success("Redirecting to Sign-Up...")
            time.sleep(1)
            st.rerun()

def signup():
    st.title("📩 Sign-Up & Take Control of Your Finances")
    st.subheader("Join now & get ₹100 Cashback After 3 Months!")
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 Name")
        email = st.text_input("✉️ Email")
    with col2:
        income = st.number_input("💵 Monthly Income (₹)", min_value=1000, step=500)
    
    if st.button("Join & Start Saving Now!"):
        st.success(f"Welcome {name}! Redirecting to Dashboard...")
        time.sleep(1)
        st.rerun()

def dashboard():
    st.title("📊 Your Personalized Savings Dashboard")
    st.subheader("You're on a **5-day savings streak!** Keep going! 🏆")
    st.progress(60)  # Endowed Progress Effect
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("💰 Total Savings", "₹25,000", "+₹1,500 this month")
    with col2:
        st.metric("📉 Unnecessary Expenses Cut", "₹8,000", "-₹500 this week")
    
    st.success("**Your savings are in the top 20% of users your age! 🎉**")

def simulator():
    st.title("🔮 Future Wealth Simulator")
    amount = st.slider("💸 How much can you save per month?", 1000, 50000, 10000)
    years = st.slider("📅 For how many years?", 1, 20, 5)
    future_savings = amount * years * 12
    
    st.success(f"If you save ₹{amount}/month, you'll have **₹{future_savings}** in {years} years! 💰")
    st.image("https://source.unsplash.com/800x300/?success,goal")

def pledge():
    st.title("✍️ Commitment Pledge")
    pledge_text = st.text_area("Write your personal savings pledge")
    
    if st.button("📜 Save Pledge"):
        st.success("✅ Pledge Saved! Stay committed to your goals!")
        time.sleep(1)

def main():
    if choice == "Home":
        home()
    elif choice == "Sign-Up":
        signup()
    elif choice == "Dashboard":
        dashboard()
    elif choice == "Simulator":
        simulator()
    elif choice == "Pledge":
        pledge()

if __name__ == "__main__":
    main()
