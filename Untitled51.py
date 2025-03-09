#!/usr/bin/env python
# coding: utf-8

# In[2]:

import streamlit as st
import os
import matplotlib.pyplot as plt
import numpy as np
import time
import random

# Set page config
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

# Navigation
page = st.sidebar.radio("📌 Navigate", ["Home", "Savings Tracker", "Leaderboard", "Commitment Contracts"]) 

# Function to create a fake savings graph
def plot_savings_graph():
    years = np.arange(2015, 2025, 1)
    savings = np.cumsum(np.random.randint(5, 20, size=len(years))) * 10  # Fake increasing savings

    fig, ax = plt.subplots()
    ax.plot(years, savings, color="red", linewidth=2)
    ax.set_facecolor("none")  # Transparent background
    fig.patch.set_alpha(0)  # Transparent figure background
    ax.set_xlabel("Year", color='lightgrey')
    ax.set_ylabel("Total Savings (in Lakhs)", color='lightgrey')
    ax.set_title("💰 Savings Growth Over Time", color='lightgrey')
    ax.set_xticklabels(years,  color='lightgrey')
    ax.set_xticklabels(savings,  color='lightgrey')
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
    
    # Savings Goal Input
    savings_goal = st.number_input("Enter your savings goal (₹)", min_value=1000, step=5000)
    st.success(f"Your goal: ₹{savings_goal:,}")
    
    # Progress Bar
    saved_amount = np.random.randint(0, savings_goal)
    progress = saved_amount / savings_goal
    st.progress(progress)
    st.write(f"🎯 You've saved **₹{saved_amount:,}** out of **₹{savings_goal:,}**")
    
    # Earn badges
    if progress > 0.75:
        st.balloons()
        st.success("🏆 You've unlocked the **Super Saver Badge!** Keep going!")

# Leaderboard Page
elif page == "Leaderboard":
    st.title("🏆 Savings Leaderboard")
    
    # Fake leaderboard
    users = ["Rahul", "Sneha", "Amit", "Priya", "Vikram", "You"]
    savings = sorted([np.random.randint(50000, 300000) for _ in users], reverse=True)
    
    # Identify user's position
    user_savings = random.randint(50000, 200000)
    rank = sum(user_savings < np.array(savings))
    
    # Bar chart visualization with transparency and subtle colors
    fig, ax = plt.subplots()
    colors = ["#B0C4DE" if s != user_savings else "#FF6347" for s in savings]
    ax.bar(users, savings, color=colors)
    ax.set_facecolor("none")  # Transparent background
    fig.patch.set_alpha(0)  # Transparent figure background
    ax.set_title("📊 Savings Distribution - Where You Stand", color='lightgrey')
    ax.set_ylabel("Total Savings (₹)", color='lightgrey')
    ax.set_xticklabels(users, rotation=30, color='lightgrey')
    ax.set_xticklabels(savings,  color='lightgrey')
    st.pyplot(fig)
    
    st.info(f"📊 Your savings are in the **top {100 - (rank * 20)}%** of users your age!")

# Commitment Contracts Page
elif page == "Commitment Contracts":
    st.title("📜 Financial Commitment Contracts")
    st.write("Set up a commitment contract where you wager money to stay on track with your savings goals!")
    
    goal = st.text_input("🎯 What is your savings goal?")
    amount = st.number_input("💰 Amount to commit (₹)", min_value=1000, step=1000)
    anti_charity = st.selectbox("💀 Choose an anti-charity (where money goes if you fail)",
                               ["Random Opponent", "Political Party You Dislike", "Competitor Bank"])
    referee = st.text_input("👀 Name of your referee (someone to verify progress)")
    
    if st.button("Create Commitment Contract"):
        st.success(f"✅ Commitment Contract Created! If you fail, ₹{amount:,} will be sent to {anti_charity}.")

# WhatsApp integration (Fake)
st.sidebar.markdown("📩 **Stay on Track**")
st.sidebar.write("Receive weekly savings tips on WhatsApp.")
phone = st.sidebar.text_input("📱 Enter your number")
if phone:
    st.sidebar.success("✅ You'll receive tips on WhatsApp!")
