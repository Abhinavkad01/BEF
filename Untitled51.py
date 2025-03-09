#!/usr/bin/env python
# coding: utf-8

# In[2]:

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.set_page_config(page_title="Smart Financial Wellness", layout="wide")
    
    st.title("Welcome to Your Financial Wellness Hub")
    st.subheader("Empowered by Behavioral Economics")
    
    # Sidebar Navigation
    st.sidebar.title("Navigation")
    option = st.sidebar.radio("Go to", ["Home", "Savings Calculator", "Investment Simulator", "Financial Dashboard"])
    
    if option == "Home":
        home_page()
    elif option == "Savings Calculator":
        savings_calculator()
    elif option == "Investment Simulator":
        investment_simulator()
    elif option == "Financial Dashboard":
        financial_dashboard()

def home_page():
    st.write("""
    ## Why Choose Us?
    - **Smart Defaults:** Pre-set recommendations for financial plans.
    - **Commitment Devices:** Set savings goals and track progress.
    - **Loss Aversion Messaging:** See what you might lose if you don't act now!
    - **Social Proof:** Join thousands of users improving their savings.
    """)
    
    st.image("https://source.unsplash.com/800x400/?finance,money", caption="Make Smarter Financial Choices Today!")
    
    st.success("Start your journey by setting a savings goal now!")

def savings_calculator():
    st.header("Savings Goal Calculator")
    initial_amount = st.number_input("Enter Initial Savings (₹)", min_value=0, value=5000)
    monthly_savings = st.number_input("Enter Monthly Savings (₹)", min_value=0, value=500)
    years = st.slider("Savings Duration (Years)", 1, 30, 10)
    interest_rate = 6.5 / 100  # Assumed average annual return
    
    total_savings = initial_amount * (1 + interest_rate) ** years + monthly_savings * (((1 + interest_rate) ** years - 1) / interest_rate)
    
    st.metric("Projected Savings in ₹", round(total_savings, 2))
    
    st.info("Commit now to reach your goal!")

def investment_simulator():
    st.header("Investment Growth Simulator")
    investment = st.number_input("Investment Amount (₹)", min_value=0, value=10000)
    rate = st.slider("Expected Annual Return (%)", 1, 20, 8) / 100
    years = st.slider("Investment Period (Years)", 1, 30, 10)
    
    future_value = investment * (1 + rate) ** years
    
    st.metric("Estimated Portfolio Value in ₹", round(future_value, 2))
    
    st.warning("Don't miss out on compounding growth! Start investing today.")

def financial_dashboard():
    st.header("Your Personalized Financial Dashboard")
    data = pd.DataFrame({
        "Category": ["Savings", "Investments", "Debt"],
        "Amount": [20000, 50000, 10000]
    })
    
    fig, ax = plt.subplots()
    ax.pie(data["Amount"], labels=data["Category"], autopct='%1.1f%%', colors=["green", "blue", "red"])
    st.pyplot(fig)
    
    st.success("Track and optimize your finances efficiently!")

if __name__ == "__main__":
    main()

