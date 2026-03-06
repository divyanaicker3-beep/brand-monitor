st.set_page_config(page_title="BrandWatch AI", page_icon="🤖")
st.title("🤖 BrandWatch AI Monitoring Agent")

brand = st.text_input("Enter Brand Name", placeholder="e.g. Samsung")

if st.button("Deploy Agent"):
with st.status("Agent performing autonomous scan...", expanded=True) as status:
st.write("🔄 Connecting to data streams...")
time.sleep(1)
st.write(f"🔎 Scanning for {brand}...")
time.sleep(1)
status.update(label="Analysis Complete!", state="complete")
