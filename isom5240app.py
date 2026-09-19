import streamlit as st
import time
from PIL import Image

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="ISOM5240 Demo",
    page_icon="🚀",
    layout="centered"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(
            135deg,
            #f5f7ff 0%,
            #eef6ff 50%,
            #f8f5ff 100%
        );
    }

    /* Main title */
    .main-title {
        text-align: center;
        padding: 30px 20px;
        border-radius: 18px;
        background: linear-gradient(135deg, #4F46E5, #7C3AED);
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 8px 25px rgba(79, 70, 229, 0.20);
    }

    .main-title h1 {
        margin: 0;
        font-size: 38px;
    }

    .main-title p {
        margin-top: 10px;
        font-size: 17px;
        opacity: 0.9;
    }

    /* Content cards */
    .card {
        background-color: white;
        padding: 22px;
        border-radius: 15px;
        margin: 15px 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
        border-left: 5px solid #6366F1;
    }

    /* Button styling */
    div.stButton > button {
        background: linear-gradient(90deg, #4F46E5, #7C3AED);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 25px;
        font-weight: 600;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(79, 70, 229, 0.30);
        color: white;
        border: none;
    }

    /* File uploader */
    [data-testid="stFileUploader"] {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #E5E7EB;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown("""
<div class="main-title">
    <h1>🚀 ISOM5240 Streamlit Demo</h1>
    <p>Interactive Streamlit application hosted on Hugging Face</p>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# Introduction
# --------------------------------------------------
st.markdown("""
<div class="card">
    <h3>👋 Welcome!</h3>
    <p>
        Welcome to a demo app showcasing some basic
        <b>Streamlit components</b>.
    </p>
    <p>✨ Upload an image below and interact with the app!</p>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# Image uploader
# --------------------------------------------------
st.subheader("📸 Upload an Image")

uploaded_image = st.file_uploader(
    "Choose a JPG or PNG image",
    type=["jpg", "jpeg", "png"]
)


# --------------------------------------------------
# Display uploaded image
# --------------------------------------------------
if uploaded_image is not None:

    with st.spinner("✨ Loading your image..."):
        time.sleep(1)

        image = Image.open(uploaded_image)

    st.success("✅ Image uploaded successfully!")

    st.image(
        image,
        caption="Your Uploaded Image",
        use_container_width=True
    )


# --------------------------------------------------
# Button interaction
# --------------------------------------------------
st.divider()

st.subheader("🎯 Try an Interaction")

if st.button("✨ Click Me"):
    st.balloons()
    st.success("🎉 You clicked the button!")
