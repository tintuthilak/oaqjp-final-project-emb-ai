import requests
import json

def emotion_detector(text_to_analyze : str):
    """
    This function analyzes the emotion in the text provided

    param: text_to_analyze - The text to analyze for emotion
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = input_json, headers=header)
    formatted_response = json.loads(response.text)
    
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    # Find the dominant action with highest score
    max_key = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = max_key

    return emotions

