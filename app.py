import streamlit as st
import boto3
import json

# Streamlit UI
st.title("Poem Generator")

# User input for the prompt
user_prompt = st.text_input("Enter your prompt for the poem:")

# Function to invoke the model
def generate_poem(prompt):
    bedrock = boto3.client(service_name="bedrock-runtime")

    payload = {
        "inputText": "[INST]" + prompt + "[/INST]",
        "textGenerationConfig": {
            "maxTokenCount": 512,
            "temperature": 0,
            "topP": 1,
            "stopSequences": []
        }
    }
    body = json.dumps(payload)
    model_id = "amazon.titan-text-express-v1"
    
    response = bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )

    response_body = json.loads(response.get("body").read())
    return response_body['results'][0]['outputText']

# Button to generate the poem
if st.button("Generate Poem"):
    poem = generate_poem(user_prompt)
    st.text_area("Generated Poem", value=poem, height=400)


