
# Vital Image Analytics – Medical Image Analysis Website

A Streamlit‑based web application that uses Google's **Gemini 1.5** generative AI to assist in medical image analysis.

## Overview
Vital Image Analytics allows users to upload medical images and receive structured, AI‑generated insights.  
It provides a findings report, suggested next diagnostic steps, and includes safety disclaimers.  
This app is intended **for educational and demonstration purposes only** and is **not a medical device**.

## Features
- **Upload & Display Images**: Users can upload PNG, JPG, or JPEG files directly in the browser.
- **AI‑Powered Analysis**: Leverages Google's Gemini 1.5 multimodal model to:
  - Detect possible anomalies or diseases
  - Provide a structured findings report
  - Suggest next diagnostic steps or treatment options (informational only)
- **Safety Guardrails**:
  - Configured safety settings to reduce harmful or irrelevant outputs.
  - Automatic inclusion of a medical disclaimer.

## Tech Stack
- **Frontend & Backend**: [Streamlit](https://streamlit.io)
- **AI Engine**: [Google Generative AI – Gemini 1.5](https://ai.google.dev/)
- **Image Handling**: Pillow (PIL)
- **Environment**: Python 3.11+ with Conda or venv

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Medicle-Image-Analysis-Website.git
   cd Medicle-Image-Analysis-Website
   ```
2. Create and activate a conda environment:
   ```bash
   conda create -n medimage python=3.11
   conda activate medimage
   ```
3. Set your Google API key (replace with your own key):
   ```bash
   export GOOGLE_API_KEY="your_api_key_here"
   ```
   Or create a `.env` file containing:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage Notes
- Upload a medical image.
- Click **Run the analysis** to get AI-generated findings.
- **Important**: This tool is **not a substitute for professional medical advice**.  
  Always consult a qualified doctor for any medical concerns.

