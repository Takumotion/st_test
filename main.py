'''
https://www.youtube.com/watch?v=Sb0A9i6d320
'''
from pathlib import Path
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as mpl
from PIL import Image, ImageOps

# --- PATH SETTING ---
THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = THIS_DIR / "assets"
STYLES_DIR = THIS_DIR / "styles"
CSS_FILE = STYLES_DIR / "main.css"


# --- GENERAL SETTINGS ---
# STRIPE_CHECKOUT = "https;//buy.stripe.com******"
CONTACT_EMAIL = "office@takumotion.com"
PRODUCT_NAME = """
Welcome to my homepage! 
My name is Taku and I am a highly skilled data freelance analyst with a background in physics and 
experience in both the semiconductor and gaming industries. But currently I am working in the health industrie sector, developing an algorithm for a female health app. 

As a data analyst and software architect, I have a strong understanding of the latest Python technologies 
and techniques, and have a track record of success in using data to drive business decisions and solutions. 
In addition to my professional experience, I have a passion for analyzing financial markets, including the stock and cryptocurrency markets, 
and have the ability to apply complex algorithms and techniques such as filtering and Fourier analysis to my work.

I believe that my diverse background in both physics and data analysis, combined with my experience as a game designer, 
allows me to approach problems with a unique perspective and find innovative solutions. I look forward to sharing my knowledge and experience with you, 
and hope to work with you in the future to drive meaningful results through data-driven decision making.
"""



# --- PAGE CONFIG ---
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(
	page_title=PRODUCT_NAME,
	page_icon=":chart_with_upwards_trend:",
	layout="centered", # centered
	#initial_sidebar_state="collapsed",
	)

# --- MAIN SECTION ---
st.header(PRODUCT_NAME)
