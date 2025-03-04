import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
        .title {
            font-size: 42px;
            font-weight: bold;
            color: #E63946; /* Red */
            text-align: center;
        }
        .review-box {
            background-color: #F1FAEE;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        .customer-name {
            font-size: 20px;
            font-weight: bold;
            color: #1D3557;
        }
        .customer-review {
            font-size: 18px;
            font-style: italic;
            color: #457B9D;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title
st.markdown('<p class="title">💬 Customer Reviews</p>', unsafe_allow_html=True)

# Sample Reviews
reviews = [
    {"name": "Ali", "review": "The best food I've ever had! The pasta was divine. 🍝"},
    {"name": "Sara", "review": "Great ambiance and excellent service. Highly recommended! ⭐⭐⭐⭐⭐"},
    {"name": "Ahmed", "review": "Loved the desserts! The chocolate lava cake was to die for. 🍫"}
]

# Display Reviews
for review in reviews:
    st.markdown(f"""
        <div class="review-box">
            <p class="customer-name">⭐ {review['name']}</p>
            <p class="customer-review">"{review['review']}"</p>
        </div>
    """, unsafe_allow_html=True)

# User Review Submission
st.markdown("### ✍️ Leave a Review")
name = st.text_input("Your Name")
review_text = st.text_area("Your Review")
if st.button("Submit Review"):
    if name and review_text:
        st.success("✅ Thank you for your review!")
    else:
        st.warning("⚠️ Please enter both name and review.")

 #image
st.image("images/review.jpg", caption="Happy Customers!", use_container_width=True)
