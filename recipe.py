from dotenv import load_dotenv
from google import genai
import os
from http.client import responses
load_dotenv()


api_key=os.getenv('GOOGLE_API_KEY')

if not api_key:
    raise ValueError('API key is not found')

client=genai.Client(api_key=api_key)




# creating a funcation 
# when so in app.py (user uploded) image that will pass in funcation
# and Selected diet Preference pass in funcation
# and the funcation will return recipe generate  from that




    # base prompt
    
base_prompt=f"""You are a recipe creation AI. You must follow these rules strictly

1.The recipe must use all ingredients shown in the uploaded images.
- If only one image is uploaded, that ingredient is the main ingredient.

2.The recipe must strictly match the Cuisine selected by the user(Cuisine)ONLY.
-Only generate recipes from the selected Cuisine STRICTLY,with detailed cooking steps

3.The recipe must be realistic and truly belong to the selected Cuisine ONLY.

4.Output format exactly like this strictly(in the selected language ONLY):

Recipe Name:

Ingredients:

Procedure:


    """

 

def generate_recipe_from_images(images,Cuisine):
    response=client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[images,Cuisine,base_prompt]

    )
    return response.text
print(f'recipe {generate_recipe_from_images}')


