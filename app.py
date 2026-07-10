import streamlit as st
from utils.ai_helper import generate_ugc_ad

st.set_page_config(
    page_title="AI UGC Ad Generator",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #b27a01 0%,
        #c78b0d 20%,
        #d79d1b 45%,
        #e7b74c 65%,
        #fee1a1 88%,
        #fee8ba 100%
    );
    background-attachment: fixed;
}

/* Main container */
.block-container{
    max-width:1100px;
    padding-top:2rem;
}

/* Heading */

h1{
    color:#2F241C;
    text-align:center;
    font-weight:700;
}

h3{
    color:#4A3520;
}

p{
    color:#5A4736;
}

/* Input boxes */

input{
    border-radius:10px !important;
}

/* Select boxes */

div[data-baseweb="select"]{
    border-radius:10px;
}

/* Button */

.stButton>button{
    width:100%;
    background:#C87D00;
    color:white;
    border:none;
    border-radius:12px;
    height:52px;
    font-size:19px;
    font-weight:700;
    transition:0.3s;
}

.stButton>button:hover{
    background:#A96900;
}

/* Download */

.stDownloadButton>button{
    width:100%;
    border-radius:12px;
    background:#FFF3D6;
    color:white;
    border:1px solid #D3A645;
    font-weight:600;
}

hr{
    border-color:#DDBA67;
}

/* Input Labels */

div[data-testid="stWidgetLabel"] p{
    color:black !important;
    font-size:22px !important;
    font-weight:1000 !important;
    letter-spacing:0.3px;
}

div[data-testid="stAlert"]{
    font-size:22px;
    font-weight:1000;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<div style="text-align:center;padding:25px 10px;">

<h1 style="font-size:48px;color:#4A3B36;">
🎬 AI UGC Ad Generator
</h1>

<h3 style="color:#7A665E;">
Create Scroll-Stopping UGC Ads using AI
</h3>

<p style="font-size:18px;color:#6B5D57;">
Generate authentic ad scripts for Instagram Reels, YouTube Shorts,
TikTok & Facebook in seconds.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="display:flex;
justify-content:space-between;
gap:15px;
margin-bottom:30px;">

<div style="
background:#FFF9EC;
padding:20px;
border-radius:15px;
flex:1;
text-align:center;
box-shadow:0 10px 25px rgba(85,55,0,.18);">

🔥<br>
<b>5 Viral Hooks</b>

</div>

<div style="
background:#FFF9EC;
padding:20px;
border-radius:15px;
flex:1;
text-align:center;
box-shadow:0 10px 25px rgba(85,55,0,.18);">

🎥<br>
<b>3 UGC Scripts</b>

</div>

<div style="
background:#FFF9EC;
padding:20px;
border-radius:15px;
flex:1;
text-align:center;
box-shadow:0 10px 25px rgba(85,55,0,.18);">

📢<br>
<b>5 CTAs</b>

</div>

<div style="
background:#FFF9EC;
padding:20px;
border-radius:15px;
flex:1;
text-align:center;
box-shadow:0 10px 25px rgba(85,55,0,.18);">

📸<br>
<b>Caption & Hashtags</b>

</div>

</div>
""", unsafe_allow_html=True)


st.divider()

# -----------------------------
# User Inputs
# -----------------------------

col1,col2=st.columns(2)

with col1:
    st.markdown(
    """
    <h2 style="color:#4A3520;">
    🏢 Business Details
    </h2>
    """,
    unsafe_allow_html=True
    )

    business_name=st.text_input("Business Name")

    business_type=st.text_input("Business Type")

    product_service=st.text_input("Product / Service")

with col2:
    st.markdown("## 🎯 Marketing Details")

    target_audience=st.text_input("Target Audience")

    platform=st.selectbox(
        "Platform",
        [
            "Instagram Reels",
            "Facebook",
            "YouTube Shorts",
            "TikTok"
        ]
    )

    tone=st.selectbox(
        "Tone",
        [
            "Friendly",
            "Professional",
            "Luxury",
            "Funny",
            "Emotional"
        ]
    )

    goal=st.selectbox(
        "Goal",
        [
            "Increase Sales",
            "Brand Awareness",
            "Lead Generation"
        ]
    )

st.divider()

# -----------------------------
# Generate Button
# -----------------------------

if st.button("🚀 Generate UGC Ad Pack"):

    if (
        business_name
        and business_type
        and product_service
        and target_audience
    ):

        with st.spinner("Generating your UGC Ad Pack..."):

            output = generate_ugc_ad(
                business_name,
                business_type,
                product_service,
                target_audience,
                platform,
                tone,
                goal
            )

        st.success("UGC Ad Pack Generated Successfully!")

        st.markdown("---")
        st.markdown("## 📦 Your AI Generated UGC Ad Pack")

        st.markdown(output)

        st.download_button(
            label="⬇ Download UGC Ad Pack",
            data=output,
            file_name=f"{business_name.replace(' ', '_')}_UGC_Ad_Pack.txt",
            mime="text/plain"
        )

    else:
        st.warning("Please fill in all the required fields.")

st.markdown("---")
st.markdown(
    """
    <div style="text-align:center;
    font-size:18px;
    font-weight:600;
    color:#3B2A19;">

    Built with love by <b>SHREE</b>

    </div>
    """,
    unsafe_allow_html=True
)