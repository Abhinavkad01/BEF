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
# Website Name
st.sidebar.title("💰 Smart Savings")

# Define file paths for logos
hdfc_logo = "images.png"
sbi_logo = "2a2c1d90075390b22e7e6060254dab0d.jpg"
Groww_logo = "Groww.jpg"

# Load and display logos if available
st.sidebar.header("🏦 Endorsed By")
if os.path.exists(hdfc_logo) and os.path.exists(sbi_logo):
    st.sidebar.image([hdfc_logo, sbi_logo], width=100)
else:
    st.sidebar.warning("Some logos are missing. Please check file paths.")

# Social Proof Messages
st.sidebar.markdown("🌟 **12,000+ users reached their savings goals this month!**")

# Navigation
page = st.sidebar.radio("📌 Navigate", ["Signup", "Home", "Savings Tracker", "Leaderboard", "Commitment Contracts", "Financial Tips", "Community & Challenges"]) 


# Signup Page
if page == "Signup":
    st.title("🔐 Join Smart Savings Today")
    st.markdown("### Take control of your financial future with our smart savings platform!")
# Add images only under the Signup Page
    signup_image = ["Screenshot 2025-03-10 193239.png"]
    for image in signup_image:
        if os.path.exists(image):
            st.image(image, use_container_width=True)
        else:
            st.warning(f"{image} not found. Please check file path.")

    
    # Signup Form
    name = st.text_input("👤 Full Name")
    email = st.text_input("📧 Email Address")
    password = st.text_input("🔑 Create Password", type="password")
    goal_preference = st.selectbox("🎯 What’s your primary savings goal?", ["Emergency Fund", "Buy a Car", "Vacation", "Retirement", "Investment Growth"])
    agree = st.checkbox("I agree to the terms and conditions")
    
    if st.button("🚀 Get Started"):
        if name and email and password and agree:
            st.success(f"🎉 Welcome, {name}! Your journey to smart savings starts now!")
        else:
            st.error("⚠️ Please fill in all fields and agree to the terms.")
    # Add images only under the Signup Page
    signup_images = ["Screenshot 2025-03-10 122106.png", "Screenshot 2025-03-10 124543.png","Screenshot 2025-03-10 193559.png"]
    for image in signup_images:
        if os.path.exists(image):
            st.image(image, use_container_width=True)
        else:
            st.warning(f"{image} not found. Please check file path.")
# Function to create a fake savings graph
def plot_savings_graph():
    years = np.arange(2015, 2025, 1)
    savings = np.cumsum(np.random.randint(5, 20, size=len(years))) * 10  # Fake increasing savings

    fig, ax = plt.subplots(figsize=(5, 3))  # Smaller figure size
    ax.plot(years, savings, color="red", linewidth=2)
    ax.set_facecolor("none")  # Transparent background
    fig.patch.set_alpha(0)  # Transparent figure background
    ax.set_xlabel("Year", color='black')
    ax.set_ylabel("Total Savings (in Lakhs)", color='black')
    ax.set_title("Savings Growth Over Time", color='black')
    st.pyplot(fig)

# Function to show a live savings counter
def live_savings_counter():
    total_savings = 500  # Start at ₹500 Cr
    counter_placeholder = st.empty()

    for _ in range(10):  # Simulate live counter update
        total_savings += np.random.randint(1, 10)  # Fake increase
        counter_placeholder.subheader(f"💸 ₹{total_savings} Cr saved by users!")
        time.sleep(1)
# Lock-in Mechanism for Withdrawals
if page == "Savings Tracker":
    st.warning("🔒 Lock-in Mechanism: Your savings are secured until the set date. Withdrawals allowed only in emergencies.")
    if st.button("Request Withdrawal"):
        st.warning("⏳ Your request has been placed. Withdrawals require a 24-hour delay before execution.")


# Home Page
if page == "Home":
    st.title("🚀 Smart Savings - Achieve Your Financial Goals")
    st.markdown("### Make smart spending decisions and build wealth with science-backed strategies.")
    
    # Streak Tracking
    streak_days = random.randint(1, 10)
    st.success(f"🔥 You're on a {streak_days}-day savings streak! Keep going!")

    # Loss Aversion Banner
    st.warning("⚠️ Indians lose ₹15,000/year due to impulse spending. Fix it now!")
    
    # Peer Accountability
    st.info("👀 Your friend Raj completed his savings goal—can you?")
    
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
        
elif page == "Savings Tracker":
    st.title("📈 Track Your Savings")
    st.warning("🔒 Lock-in Mechanism: Your savings are secured until the set date. Withdrawals allowed only in emergencies.")

    if st.button("Request Withdrawal", key="withdraw_button"):
        st.warning("⏳ Your request has been placed. Withdrawals require a 24-hour delay before execution.")

    st.markdown("### 💰 Accounts Overview")
    accounts = {"Checking": 25000, "Credit Card": -5000, "Savings": 80000}
    col1, col2, col3 = st.columns(3)
    col1.metric("Checking", f"₹{accounts['Checking']:,}")
    col2.metric("Credit Card", f"₹{accounts['Credit Card']:,}")
    col3.metric("Savings", f"₹{accounts['Savings']:,}")

    # Expenses Overview Bar Chart (Smaller Size)
    st.subheader("📊 Expenses Overview")
    expenses = {"Groceries": 6000, "Transport": 4000, "Health": 3000, "Entertainment": 2000}
    fig, ax = plt.subplots(figsize=(4, 2))  # Adjusted size
    ax.bar(expenses.keys(), expenses.values(), color=['blue', 'green', 'red', 'purple'])
    ax.set_ylabel("Amount (₹)")
    ax.set_title("Monthly Expenses")
    st.pyplot(fig)
    # Savings Goals
    default_goals = {"Emergency Fund": 50000, "Vacation": 100000, "Retirement": 1000000}
    goal_type = st.selectbox("Choose a savings goal:", list(default_goals.keys()))
    savings_goal = st.number_input("Enter your savings goal (₹)", min_value=1000, step=5000, value=default_goals[goal_type])
    st.success(f"Your goal: ₹{savings_goal:,}")

    # Progress Bar
    saved_amount = np.random.randint(0, savings_goal)
    progress = saved_amount / savings_goal
    st.progress(progress)
    st.write(f"🎯 You've saved **₹{saved_amount:,}** out of **₹{savings_goal:,}**")

    # Loss Framing for Withdrawals
    if st.button("Adjust Savings Goal", key="adjust_goal_button"):
        st.warning("⚠️ Reducing your goal now could delay your financial freedom by 2 years!")

    # Fake Monthly Savings Graph
    months = np.arange(1, 13)
    monthly_savings = np.random.randint(5000, 20000, size=12)
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(months, monthly_savings, marker='o', linestyle='-', color='blue')
    ax.set_xlabel("Month")
    ax.set_ylabel("Savings (₹)")
    ax.set_title("Monthly Savings Over the Year")
    st.pyplot(fig)

    # Goals with Progress
    st.subheader("🎯 Future Goals")
    goals = [
        {"name": "Buy a Car", "total": 500000, "saved": random.randint(100000, 400000)},
        {"name": "Go on a Vacation", "total": 200000, "saved": random.randint(50000, 150000)},
        {"name": "Buy a House", "total": 2000000, "saved": random.randint(500000, 1500000)},
        {"name": "Retirement Fund", "total": 5000000, "saved": random.randint(1000000, 4000000)}
    ]
    for goal in goals:
        st.write(f"🔜 {goal['name']} - Saved: ₹{goal['saved']:,} / ₹{goal['total']:,}")

    # Suggested Savings Amounts
    st.subheader("💡 Suggested Savings")
    recommended_savings = ["₹5,000 (Beginner)", "₹10,000 (Intermediate)", "₹20,000 (Advanced)"]
    savings_choice = st.radio("Select a recommended amount:", recommended_savings, index=0)
    st.success(f"✅ You've chosen to save {savings_choice} per month!")

    # Finance Tip & News
    if st.button("Get a Quick Finance Tip & News Update!", key="finance_news"):
        tips = [
            "Automate savings to avoid decision fatigue!",
            "Invest at least 20% of your income.",
            "Track expenses weekly to stay accountable."
        ]
        news = [
            "Markets hit all-time high today!",
            "New savings scheme launched by the government.",
            "Top CEOs reveal their money-saving habits!"
        ]
        st.info(f"💡 {random.choice(tips)} | 📰 {random.choice(news)}")

    # Achievement Badges
    if progress > 0.75:
        st.balloons()
        st.success("🏆 You've unlocked the **Super Saver Badge!** Keep going!")    # Leaderboard Page
elif page == "Leaderboard":
    st.title("🏆 Savings Leaderboard")
    
    # Fake leaderboard
    users = ["Rahul", "Sneha", "Amit", "Priya", "Vikram", "You"]
    savings = sorted([np.random.randint(50000, 300000) for _ in users], reverse=True)
    
    # Identify user's position
    user_savings = random.randint(50000, 200000)
    rank = sum(user_savings < np.array(savings))
    
    # Bar chart visualization with transparency and subtle colors
    fig, ax = plt.subplots(figsize=(5, 3))
    colors = ["#B0C4DE" if s != user_savings else "#FF6347" for s in savings]
    ax.bar(users, savings, color=colors)
    ax.set_facecolor("none")  # Transparent background
    fig.patch.set_alpha(0)  # Transparent figure background
    ax.set_title(" Savings Distribution - Where You Stand", color='black')
    ax.set_ylabel("Total Savings (₹)", color='black')
    ax.set_xticklabels(users, rotation=30, color='black')
    ax.set_yticklabels(savings,  color='black')
    st.pyplot(fig)
    
    st.info(f"📊 Your savings are in the **top {100 - (rank * 20)}%** of users your age!")
    
    # Public Accountability
    if st.button("Share My Progress on Social Media! 🎯"):
        st.success("✅ Your savings progress has been shared successfully!")
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
    # Financial Tips Page
elif page == "Financial Tips":
    st.title("💡 Smart Financial Tips")
    
    # AI-Powered Savings & Finance Tips
    ai_tips = [
        "🤖 AI Suggestion: Based on your spending pattern, reducing dining out by 20% can save ₹5,000 monthly!",
        "📊 AI Insight: Investing in an index fund for 5 years could yield 12% annual returns!",
        "💡 Tip: Set up an auto-debit savings plan to avoid temptation spending.",
        "🔄 Reinvesting your tax refunds can accelerate your wealth growth!",
        "🧠 Behavioral Trick: Name your savings account (e.g., 'Dream Home Fund') to stay motivated!"
    ]
    st.write(random.choice(ai_tips))
    
    if st.button("Get Another AI Tip"):
        st.write(random.choice(ai_tips))
    
    # Paid Expert Advice Section with Ratings
    st.markdown("### 🎓 Get Personalized Advice from Finance Experts")
    experts = [
        {"name": "Dr. Anil Mehta", "experience": "Ex-Chief Economist at HDFC Bank", "education": "PhD in Behavioral Finance", "rating": round(random.uniform(4.5, 5.0), 1), "reviews": random.randint(50, 200)},
        {"name": "Priya Sharma", "experience": "Former Investment Manager at Goldman Sachs", "education": "MBA, Harvard Business School", "rating": round(random.uniform(4.3, 4.9), 1), "reviews": random.randint(30, 150)},
        {"name": "Rahul Khanna", "experience": "Senior Financial Advisor at Morgan Stanley", "education": "CFA, London Business School", "rating": round(random.uniform(4.2, 4.8), 1), "reviews": random.randint(40, 180)},
        {"name": "Sneha Patel", "experience": "Ex-Head of Personal Finance at ICICI", "education": "Certified Financial Planner (CFP)", "rating": round(random.uniform(4.6, 5.0), 1), "reviews": random.randint(60, 250)}
    ]
    
    for expert in experts:
        st.write(f"**{expert['name']}** - {expert['experience']} ({expert['education']})")
        st.write(f"⭐ Rating: {expert['rating']} ({expert['reviews']} reviews)")
        if st.button(f"Book a Session with {expert['name']}"):
            st.success(f"📅 A consultation request has been sent to {expert['name']}! They will reach out to you soon.")
    
    st.markdown("---")
    # Standard Financial Tips
    st.markdown("### 📌 Quick Financial Tips")
    tips = [
        "🚗 Want to buy a car? You need to save ₹10,000 per month for 3 years!",
        "🏠 Planning to buy a house? Start investing 20% of your salary today!",
        "🎓 Student loan? Pay off high-interest debt first to save money in the long run!",
        "✈️ Dreaming of a vacation? Set up an automated travel fund and save ₹5000 every month!",
        "📈 Want to retire early? Increase your monthly investments by just 5% every year!"
    ]
    st.write(random.choice(tips))
    
    if st.button("Get Another Tip"):
        st.write(random.choice(tips))

# Community & Challenges
elif page == "Community & Challenges":
    st.title("🌍 Community & Challenges")
    
    # Savings Streak Challenge
    st.markdown("### 🔥 Savings Streak Challenge")
    st.info("Save consistently for 30 days and win exclusive rewards!")
    
    # Weekly Savings Battle
    st.markdown("### 🏆 Weekly Savings Battle")
    st.write("Compete with your friends and see who saves the most each week!")
    
    # Interactive Savings Goals
    st.markdown("### 🎯 Interactive Savings Goals")
    if st.button("Set a New Challenge Goal"):
        st.success("✅ Challenge Goal Created! Keep pushing towards your target.")
    
    # Social Sharing for Motivation
    st.markdown("### 📢 Share Your Progress")
    if st.button("Share My Savings Streak on Social Media 🎯"):
        st.success("✅ Your progress has been shared successfully!")
    
    # Join Savings Support Groups
    st.markdown("### 🤝 Join a Savings Support Group")
    st.write("Find like-minded savers and stay accountable!")
    if st.button("Find a Group"):
        st.success("✅ You've been added to a savings group!")
    
    # WhatsApp Community Join
    st.markdown("### 📲 Join Our WhatsApp Savings Community")
    phone = st.text_input("📱 Enter your number to join community updates")
    if phone:
        st.success("✅ You'll receive weekly savings tips & community updates!")
# WhatsApp integration (Fake)
st.sidebar.markdown("📩 **Stay on Track**")
st.sidebar.write("Receive weekly savings tips on our newsletter.")
phone = st.sidebar.text_input("📱 Enter your number")
if phone:
    st.sidebar.success("✅ You'll receive Receive weekly newsletter")


