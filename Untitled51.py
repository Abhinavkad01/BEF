#!/usr/bin/env python
# coding: utf-8

# In[2]:

import streamlit as st
import os
import matplotlib.pyplot as plt
import numpy as np

# Set Page Config
st.set_page_config(page_title="Financial Wellness Platform", layout="wide")

# Function to load images (fallback to URLs if not found)
def load_image(filename, url):
    return filename if os.path.exists(filename) else url

# Image Paths / URLs
hdfc_logo = load_image("hdfc_logo.png", "https://upload.wikimedia.org/wikipedia/en/thumb/7/72/HDFC_Bank_logo.svg/1200px-HDFC_Bank_logo.svg.png")
sbi_logo = load_image("sbi_logo.png", "https://upload.wikimedia.org/wikipedia/commons/4/4e/SBI-logo.svg")
amfi_logo = load_image("amfi_logo.png", "https://upload.wikimedia.org/wikipedia/commons/a/a8/AMFI_India_logo.png")

# Sidebar - Endorsements & Trust Signals
with st.sidebar:
    st.image([hdfc_logo, sbi_logo, amfi_logo], width=100)
    st.markdown("### Recommended by Top Financial Experts")

# Fake Live Counter - ₹500 Cr saved by users
st.markdown("## 💰 ₹500 Cr saved by users!")
st.markdown("*(Scarcity & Bandwagon Effect)*")

# Fake Line Graph - Showing Savings Over Time
st.markdown("### 📊 Savings Growth Over the Year")
fig, ax = plt.subplots()
months = np.arange(1, 13)
savings = np.cumsum(np.random.randint(5000, 15000, size=12))  # Fake increasing savings data
ax.plot(months, savings, marker='o', linestyle='-', color='green')
ax.set_xlabel("Month")
ax.set_ylabel("Total Savings (₹)")
ax.set_xticks(months)
ax.set_title("Savings Trend Over the Year")
st.pyplot(fig)

# Commitment Bias - Video Message to Future Self
st.markdown("## 🎥 Record a Message to Your Future Self")
st.write("Tell your future self why you’re saving money. Your message will be replayed to keep you motivated.")
video = st.file_uploader("Upload your video message (MP4, AVI, etc.)", type=["mp4", "avi"])

# Gamification - Challenges & Rewards
st.markdown("## 🏆 Challenges & Rewards")
st.write("Complete smart spending challenges and earn badges for saving efficiently!")
st.image("https://img.icons8.com/color/96/medal.png", width=80)  # Example badge icon

# Peer Comparison & Leaderboard
st.markdown("## 📈 Leaderboard - Where Do You Stand?")
leaderboard_data = {
    "User": ["You", "Rahul", "Priya", "Amit", "Sneha"],
    "Savings (₹)": [75000, 80000, 70000, 65000, 62000]
}
st.table(leaderboard_data)

# WhatsApp Integration - Weekly Savings Tips
st.markdown("## 📩 Get Weekly Tips on WhatsApp!")
st.write("Stay on track with personalized financial advice directly on WhatsApp.")
st.button("Subscribe via WhatsApp")

st.success("🔹 This platform is built using behavioral economics principles to maximize user engagement and savings!")
