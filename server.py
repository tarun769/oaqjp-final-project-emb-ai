from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    emotions_data = emotion_detector(text_to_analyze)

    anger_score = str(emotions_data['anger'])
    disgust_score = str(emotions_data['disgust'])
    fear_score = str(emotions_data['fear'])
    joy_score = str(emotions_data['joy'])
    sadness_score = str(emotions_data['sadness'])
    dominant_emotion = str(max(emotions_data, key=emotions_data.get))


    # Return a formatted string with the sentiment label and score
    return "For the given statement, the system response is {}:{},{}:{},{}:{},{}:{} and {}:{}. The dominant emotion is {}.".format('anger', anger_score, 'disgust', disgust_score, 'fear', fear_score, 'joy', joy_score, 'sadness', sadness_score, dominant_emotion)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5002)