import streamlit as st
from recipe import generate_recipe_from_images
from PIL import Image
import streamlit as st

# Load a Google Font (Poppins)
st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;700&display=swap" rel="stylesheet">
    
    <style>
        .title-wordmark {
            font-family: 'Poppins', sans-serif;
            font-size: 55px;
            font-weight: 700;
            text-align: center;
            color: #064e3b; /* Dark green shade */
            letter-spacing: 1px;
        }
        .subtitle {
            font-family: 'Poppins', sans-serif;
            font-size: 20px;
            text-align: center;
            color: #1b4332;
            margin-top: -10px;
        }
    </style>
""", unsafe_allow_html=True)


# Custom Title
st.markdown('<div class="title-wordmark">Pic<span style="color:#10b981;">2</span>Plate</div>', unsafe_allow_html=True)

# Subtitle
st.markdown('<div class="subtitle">Generate recipe from your ingredient images</div>', unsafe_allow_html=True)



st.markdown('Upload 1 to 10 Ingradient images and let the AI create recipe for you')


st.write("")  # small spacing

#----------------------------------------------------------------------------

with st.sidebar:
    st.header("controls")

    # sidebar option to upload images 

    uploaded_files=st.file_uploader(
        'Upload your files...',
        type=['png','jpg','jpeg'],
        accept_multiple_files=True
    )
    

#     # selecting Select cuision

    Cuisine=st.selectbox(
        'Choose a cuisine',
        ('Indian','Nepali','Middle Eastern','Mexican','Thai')
         )

    generate_button=st.button('Generate recipe',type='primary')



# main logic

if generate_button:
    if not uploaded_files:#( if no image file upload in upload file)
        st.warning('please upload atlest 1 image!') # then show this 
    elif len(uploaded_files)>10:
        st.warning('please upload an maximum of 10 images')
    else:
         with st.spinner('The AI is creating your recipe..... This may take few moments'):
             
            try:
                pil_images=[Image.open(img_files) for img_files in uploaded_files]
                st.subheader('Your ingredients')
                image_columns=st.columns(len(pil_images))
                
                
                for i ,image in enumerate(pil_images):
                    with image_columns[i]:
                        st.image(image,use_container_width=True)
            
                generate_recipe=generate_recipe_from_images(pil_images,Cuisine)  
                if 'Error'in generate_recipe or 'failed' in generate_recipe or 'API key' in generate_recipe:
                  
                   st.error(generate_recipe)
                else:
                   st.subheader(f'Your {Cuisine} recipe:')
                   st.success(generate_recipe)
            
            
                
            
            except Exception as e:
                st.error(f'An application error occrred {e}')
                
                 