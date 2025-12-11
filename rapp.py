import streamlit as st
from recipe import generate_recipe_from_images,recipe_audio
from PIL import Image


st.title('AI Recipe Generator From Ingradients Images')
st.markdown('Upload 1 to 10 Ingradient images and let the AI create recipe for you')



with st.sidebar:
    st.header("controls")

    # sidebar option to upload images 

    uploaded_files=st.file_uploader(
        'Upload your files...',
        type=['png','jpg','jpeg'],
        accept_multiple_files=True
    )
    

#     # selecting Select Preference

    Cuisine=st.selectbox(
        'Choose a cuisine',
        ('Indian','Nepali','Middle Eastern','Mexican','Thai')
         )



    # generate recipe type='primary' if chrome theam is dark button color adjest accoring to that color
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
                pil_images=[Image.open(uploaded_files) for uploaded_files in uploaded_files]
                st.subheader('Your ingredients list')
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
            
            
            
                # recipe_audio
                st.subheader(f'Listen to your recipe:')
                audio_file=recipe_audio(generate_recipe)
                if audio_file:
                    st.audio(audio_file,format='audio/mp3')
                    
                
            
            except Exception as e:
                st.error(f'An application error occrred {e}')
                
                 