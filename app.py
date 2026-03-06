import streamlit as st
import time

st.set_page_config(page_title="BrandWatch AI", page_icon="🤖")

st.title("🤖 BrandWatch AI Monitoring Agent")
st.markdown("Automated Brand Mention & Alert System")

brand = st.text_input("Enter Brand Name to Monitor", placeholder="e.g. Samsung, Apple")

if st.button("Deploy Agent"):
with st.status("Agent performing autonomous scan...", expanded=True) as status:
st.write("🔄 Connecting to global data streams...")
time.sleep(1)
st.write(f"🔎 Scraping mentions for '{brand}'...")
time.sleep(2)
st.write("🧠 Running Sentiment Analysis NLP...")
time.sleep(1)
status.update(label="Analysis Complete!", state="complete", expanded=False)
