import streamlit as st
import pandas as pd
import os

# === Load the pre-generated Folium map ===
html_path = "stp_thermal_map_final.html"
with open(html_path, 'r', encoding='utf-8') as f:
    map_html = f.read()

# === Show map in browser ===
st.components.v1.html(map_html, height=700, scrolling=True)

# === Sidebar CSV download interface ===
st.sidebar.title("Download Nearby STPs")
csv_dir = "csvs"
csv_files = [f for f in os.listdir(csv_dir) if f.endswith(".csv")]
thermal_names = [f.replace("_nearby_stps.csv", "").replace("_", " ") for f in csv_files]

selection = st.sidebar.selectbox("Select a Thermal Plant:", thermal_names)

# Load selected CSV
selected_file = selection.replace(" ", "_") + "_nearby_stps.csv"
df = pd.read_csv(os.path.join(csv_dir, selected_file))
st.sidebar.write(f"**Nearby STPs for:** {selection}")
st.sidebar.dataframe(df)

# Download button
st.sidebar.download_button(
    label="📥 Download CSV",
    data=df.to_csv(index=False),
    file_name=selected_file,
    mime="text/csv"
)
