#!/usr/bin/env python
# coding: utf-8

# In[2]:

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# Set page title
st.set_page_config(page_title="Financial Wellness Platform", layout="wide")

# Header
st.title("Behavioral-Optimized Financial Wellness Platform")

# Dynamic Live Counter (Non-recurring, Just Display Column)
def format_currency(value):
    return f"₹{value:,.0f} Cr"

st.sidebar.header("Total Savings by Users")
col1, col2 = st.sidebar.columns([2, 1])
col1.metric(label="Total Savings", value=format_currency(500))  # Static ₹500 Cr Display

# Endorsements & Trust Signals
st.sidebar.header("Trusted by Experts")
st.sidebar.image(["hdfc_logo.png", "sbi_logo.png", "amfi_logo.png"], width=100)

# Fake Line Graph for Savings Trend
years = np.arange(1, 13)
savings = np.cumsum(np.random.randint(5, 15, size=12))

fig, ax = plt.subplots()
ax.plot(years, savings, marker='o', linestyle='-', color='blue', label="Savings Growth")
ax.set_title("User Savings Over the Year")
ax.set_xlabel("Months")
ax.set_ylabel("Savings (₹ in thousands)")
ax.legend()
st.pyplot(fig)

# Challenges & Rewards
st.subheader("Earn Rewards for Smart Financial Decisions")
st.write("Complete financial challenges and earn badges to stay motivated!")
st.image("badges_example.png", caption="Your Achievements", use_column_width=True)

# Commitment Video Feature
st.subheader("Commit to Your Future Self")
st.write("Record a message for your future self as a financial commitment.")
if st.button("Record Video Message"):
    st.write("Feature coming soon!")

# Leaderboard & Peer Comparison
st.subheader("Where Do You Stand?")
st.write("Your savings are in the **top 20%** of users your age!")

# WhatsApp Integration
st.subheader("Stay Engaged with Weekly WhatsApp Tips")
st.write("Get weekly savings insights and nudges on WhatsApp to keep you on track.")
st.button("Subscribe via WhatsApp")

st.success("🚀 Get started today and build a financially secure future!")
