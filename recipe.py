from dotenv import load_dotenv
from google import genai
load_dotenv
import os
from gtts import gTTS#( FOR AUDIO)
from io import BytesIO

load_dotenv()


api_key=os.getenv('GOOGLE_API_KEY')

if not api_key:
    raise ValueError('API akeey is not found')

client=genai.Client(api_key=api_key)




# creating a funcation 
# when so in app.py (user uploded) image that will pass in funcation
# and Selected diet Preference pass in funcation
# and the funcation will return recipe generate  from that




    # base prompt
    
base_prompt=f"""You are an expert recipe creator AI. Your job is to analyze
the ingredients shown in the uploaded images and Cuisine selected by user in Cuisine selcted box and generate one
complete recipe based Cuisine selcted box and uploaded images only.
Your Main Goal 
Your Task 
1. Use Every Image:Recipe must use all ingredients shown in the images.
2. If only one image is uploaded, that ingredient becomes the main ingredient of the recipe.
3. The recipe must strictly match the user-selected Cuisine (Indian, Italian, Nepali, Middle Eastern, Mexican, Thai,only).
4. Create exactly one recipe that uses every ingredient and asper Cuision.
5. Output Format:
   Recipe Name: (Give actual recipe name as per Cuisine)
   Cuisine:(Must match the user-selected cuisine)
   Ingredients:(List all ingredients identified from images)
   Step-by-Step instructions:(Detailed steps to cook the recipe)
6. The recipe must be realistic and truly belong to the cuisine selected by the user.
7. If any ingredient is unclear in the images, make a reasonable guess that fits the Cuisine.
9. only create recipe from user selcted box Cuision only 
    **Output Format:** Recipe name :
                       Cuision:
                       Ingredients:
    """

    






def generate_recipe_from_images(images,Cuisine):
    response=client.models.generate_content(
    model='gemini-2.5-flash-lite',
    contents=[images,Cuisine,base_prompt]

    )
    return response.text


# function ---> recipe ---> audio file

def recipe_audio(recipe_text):
    try:
        tts=gTTS(text=recipe_text,lang="en",slow=False)
        audio_fp=BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0) # start recipe audio from start
        return audio_fp
    except Exception as e:
        return f" An unexpected error occured during the API call"
    

