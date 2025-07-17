from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    emotions_data = emotion_detector(text_to_analyze)

    # anger_score = emotions_data['anger']
    # disgust_score = emotions_data['disgust']
    # fear_score = emotions_data['fear']
    # joy_score = emotions_data['joy']
    # sadness_score = emotions_data['sadness']
    # dominant_emotion = max(emotions_data, key=emotions_data.get)


    # Return a formatted string with the sentiment label and score
    return "For the given statement, the system response is {}.".format(emotions_data)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)