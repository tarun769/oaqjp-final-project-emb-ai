import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyze):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    data = json.loads(response.text)
    emotions_data = data['emotionPredictions'][0]['emotion']
    anger_score = emotions_data['anger']
    disgust_score = emotions_data['disgust']
    fear_score = emotions_data['fear']
    joy_score = emotions_data['joy']
    sadness_score = emotions_data['sadness']
    dominant_emotion = max(emotions_data, key=emotions_data.get)

    # return anger_score
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }