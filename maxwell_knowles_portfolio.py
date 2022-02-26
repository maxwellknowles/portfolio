## Imports
import urllib
import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
import base64
import urllib.request
from PIL import Image

with st.sidebar:
    choose = option_menu("Maxwell's Portfolio", ["Bio & Resume", "Low-Code Prototypes", "Data-Intensive Work", "Products & Features", "Consulting with Eikona", "Contact"],
                         icons=['house', 'arrow-clockwise', 'kanban', '123','activity', 'archive'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#BBBBBD"},
        "icon": {"color": "white", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#BBBBBD"},
    }
    )

if choose == 'Bio & Resume':
    st.title('Maxwell Knowles')
    st.header('Bio & Resume')
    with st.container():
        st.subheader("Bio")

    st.subheader("Resume") 
    resume = "https://github.com/maxwellknowles/portfolio/raw/main/Maxwell_Knowles_Resume_2022.pdf"
    st.write("[Download Resume](%s)" % resume)

    with open("Maxwell_Knowles_Resume_2022.pdf", "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)

if choose == "Data-Intensive Work":
    st.title("Data-Intensive Work")
    st.header('Churn Analysis Report Coded in R')
    with open("Churn-Analysis--12-20-to-4-21-.pdf", "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)
    
    st.header('Mock Vendor Performance Report Coded in R')
    with open("Renewal-Mill-Performance-April-2021.pdf", "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)

if choose == "Contact":
    st.title("Contact Information")
    linkedin = "https://www.linkedin.com/in/maxwell-knowles/"
    st.write("[LinkedIn](%s)" % linkedin)
    spotify = "https://open.spotify.com/artist/2p2YiVrDP0scQefeefDqCO?si=LIyTgWg5T1KL7Fn79lXHPw"
    st.write("[Spotify](%s)" % spotify)
    st.write("Email: maxknowles27@gmail.com")
   
