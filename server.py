"""
This Flask application serves as an Emotion Detector.
It takes text input, analyzes it for emotions using an external service,
and displays the detected emotion scores and dominant emotion.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Analyzes the emotion of the text provided in the request argument 'textToAnalyze'.

    This function retrieves text from the URL query parameters, calls the
    `emotion_detector` function to analyze it, and then returns a formatted
    string displaying the emotion scores and the dominant emotion.
    If the analysis fails (e.g., invalid text), it returns an error message.

    Returns:
        str: A formatted string displaying the emotion scores and dominant emotion,
             or an error message if the text is invalid or analysis fails.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    emotions_data = emotion_detector(text_to_analyze)

    if emotions_data['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    response_string = (
    f"For the given statement, the system response is "
    f"'anger' : {emotions_data['anger']}, "
    f"'disgust' : {emotions_data['disgust']}, "
    f"'fear' : {emotions_data['fear']}, "
    f"'joy' : {emotions_data['joy']}, "
    f"'sadness' : {emotions_data['sadness']}. "
    f"The dominant emotion is {emotions_data['dominant_emotion']}."
    )
    return response_string@app.route("/")
def render_index_page():
    """
    Renders the index.html template for the home page of the application.

    Returns:
        str: The rendered HTML content of the index.html page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
    