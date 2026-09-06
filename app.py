import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Kucchu Pucchu EVM",
    page_icon="🗳️",
    layout="wide",
)

# Load the fully self-contained EVM app (HTML + CSS + JS + images all
# embedded inline as base64 data, so nothing needs to be fetched
# separately — this avoids broken-image issues inside Streamlit's
# sandboxed iframe).
html_path = Path(__file__).parent / "embedded_app.html"
html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=1400, scrolling=True)
