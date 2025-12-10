""" Flask web server for the Emotion Detection application. 
It provides an endpoint that accepts user text, calls the
emotion detection logic, and formats the output in a readable form.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)
@app.route("/")
def index_page():
    """
    Render the main web interface for the Emotion Detection application.Returns:
        HTML page: The index.html file.
    """
    return render_template("index.html")
@app.route("/emotionDetector")
def detect_emotion():
    """
    Handle emotion detection requests coming from the front-end. 
    Extracts the text from query parameters, runs emotion analysis,
    formats the output, and handles invalid cases.
    Returns:
        str: Text output describing emotion scores and dominant emotion.
             Or an error message if the input is invalid.
    """
    # Extract text from request
    text_to_analyze = request.args.get("textToAnalyze")
    # Run the emotion detection logic
    result = emotion_detector(text_to_analyze)
    # Check for invalid input (dominant_emotion == None)
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    # Extract the emotion scores
    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]
    # Format the output string
    response_text = (
        f"For the given statement, the system response is: "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )
    return response_text
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
