import streamlit as st

# Custom CSS for styling the menu page
st.markdown(
    """
    <style>
        .title {
            font-size: 70px;
            font-weight: bold;
            color: #E63946; /* Red */
            text-align: center;
        }
        .subtitle {
            font-size: 50px;
            font-weight: bold;
            color: #457B9D; /* Blue */
            text-align: center;
            margin-top: 20px;
        }
        .menu-item {
            font-size: 35px;
            font-weight: normal;
            color: #1D3557; /* Dark Blue */
            text-align: center;
        }
        .price {
            font-size: 22px;
            font-weight: bold;
            color: #E76F51; /* Orange */
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Menu Page Title
st.markdown('<h1 class="title">🍽 Our Delicious Menu 🍽</h1>', unsafe_allow_html=True)

# Sections with Menu Items
st.markdown('<p class="subtitle">🥗 Starters</p>', unsafe_allow_html=True)
st.markdown('<p class="menu-item">Greek Salad <span class="price"> Rs: 750</span></p>', unsafe_allow_html=True)
st.markdown('<p class="menu-item">Garlic Bread <span class="price"> Rs: 400</span></p>', unsafe_allow_html=True)

st.image("images/starter.jpg", width=100, caption="Starter",use_container_width=True)

st.markdown('<p class="subtitle">🍕 Main Course</p>', unsafe_allow_html=True)
st.markdown('<p class="menu-item">Margherita Pizza <span class="price"> Rs: 2500</span></p>', unsafe_allow_html=True)
st.markdown('<p class="menu-item">Pasta Alfredo <span class="price"> Rs: 2000</span></p>', unsafe_allow_html=True)

st.image("images/main course.jpg", width=100, caption="Main Course", use_container_width=True)

st.markdown('<p class="subtitle">🍰 Desserts</p>', unsafe_allow_html=True)
st.markdown('<p class="menu-item">Chocolate Lava Cake <span class="price"> Rs: 1000</span></p>', unsafe_allow_html=True)
st.markdown('<p class="menu-item">Cheesecake <span class="price"> Rs: 950</span></p>', unsafe_allow_html=True)

st.image("images/dessert.jpg", width=100, caption= "Desserts", use_container_width=True )

st.markdown('<p class="subtitle">🍹 Beverages</p>', unsafe_allow_html=True)
st.markdown('<p class="menu-item">Fresh Lemonade <span class="price"> Rs: 600</span></p>', unsafe_allow_html=True)
st.markdown('<p class="menu-item">Mango Smoothie <span class="price"> Rs: 800</span></p>', unsafe_allow_html=True)

st.image("images/beverages.jpg", width=100, caption="Beverages", use_container_width=True)


