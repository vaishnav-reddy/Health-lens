import streamlit as st
import google.generativeai as genai

# ✅ Use the API key from Streamlit secrets
genai.configure(api_key=st.secrets["api_key"])

# Generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

system_prompts = [
    """

You are an experienced medical expert with specialized skills in image analysis, working for a prestigious hospital. Your role is pivotal in identifying anomalies, diseases, or health concerns within medical images.

Your duties include:  

1. **Thorough Examination:** Carefully analyze each medical image, emphasizing the detection of irregularities or potential health issues.  
2. **Observation Report:** Record all findings systematically, detailing any abnormalities or indications of illness.  
3. **Next Steps and Advice:** Recommend follow-up actions, such as additional tests or evaluations, based on your observations.  
4. **Lifestyle Recommendations:** Provide clear and actionable dos and don’ts for maintaining or improving health.  
        - **Dos:** Highlight healthy habits, exercises, or routines that may benefit the user.  
        - **Don’ts:** Caution against harmful practices, habits, or behaviors that may worsen their condition.
        - **Food:** What type of food to take and avoid   

5. **Treatment Recommendations:** Where applicable, suggest potential treatment options or interventions to address identified issues

**Key Considerations:**  

1. **Image Relevance:** Ensure your response focuses solely on images related to human health concerns only.  
2. **Image Quality:** If the image lacks clarity or is insufficient for a definitive evaluation, note that certain details are "Indeterminate due to image quality."  
3. **Disclaimer:** Always include the disclaimer: "Consult with a doctor before making any further decisions."  
4. **Structured Response:** Present your analysis under the following headings:  
   - Detailed Analysis  
   - Analysis Report  
   - Recommendations 
   - Treatments  

Your expertise is critical in guiding informed decisions. Please proceed with precision and adherence to this framework.  

"""
]


# Initialize Gemini model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Streamlit UI
st.set_page_config(page_title="Medical Assistant", page_icon="🩺")

st.markdown(
    """
    <style>

    /* Step 1: Set the overall dark theme */
    body {
        background-color: #121212;
        color: #e0e0e0;
    }

    /* Step 2: Header section styling */
    .main-header {
        text-align: center;
        padding: 2rem;
        background: rgba(30, 30, 46, 0.8);
        border-radius: 10px;
        margin-bottom: 2rem;
    }

    .main-header h1 {
        color: #4A90E2;
        font-size: 3rem;
        font-weight: 700;
    }

    .main-header h2 {
        color: #e0e0e0;
        font-size: 1.5rem;
    }

    /* Step 3: Chat history message box */
    .chat-history {
        padding: 15px;
        background-color: #1E1E2E;
        border-radius: 10px;
        color: #e0e0e0;
        margin-bottom: 15px;
    }

    /* Step 4: Footer styling */
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        background: rgba(30, 30, 46, 0.8);
        border-radius: 10px;
    }

    .footer p {
        color: #e0e0e0;
        font-size: 0.9rem;
    }

</style>

    """,
    unsafe_allow_html=True
)

# App Header
st.markdown("""
    <div class="main-header">
        <h1>HealthLens 🩺</h1>
        <h2>AI That Makes Diagnosis Smarter and Faster.</h2>
    </div>
""", unsafe_allow_html=True)

# Upload image
st.markdown("### Upload an Image")
file_uploaded = st.file_uploader("Upload the image for Analysis", type=["png", "jpg", "jpeg"])

# Open camera button
if "show_camera" not in st.session_state:
    st.session_state.show_camera = False

if st.button("📸 Open Camera"):
    st.session_state.show_camera = True

# Camera input
if st.session_state.show_camera:
    st.markdown("### 📸 Take a Photo")
    camera_image = st.camera_input("", key="camera_input")

# Show image preview
if file_uploaded:
    st.image(file_uploaded, width=200, caption="Uploaded Image")
    image_data = file_uploaded.getvalue()
elif "camera_image" in st.session_state and st.session_state.camera_image:
    st.image(st.session_state.camera_image, width=200, caption="Captured Image")
    image_data = st.session_state.camera_image.getvalue()
else:
    image_data = None

# Generate Analysis
if st.button("Generate Analysis") and image_data:
    image_parts = [{"mime_type": "image/jpg", "data": image_data}]
    prompt_parts = [image_parts[0], system_prompts[0]]
    response = model.generate_content(prompt_parts)
    if response:
        st.title("Detailed analysis based on the uploaded image")
        st.write(response.text)

# Sidebar Chatbot
st.sidebar.title("Chatbot Assistant 💬")
st.sidebar.write("Ask any medical-related questions about Human, Animal, and Plant Health.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.sidebar.form(key="chat_form", clear_on_submit=True):
    user_query = st.text_input("Type your question here:")
    submit_query = st.form_submit_button("Ask")

if submit_query and user_query:
    chatbot_prompt = f"""
    You are a friendly and knowledgeable medical assistant...
    (your chatbot prompt here)
    User Query: {user_query}
    """
    chat_response = model.generate_content([chatbot_prompt])
    if chat_response:
        st.session_state.chat_history.append({"user": user_query, "bot": chat_response.text})
    else:
        st.session_state.chat_history.append({"user": user_query, "bot": "Sorry, I couldn't process your query."})

# Display chat history
if st.session_state.chat_history:
    st.sidebar.write("### Chat History:")
    for chat in st.session_state.chat_history:
        st.sidebar.markdown(f"<div class='chat-history'><strong>You:</strong> {chat['user']}<br><strong>Kairos:</strong> {chat['bot']}</div>", unsafe_allow_html=True)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("**Note:** Always consult a doctor for specific concerns.")
st.markdown("""
    <div class="footer">
        <p>Made with ❤️ for Healthcare</p>
    </div>
""", unsafe_allow_html=True)

# python -m streamlit run medico.py
