import streamlit as st
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"
token = os.environ["TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

# Set the title of the app
st.title("Generate your Poem")

# Create a textbox for user input
user_input = st.text_area("Enter your theme or idea for the poem:")

# Submit button
if st.button("Submit"):
    if user_input:
        # Placeholder for the LLM response
        with st.spinner("Generating your poem..."):
            try:
                # Example LLM API Call (replace with actual API)
                response = client.complete(
                            messages=[
                            SystemMessage("You are a helpful assistant."),
                            UserMessage("write a poem on "+user_input),
                        ],
                        temperature=1.0,
                        top_p=1.0,
                        max_tokens=1000,
                        model=model_name
                    )
                poem = response.choices[0].message.content
                
                # Display the output
                st.subheader("Your Generated Poem:")
                st.write(poem)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text to generate a poem.")
