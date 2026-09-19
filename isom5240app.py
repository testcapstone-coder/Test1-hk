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

    /* Main title box */
    .main-title {
        text-align: center;
        padding: 30px 20px;
        border-radius: 18px;
        background: linear-gradient(135deg, #4F46E5, #7C3AED);
        margin-bottom: 25px;
        box-shadow: 0 8px 25px rgba(79, 70, 229, 0.20);
    }

    /* Main title */
    .main-title h1 {
        color: #FFD166;
        margin: 0;
        font-size: 38px;
    }

    /* Main subtitle */
    .main-title p {
        color: #E0E7FF;
        margin-top: 10px;
        font-size: 17px;
    }

    /* Welcome card */
    .card {
        background-color: white;
        padding: 22px;
        border-radius: 15px;
        margin: 15px 0 25px 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
        border-left: 5px solid #6366F1;
    }

    /* Welcome title */
    .card h3 {
        color: #7C3AED;
        margin-top: 0;
    }

    /* Welcome text */
    .card p {
        color: #475569;
        font-size: 16px;
    }

    /* Upload section title */
    .upload-title {
        color: #E11D48;
        font-size: 27px;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    /* Interaction section title */
    .interaction-title {
        color: #059669;
        font-size: 27px;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    /* Normal Streamlit text */
    .stMarkdown p {
        color: #374151;
    }

    /* File uploader */
    [data-testid="stFileUploader"] {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #C7D2FE;
        box-shadow: 0 3px 10px rgba(0, 0, 0, 0.04);
    }

    /* File uploader label */
    [data-testid="stFileUploader"] label {
        color: #4338CA !important;
        font-weight: 600;
    }

    /* Button */
    div.stButton > button {
        background: linear-gradient(90deg, #4F46E5, #7C3AED);
        color: #FFFFFF;
        border: none;
        border-radius: 10px;
        padding: 10px 25px;
        font-weight: 600;
        font-size: 16px;
        transition: 0.3s;
    }

    /* Button hover */
    div.stButton > button:hover {
        background: linear-gradient(90deg, #7C3AED, #DB2777);
        color: #FFFFFF;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(79, 70, 229, 0.30);
        border: none;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# Main Header
# --------------------------------------------------
st.markdown("""
<div class="main-title">
    <h1>🚀 ISOM5240 Streamlit Demo</h1>
    <p>Interactive Streamlit Application on Hugging Face</p>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# Welcome Section
# --------------------------------------------------
st.markdown("""
<div class="card">
    <h3>👋 Welcome to the Demo!</h3>
    <p>
        This application showcases some basic
        <b>Streamlit components</b> in a colorful and interactive interface.
    </p>
    <p>
        Upload an image below and explore the different features of the app.
    </p>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# Image Upload Section
# --------------------------------------------------
st.markdown(
    '<div class="upload-title">📸 Upload Your Image</div>',
    unsafe_allow_html=True
)

st.write("Choose a JPG, JPEG or PNG image from your computer.")

uploaded_image = st.file_uploader(
    "Select your image",
    type=["jpg", "jpeg", "png"]
)


# --------------------------------------------------
# Display Uploaded Image
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
# Divider
# --------------------------------------------------
st.divider()


# --------------------------------------------------
# Interaction Section
# --------------------------------------------------
st.markdown(
    '<div class="interaction-title">🎯 Try an Interaction</div>',
    unsafe_allow_html=True
)

st.write("Click the button below to see what happens!")

if st.button("✨ Click Me"):
    st.balloons()
    st.success("🎉 You clicked the button!")
