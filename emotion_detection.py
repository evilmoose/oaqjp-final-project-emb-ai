import requests
import json

def emotion_detection(text_to_analyse):
    """ function to run emotion detection 
        using the appropriate Emotion Detection function.
    """

    # Endpoint of the Watson Emotion Detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Header specifying the model ID for the emotion detection service
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Request payload in the expected format
    data = { "raw_document": { "text": text_to_analyse } }

    # Sending a POST request to the emotion detection API
    response = requests.post(url, json=data, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extract emotion predictions
    emotions = formatted_response.get('emotionPredictions', [])[0].get('emotion', {})

    # Extract required emotions and their scores
    required_emotions = {
        'anger': emotions.get('anger', 0),
        'disgust': emotions.get('disgust', 0),
        'fear': emotions.get('fear', 0),
        'joy': emotions.get('joy', 0),
        'sadness': emotions.get('sadness', 0),
    }
   
    return required_emotions