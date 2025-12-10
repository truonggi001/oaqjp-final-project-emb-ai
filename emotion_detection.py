import requests
import json

def emotion_detector(text_to_analyze):
    """
    Send the input text to the Watson NLP Emotion Predict API,format the response, and return a dictionary containing the scores for each emotion and the dominant emotion.
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
    # Convert the response text into a Python dictionary
    response_dict = json.loads(response.text)
    # Extract the emotion scores from the response dictionary
    emotions = response_dict["emotionPredictions"][0]["emotion"]
    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]
    # Determine the dominant emotion (the emotion with the highest score)
    dominant_emotion = max(
        emotions,
        key=emotions.get
    )
    # Return the formatted output dictionary
    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
    }
