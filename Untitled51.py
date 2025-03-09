#!/usr/bin/env python
# coding: utf-8

# In[2]:

import streamlit as st
import os
import matplotlib.pyplot as plt
import numpy as np
import time
import random

# Set page config - MUST BE FIRST
st.set_page_config(page_title="Smart Savings", page_icon="💰", layout="wide")

# Define file paths for logos
hdfc_logo = "images.png"
sbi_logo = "2a2c1d90075390b22e7e6060254dab0d.jpg"

# Load and display logos if available
st.sidebar.header("🏦 Endorsed By")
if os.path.exists(hdfc_logo) and os.path.exists(sbi_logo):
    st.sidebar.image([hdfc_logo, sbi_logo], width=100)
else:
    st.sidebar.warning("Some logos are missing. Please check file paths.")

# Social Proof Messages
st.sidebar.markdown("🌟 **12,000+ users reached their savings goals this month!**")

# Navigation
page = st.sidebar.radio("📌 Navigate", ["Home", "Savings Tracker", "Leaderboard", "Commitment Contracts", "Financial Tips"]) 

# Function to create a fake savings graph
def plot_savings_graph():
    years = np.arange(2015, 2025, 1)
    savings = np.cumsum(np.random.randint(5, 20, size=len(years))) * 10  # Fake increasing savings

    fig, ax = plt.subplots(figsize=(5, 3))  # Smaller figure size
    ax.plot(years, savings, color="red", linewidth=2)
    ax.set_facecolor("none")  # Transparent background
    fig.patch.set_alpha(0)  # Transparent figure background
    ax.set_xlabel("Year", color='lightgrey')
    ax.set_ylabel("Total Savings (in Lakhs)", color='lightgrey')
    ax.set_title("💰 Savings Growth Over Time", color='lightgrey')
    st.pyplot(fig)

# Function to show a live savings counter
def live_savings_counter():
    total_savings = 500  # Start at ₹500 Cr
    counter_placeholder = st.empty()

    for _ in range(10):  # Simulate live counter update
        total_savings += np.random.randint(1, 10)  # Fake increase
        counter_placeholder.subheader(f"💸 ₹{total_savings} Cr saved by users!")
        time.sleep(1)

# Home Page
if page == "Home":
    st.title("🚀 Smart Savings - Achieve Your Financial Goals")
    st.markdown("### Make smart spending decisions and build wealth with science-backed strategies.")
    
    # Streak Tracking
    streak_days = random.randint(1, 10)
    st.success(f"🔥 You're on a {streak_days}-day savings streak! Keep going!")
    
    # Live Savings Counter
    live_savings_counter()
    
    # Show savings graph
    st.markdown("### 📊 How People Are Saving Over Time")
    plot_savings_graph()
    
    # Fake Reviews
    st.markdown("### ⭐ Customer Reviews")
    reviews = [
        {"name": "Rahul M.", "rating": "⭐⭐⭐⭐⭐", "comment": "Best savings tracker! Helped me stay on budget."},
        {"name": "Sneha P.", "rating": "⭐⭐⭐⭐⭐", "comment": "Love the financial tips. The leaderboard keeps me motivated!"},
        {"name": "Amit K.", "rating": "⭐⭐⭐⭐", "comment": "Simple & effective! Highly recommended."},
    ]
    for review in reviews:
        st.write(f"**{review['name']}** {review['rating']}")
        st.write(f"📝 {review['comment']}")
        st.divider()

# Savings Tracker Page
elif page == "Savings Tracker":
    st.title("📈 Track Your Savings")
    
    # Smart Defaults for Savings Goal
    default_goals = {"Emergency Fund": 50000, "Vacation": 100000, "Retirement": 1000000}
    goal_type = st.selectbox("Choose a savings goal:", list(default_goals.keys()))
    savings_goal = st.number_input("Enter your savings goal (₹)", min_value=1000, step=5000, value=default_goals[goal_type])
    st.success(f"Your goal: ₹{savings_goal:,}")
    
    # Progress Bar with Loss Framing
    saved_amount = np.random.randint(0, savings_goal)
    progress = saved_amount / savings_goal
    st.progress(progress)
    st.write(f"🎯 You've saved **₹{saved_amount:,}** out of **₹{savings_goal:,}**")
    
    # Loss Framing for Withdrawals
    if st.button("Adjust Savings Goal"):
        st.warning("⚠️ Reducing your goal now could delay your financial freedom by 2 years!")
    
    # Fake Monthly Savings Graph
    months = np.arange(1, 13)
    monthly_savings = np.random.randint(5000, 20000, size=12)  # Fake monthly savings
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(months, monthly_savings, marker='o', linestyle='-', color='blue')
    ax.set_facecolor("none")
    fig.patch.set_alpha(0)
    ax.set_xlabel("Month", color='lightgrey')
    ax.set_ylabel("Savings (₹)", color='lightgrey')
    ax.set_title("📈 Monthly Savings Over the Year", color='lightgrey')
    st.pyplot(fig)
    
    # Earn badges
    if progress > 0.75:
        st.balloons()
        st.success("🏆 You've unlocked the **Super Saver Badge!** Keep going!")

# WhatsApp integration (Fake)
st.sidebar.markdown("📩 **Stay on Track**")
st.sidebar.write("Receive weekly savings tips on WhatsApp.")
phone = st.sidebar.text_input("📱 Enter your number")
if phone:
    st.sidebar.success("✅ You'll receive tips on WhatsApp!")
