import requests

def emotion_detector(text_to_analyze):
    """
    Send the input text to the Watson NLP Emotion Predict API
    and return the raw JSON response as a string.
    """

    # Define the URL for the Emotion Predict function
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Set the headers with the required model ID for the Emotion model
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Create the JSON payload using the text_to_analyze argument
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Make a POST request to the Watson NLP Emotion Predict API
    response = requests.post(url, json=input_json, headers=headers)

    # Return the text attribute of the response object
    return response.text
