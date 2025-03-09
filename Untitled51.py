#!/usr/bin/env python
# coding: utf-8

# In[2]:

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import os

def load_image(filename, url):
    return filename if os.path.exists(filename) else url

def home_page():
    st.title("💰 Smart Savings - Your Financial Future Starts Here!")
    
    # Live Counter (Bandwagon Effect)
    st.markdown("## ₹500 Cr saved by users! 🔥")
    
    # Fake Reviews & Ratings
    st.markdown("### ⭐⭐⭐⭐⭐ 'This app changed my life!' - Rahul M.")
    st.markdown("### ⭐⭐⭐⭐⭐ 'Best savings tool I've ever used!' - Priya S.")
    
    # Endorsements
    hdfc_logo = load_image("hdfc_logo.png", "https://upload.wikimedia.org/wikipedia/en/thumb/7/72/HDFC_Bank_logo.svg/1200px-HDFC_Bank_logo.svg.png")
    sbi_logo = load_image("sbi_logo.png", "https://upload.wikimedia.org/wikipedia/commons/4/4e/SBI-logo.svg")
    amfi_logo = load_image("amfi_logo.png", "https://upload.wikimedia.org/wikipedia/commons/a/a8/AMFI_India_logo.png")
    st.image([hdfc_logo, sbi_logo, amfi_logo], width=150)
    
    # Peer Comparison
    st.markdown("### Your savings are in the **top 10%** of people your age!")

def dashboard_page():
    st.title("📊 Savings Dashboard")
    
    # Fake Savings Data
    months = np.arange(1, 13)
    savings = np.cumsum(np.random.randint(5000, 15000, size=12))
    
    fig, ax = plt.subplots(facecolor='none')
    ax.patch.set_alpha(0)
    ax.plot(months, savings, marker='o', linestyle='-', color='red', linewidth=2)
    ax.set_xlabel("Month", color='white')
    ax.set_ylabel("Total Savings (₹)", color='white')
    ax.set_title("Your Savings Trend", color='white')
    ax.set_facecolor('none')
    fig.patch.set_alpha(0)
    
    st.pyplot(fig)

def challenges_page():
    st.title("🏆 Challenges & Rewards")
    st.markdown("### **Badges Earned:**")
    st.image("https://img.icons8.com/color/96/medal.png", width=80)
    st.markdown("✅ **₹1L Club - Unlocked!**")
    st.markdown("🔒 **₹5L Club - Only 2% achieve this!**")

def commitment_page():
    st.title("🎥 Record a Message to Your Future Self")
    st.write("Tell your future self why you’re saving money. Your message will be replayed to keep you motivated.")
    video = st.file_uploader("Upload your video message (MP4, AVI, etc.)", type=["mp4", "avi"])
    if video:
        st.video(video)

def whatsapp_page():
    st.title("📩 Get Weekly Tips on WhatsApp!")
    st.write("Stay on track with personalized financial advice directly on WhatsApp.")
    st.button("Subscribe via WhatsApp")

def main():
    st.sidebar.title("📌 Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Dashboard", "Challenges", "Commitment", "WhatsApp"])
    
    if page == "Home":
        home_page()
    elif page == "Dashboard":
        dashboard_page()
    elif page == "Challenges":
        challenges_page()
    elif page == "Commitment":
        commitment_page()
    elif page == "WhatsApp":
        whatsapp_page()

if __name__ == "__main__":
    main()
