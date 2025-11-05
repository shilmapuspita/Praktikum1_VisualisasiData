import streamlit as st


st.title("Praktikum 1 - Visualisasi Data")
st.subheader("Bagian 3: Data Media")
st.markdown("""
1. Shilma Puspita - 0110122038
2. Taufik Hidayat - 0110222093
3. Nurhafidudin - 0110222110
""")
    

st.write("Displaying an Images")
# Displaying Image by specifying path
st.image("assets/meng6.jpeg")
#Image Courtesy by National Wildlife Federation
st.write("Image Courtesy: National Wildlife Federation")


import streamlit as st

# Image Courtesy
st.write("Diplaying Multiple Images")

# Listing out animal images
animal_images = [
    'assets/meng1.jpeg',
    'assets/meng2.jpeg',
    'assets/meng7.jpeg',
    'assets/meng4.jpeg',
    'assets/meng5.jpeg',
]

# Displaying Multiple images with width 150
st.image(animal_images, width=150)

# Image Courtesy
st.write("Image Courtesy: National Wildlife Federation")


import streamlit as st
import base64

# Function to set Image as Background
def add_local_background_image(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())

    st.write("Image Courtesy: National Wildlife Federation")
    st.markdown(
    f""" 
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
   unsafe_allow_html=True
    )

st.write("Background Image")
# Calling Image in function
add_local_background_image('assets/wallpaper.jpg')



import streamlit as st
from PIL import Image

original_image = Image.open("assets/meng4.jpeg")

# Display Original Image
st.title("Original Image")
st.image(original_image)

# Resizing Image to 600*400
resized_image = original_image.resize((600, 400))

# Displaying Resized Image
st.title("Resized Image")
st.image(resized_image)
