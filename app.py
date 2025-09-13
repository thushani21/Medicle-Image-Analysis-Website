import streamlit as st
import os
from pathlib import Path

API_KEY = os.getenv("AIzaSyDXT_C4XzzWu9I38H1g1KiczYgkMJiQroM")
if not API_KEY:
    try:
        from api_key import api_key as API_KEY 
    except Exception:
        API_KEY = None

import google.generativeai as genai

#setup
generation_config = {
    "temperature" : 0.4,
    "top_p" : 1,
    "top_k" : 32,
    "max_output_tokens" : 4096,
}

#apply safety settings
safety_settings =[
    {
        "category" : "HARM_CATEGORY_HARASSMENT",
        "threshold" : "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category" : "HARM_CATEGORY_HATE_SPEECH",
        "threshold" : "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category" : "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold" : "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category" : "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold" : "BLOCK_MEDIUM_AND_ABOVE"
    },
]

system_prompt=""" As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining medical images for a renowned hospital. Your expertise is crucial for identifying any anomalies, diseases, or other health issues that may be present.

Responsibilities
1.Detailed analysis: Thoroughly analyze each image, focusing on identifying any abnormal findings.
2.Findings report: Document all observed anomalies or signs of disease, and clearly present these findings in a structured format.
3.Recommendations & next steps: Based on your analysis, suggest next steps, including further tests or treatments as applicable.
4.Treatment suggestions: If appropriate, recommend possible treatment options or interventions.

Important notes
1.Scope of response: Only respond if the image pertains to human health issues.
2.Clarity of images: If image quality limits assessment, state: “Unable to determine certain aspects based on the provided image.”
3.Disclaimer: Include: “Consult with a doctor before making any decisions. Your insights are invaluable in guiding clinical decisions.”

provide me an output resposnse with these headings: Detailed analysis, Findings report, Recommendations & next steps, Treatment suggestions
"""

#model config
model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

st.set_page_config(page_title="vital image analytics", page_icon=":robot")

#title
st.title("ViTal ImaGE AnaLyTicS 👨🏼‍⚕ 💊 💉")
st.subheader("An app for medical image identification ")

uploaded_file = st.file_uploader("Uplaod an Image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    st.image(uploaded_file, width=300, caption="Uploaded Medical Image")
submit_button = st.button("Run the analysis")

if submit_button:
    if uploaded_file is None:
        st.warning("Please upload an image first.")
        st.stop()

    #uploaded image
    image_data = uploaded_file.getvalue()

    image_parts = [
        {
            "mime_type": "image/jpeg",
            "data": image_data
        }
    ]

    prompt_parts = [
        image_parts[0],
        system_prompt,
    ]

    #generate response
    response = model.generate_content(prompt_parts)
    if response:
        st.title("Here is the analysis based on your uploaded image: ")
        st.write(response.text)



