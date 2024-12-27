import streamlit as st
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

st.set_page_config(layout='centered')
st.title('Dominate Color in Image')


uploaded_file = st.file_uploader("Choose a file", label_visibility='hidden')

def upload(file):
    if uploaded_file is not None:
        imag = Image.open(uploaded_file)
        img = plt.imread(uploaded_file)
        st.image(imag)
        
        X = img.reshape(-1,3)
        
        kmeans = KMeans(n_clusters=3)
        return kmeans.fit(X)
        
    else:
        st.warning('Image not uploaded')
    
kmeans = upload(uploaded_file)
   
st.header('Display Top 3 Dominate Color')
    
def create_color_palette(dominant_colors, palette_size=(300, 50)):
    # Create an image to display the colors
        palette = Image.new("RGB", palette_size)
        draw = ImageDraw.Draw(palette)

        # Calculate the width of each color swatch
        swatch_width = palette_size[0] // len(dominant_colors)

        # Draw each color as a rectangle on the palette
        for i, color in enumerate(dominant_colors):
            draw.rectangle([i * swatch_width, 0, (i + 1) * swatch_width, palette_size[1]], fill=tuple(color))

        return st.image(palette)
    
create_color_palette(kmeans.cluster_centers_.astype(int))
