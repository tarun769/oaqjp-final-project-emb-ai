import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using a Watson NLP API.

    Args:
        text_to_analyze (str): The text content to be analyzed for emotions.

    Returns:
        dict: A dictionary containing the scores for 'anger', 'disgust',
              'fear', 'joy', 'sadness', and the 'dominant_emotion'.
              Returns None for all emotions if the API call fails.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    data = json.loads(response.text)
    emotions_list = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']
    emotion_dict = {}

    for key in emotions_list:
        if response.status_code == 400:
            emotion_dict[key] = None
        else:
            emotions_data = data['emotionPredictions'][0]['emotion']
            if key == 'dominant_emotion':
                emotion_dict['dominant_emotion'] = max(emotions_data, key=emotions_data.get)
            else:
                emotion_dict[key] = emotions_data[key]

    return emotion_dict