#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import time

# Set up page configuration
st.set_page_config(page_title="Financial Wellness Platform", layout="wide")


# In[3]:


# Navigation menu
menu = ["Home", "Sign-Up", "Dashboard", "Simulator", "Pledge"]
choice = st.sidebar.selectbox("Navigate", menu)

def home():
    st.title("💰 The Smartest Way to Save Money Without Changing Your Lifestyle")
    st.markdown("### 🌟 ₹500 Cr saved by users")
    st.info("**Indians lose ₹15,000/year due to impulse spending. Fix it now!**")
    st.image("https://source.unsplash.com/1000x400/?finance,money")
    
    if st.button("🚀 Start Tracking in 30 Seconds - No Bank Details Needed"):
        st.success("Redirecting to Sign-Up...")
        time.sleep(1)
        st.experimental_rerun()

def signup():
    st.title("📩 Sign-Up for Smarter Savings")
    st.subheader("Join Now & Get ₹100 Cashback After 3 Months!")
    
    name = st.text_input("👤 Name")
    email = st.text_input("✉️ Email")
    income = st.number_input("💵 Monthly Income (₹)", min_value=1000, step=500)
    
    if st.button("Join & Start Saving Now!"):
        st.success(f"Welcome {name}! Redirecting to Dashboard...")
        time.sleep(1)
        st.experimental_rerun()

def dashboard():
    st.title("📊 Your Personalized Savings Dashboard")
    st.subheader("You're on a **5-day savings streak!** Keep going! 🏆")
    st.progress(60)  # Endowed Progress Effect
    
    st.write("### Your Savings Performance 📈")
    st.metric("💰 Total Savings", "₹25,000", "+₹1,500 this month")
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


# In[4]:


if __name__ == "__main__":
    main()


# In[ ]:




