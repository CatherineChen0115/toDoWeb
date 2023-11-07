import streamlit as st
from PIL import Image #Pillow?

with st.expander("Start Camera"):
    #start the camera
    camera_image = st.camera_input("Camera") #browser will ask for permitsion
    print(camera_image)

    if camera_image:
        # create a pilow image instance
        img = Image.open(camera_image)
        
        #convert the pillow image
        gray_img = img.convert("L")
        
        #render the grayscale image on the webpage
        st.image(gray_img)