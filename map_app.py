import streamlit as st

# Set layout and title
st.set_page_config(layout="wide")
st.title("STP–Thermal Plant Interactive Map (Maharashtra)")
st.markdown("View infrastructure linkages between STPs and thermal power plants, with district boundaries and distances.")

# Path to your saved folium map
map_path = r"F:\MITRA_WORK\GIS Lab\Analysis\stp_thermal_map_final.html"

# Load and display the HTML content of the map
try:
    with open(map_path, "r", encoding="utf-8") as f:
        folium_map_html = f.read()
    st.components.v1.html(folium_map_html, height=700, scrolling=True)
except FileNotFoundError:
    st.error(f"❌ Map file not found at: {map_path}")
    st.stop()
