Project Overview

Pic2Plate is a web application that generates customized recipes based on images of ingredients uploaded by the user.
The system detects the ingredients in images and creates recipes tailored to a selected cuisine and dietary preferences,
providing a personalized cooking experience.




Features

Image-based ingredient detection: Users can upload 1–10 images (png, jpg, jpeg) of ingredients.
Customizable cuisine selection: Recipes are generated according to the user-selected cuisine (e.g., Indian, Nepali, Middle Eastern, Mexican, Thai).
LLM-powered recipe generation: Uses Google Gemini LLM to create realistic, detailed recipes .
User-friendly interface: Built with Streamlit, allowing easy image upload, cuisine selection, and interactive recipe display.
Error handling & feedback: Alerts users if no images are uploaded or more than 10 are selected.



Tech Stack

Python
Streamlit (Web UI)
PIL (Image processing)
Google Gemini LLM (via genai)
LangChain 



Project Architecture

Users upload ingredient images through the Streamlit interface.
Images are processed using PIL, and ingredient information is extracted.
The base prompt is prepared for the LLM, including user-selected cuisin
Google Gemini LLM generates a recipe using the detected ingredients


1. Install Dependencies
   pip install -r requirements.txt

2. Set API Key
   GOOGLE_API_KEY=your_api_key_here

3.3. Run the App
 streamlit run app.py

   
4. Upload Images & Generate Recipes

Upload 1–10 ingredient images.
Select your preferred cuisine.
Click “Generate Recipe” to get a personalized recipe.



Uploaded Images: tomato.jpg, cheese.jpg, basil.jpg
Cuisine: Italian

Generated Recipe:
Recipe Name: Margherita Pizza
Ingredients: Tomato, Mozzarella Cheese, Basil, Olive Oil, Pizza Dough
Procedure: 1. Preheat oven to 220°C. 2. Spread dough on a tray... (etc.)

