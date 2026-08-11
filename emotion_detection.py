import requests
import json

def emotion_detector(text_to_analyze):
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload= { "raw_document": { "text": text_to_analyze } }

    r = requests.post(URL, headers=headers, json=payload)

    if r.status_code == 200:
        result = r.json()
        
        emotions = result["emotionPredictions"][0]["emotion"]
        
        output = {
            "anger": emotions.get("anger", 0),
            "disgust": emotions.get("disgust", 0),
            "fear": emotions.get("fear", 0),
            "joy": emotions.get("joy", 0),
            "sadness": emotions.get("sadness", 0),
        }
        dominant = max(output, key=output.get)
        output["dominant_emotion"] = dominant

        return output
    else:
        return ({"Message":"Request failed"}, r.status_code)
