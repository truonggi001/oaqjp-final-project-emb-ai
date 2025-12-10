from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():    
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    # Retrieve text entered by the user
    text_to_analyze = request.args.get("textToAnalyze")
    # Get the emotion analysis result
    result = emotion_detector(text_to_analyze)
    # Extract emotion scores
    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]
    # Format the output as required in the task
    response_text = (
        f"For the given statement, the system response is: "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )
    return response_text

if __name__ == "__main__":
    # Run on port 5000 exactly as required by the lab
    app.run(host="0.0.0.0", port=5000)
