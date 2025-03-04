import streamlit as st

# Set Page Configuration
st.set_page_config(page_title="About the Creator", layout="wide")

# Custom CSS for Styling
st.markdown(
    """
    <style>
        .big-font {
            font-size: 36px !important;
            font-weight: bold;
            text-align: center;
            color: #E63946; 
        }
        .bio-text {
            font-size: 28px;
            text-align: center;
            color:  #457B9D;
            font-weight: bold;
        }
        .container {
            background: rgba(0, 0, 0, 0.8);
            padding: 25px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0px 4px 10px rgba(255, 204, 0, 0.5);
        }
        .button {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)



# Main Content
st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown('<p class="big-font">🏠 Welcome to Growth Mindset Project</p>', unsafe_allow_html=True)
st.markdown('<p class="bio-text">Created by <b>Mashal Afzal</b> – an educationist passionate about innovation and learning.</p>', unsafe_allow_html=True)
st.markdown('<p class="bio-text">This web app is designed to inspire and foster a growth mindset through interactive features.</p>', unsafe_allow_html=True)
st.markdown('<p class="bio-text">🌟 Explore, learn, and grow with us! Use the sidebar to navigate.</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Display Profile Image
st.image("images/Tree.webp", width=100, caption="Mashal Afzal - Creator of Growth Mindset Project", use_container_width=True)
# GitHub Button
st.markdown(
    """
    <div style="text-align: center;">
        <a href="https://github.com/mashal-afzal" target="_blank">
            <button style="background-color: #333; color: white; padding: 10px 20px; font-size: 18px; border-radius: 5px; border: none; cursor: pointer;">
                🔗 Connect on GitHub
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
