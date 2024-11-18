# import streamlit as st
# from langchain_community.llms import Ollama  # Updated import
# from langchain.prompts import PromptTemplate
# import base64
# from PIL import Image
# import io

# # Initialize the Llama Vision model
# llama_vision = Ollama(model="llama3.2-vision")

# # Define the prompt template for handling image and text queries
# default_prompt = "Analyze this image content and answer the query: {query}"

# def process_image_query(query: str, image_base64: str, prompt: str):
#     # Format the prompt with the provided query
#     formatted_prompt = prompt.format(query=query)

#     # Query the model with the formatted prompt
#     response = llama_vision(formatted_prompt, images=[image_base64])  # Pass formatted prompt and image
#     return response

# # Streamlit UI
# st.title("Llama Vision Image Analysis")
# st.write("Upload an image and enter a query to analyze its content.")

# # Input field for custom prompt
# prompt_template = st.text_area("Prompt Template", default_prompt, height=100)
# query = st.text_input("Enter your query:", "What objects are in this image?")

# # Upload image
# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# if uploaded_file and query:
#     # Read image and convert to RGB if it has an alpha channel
#     image = Image.open(uploaded_file)
#     if image.mode == 'RGBA':
#         image = image.convert("RGB")

#     # Convert image to base64
#     buffered = io.BytesIO()
#     image.save(buffered, format="JPEG")
#     image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

#     # Display the uploaded image
#     st.image(image, caption="Uploaded Image", use_container_width=True)

#     # Analyze the image and display results
#     if st.button("Analyze Image"):
#         response = process_image_query(query, image_base64, prompt_template)
#         st.write("### Response:")
#         st.write(response)
import streamlit as st
from langchain_community.llms import Ollama  # Updated import
import base64
from PIL import Image
import io

# Initialize the Llama Vision model
llama_vision = Ollama(model="llama3.2-vision")

# Define the prompt template for handling image and text queries
default_prompt = "Analyze this image content and answer the query: {query}"

def process_image_query(query: str, image_base64: str, prompt: str):
    # Format the prompt with the provided query
    formatted_prompt = prompt.format(query=query)

    # Query the model with the formatted prompt
    response = llama_vision(formatted_prompt, images=[image_base64])  # Pass formatted prompt and image
    return response

# Streamlit UI
st.title("Llama Vision Image Analysis")
st.write("Upload an image and enter a query to analyze its content.")

# Input field for query
query = st.text_input("Enter your query:", "What objects are in this image?")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=None)  # Accept all types of images

if uploaded_file and query:
    # Read image and convert to RGB if it has an alpha channel
    image = Image.open(uploaded_file)
    if image.mode == 'RGBA':
        image = image.convert("RGB")

    # Convert image to base64
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Analyze the image and display results
    if st.button("Analyze Image"):
        response = process_image_query(query, image_base64, default_prompt)
        st.write("### Response:")
        st.write(response)
