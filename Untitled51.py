#!/usr/bin/env python
# coding: utf-8

# In[2]:

import streamlit as st
import time
import pandas as pd
import random
import matplotlib.pyplot as plt

# Ensure images exist in the correct directory
def load_image(filename, url=None):
    try:
        return filename  # If file exists locally
    except:
        return url  # If using a URL fallback

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Dashboard", "Reviews", "Goal Tracking"])

# -------------------- PAGE: HOME --------------------
if page == "Home":
    st.title("💰 Smart Finance: Nudge Your Way to Wealth!")

    # Dynamic Live Counter (Not recurring)
    total_savings = 500000000  # ₹500 Cr
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"### **₹{total_savings:,} Saved by Users!** 🏦")
    with col2:
        st.image(["hdfc_logo.png", "sbi_logo.png"], width=80)

    # Behavioral Prompt
    st.subheader("🚀 'The smartest way to save money without changing your lifestyle.'")

    # Fake Savings Graph
    st.markdown("### 📊 How Our Users Have Grown Their Savings Over the Year")
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    savings = [random.randint(20000, 100000) for _ in months]

    fig, ax = plt.subplots()
    ax.plot(months, savings, marker='o', color='red')
    ax.set_facecolor("none")  # Transparent background
    st.pyplot(fig)

    st.markdown("💡 *Our users have consistently increased their savings by following our behavioral nudges!*")

# -------------------- PAGE: DASHBOARD --------------------
elif page == "Dashboard":
    st.title("📈 Your Finance Dashboard")
    
    # Gamification Elements
    streak = random.randint(1, 10)
    st.subheader(f"🔥 You're on a {streak}-day savings streak! Keep going!")

    # Budget Tracker
    spent = random.randint(5000, 20000)
    limit = 25000
    st.progress(spent / limit)
    st.markdown(f"💸 You've spent ₹{spent} this month. *Stay within your ₹{limit} budget!*")

    # Pre-commitment Bias
    if st.button("Record Message to Future Self 🎥"):
        st.markdown("📹 *Recording your message... 'Hey future me, keep saving!'*")

    # Social Influence - Peer Comparison
    percentile = random.randint(10, 90)
    st.subheader(f"🏆 Your savings rank in the **top {100 - percentile}%** of users your age!")

# -------------------- PAGE: REVIEWS --------------------
elif page == "Reviews":
    st.title("🌟 What Our Users Say")
    
    # Fake Reviews with Star Ratings
    reviews = [
        ("Amit Sharma", 5, "This platform changed my financial habits forever!"),
        ("Priya Mehta", 4, "Love the gamification and nudges. Super effective!"),
        ("Rahul Verma", 5, "Started saving ₹10,000 per month without even noticing."),
        ("Sonia Kapoor", 4, "Wish I knew about this earlier. Smart savings strategies!"),
        ("Arjun Desai", 5, "Peer comparison and goal tracking keep me motivated."),
    ]

    for name, rating, text in reviews:
        st.subheader(f"⭐ {'⭐' * rating} ({rating}/5)")
        st.write(f"**{name}**: {text}")

# -------------------- PAGE: GOAL TRACKING --------------------
elif page == "Goal Tracking":
    st.title("🎯 Achieve Your Savings Goals")

    goal = st.slider("Set your savings goal (₹)", min_value=5000, max_value=50000, step=5000, value=20000)
    saved = random.randint(1000, goal)
    st.progress(saved / goal)
    st.markdown(f"📊 You've saved ₹{saved} out of ₹{goal}. *Keep going!*")

    # Loss Aversion Nudge
    if saved < goal * 0.5:
        st.warning(f"⚠️ You're behind schedule! Missing your goal could cost you ₹{goal - saved} over time.")

    # WhatsApp Integration (Fake CTA)
    st.button("📩 Get Weekly Savings Tips on WhatsApp")

# -------------------- END --------------------
st.sidebar.info("Built using behavioral science to make saving effortless! 🚀")
