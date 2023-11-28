import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=input_json, headers=header)
    
    if response.status_code == 500:
        emotions = {
            'anger': None,
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None}
        return emotions
    elif response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        emotions_name = [key for key in emotions.keys()]
        scores = [value for value in emotions.values()]
        dominant = emotions_name[scores.index(max(scores))]
        emotions['dominant_emotion'] = dominant
        return emotions
 

# from emotion_detection import emotion_detector
# emotion_detector("I love this new technology")
