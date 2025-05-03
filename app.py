
import streamlit as st
from PIL import Image

# Initialize session state for product quantities
if 'quantities' not in st.session_state:
    st.session_state.quantities = [5, 4, 6, 3, 8, 2, 10, 7]

# Product list
products = [
    {"id": 1, "name": "Pepsi Can", "price": 1.0, "image": "pepsi.png"},
    {"id": 2, "name": "KitKat", "price": 1.0, "image": "kitkat.png"},
    {"id": 3, "name": "Oreo", "price": 1.0, "image": "oreo.png"},
    {"id": 4, "name": "Cheetos", "price": 1.0, "image": "cheetos.png"},
    {"id": 5, "name": "Mentos", "price": 1.0, "image": "mentos.png"},
    {"id": 6, "name": "Galaxy Bar", "price": 1.0, "image": "galaxy.png"},
    {"id": 7, "name": "Water Bottle", "price": 1.0, "image": "water.png"},
    {"id": 8, "name": "Almarai Juice", "price": 1.0, "image": "juice.png"},
]

st.title("Smart Vending Machine")

cols = st.columns(4)

for i, product in enumerate(products):
    col = cols[i % 4]
    with col:
        st.image(product["image"], width=100)
        st.write(f"[{product['id']}] {product['name']}")
        st.write(f"{product['price']} SAR")
        st.write(f"Stock: {st.session_state.quantities[i]}")
        if st.button(f"Buy {product['id']}", key=product['id']):
            if st.session_state.quantities[i] > 0:
                st.session_state.quantities[i] -= 1
                st.success(f"Thank you for purchasing {product['name']}!")
            else:
                st.error(f"{product['name']} is out of stock.")
