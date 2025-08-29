import requests
import json


def emotion_detector(text_to_analyze):
    """
    Detect emotions in the given text using Watson NLP API.
    
    Args:
        text_to_analyze (str): The text to analyze for emotions
        
    Returns:
        A dictionary containing emotion scores and the dominant emotion
    """
    # Watson API URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input JSON format as specified
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Make the POST request to the Watson API
    response = requests.post(url, headers=headers, json=input_json)
    
    # Convert the response text to a dictionary
    response_dict = json.loads(response.text)
    
    # Extract emotion scores from the response
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    # Extract individual emotion scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Find the dominant emotion (emotion with highest score)
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Return the formatted output
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }


# Testing the emotion detection function
if __name__ == "__main__":
    # Step 1: Import simulation (showing what would be typed in shell)
    print(">>> from emotion_detection import emotion_detector")
    
    # Step 2: Test the application with the given text
    test_text = "I am so happy I am doing this."
    print(f">>> emotion_detector('{test_text}')")
    
    # Step 3: Execute and display the result
    result = emotion_detector(test_text)
    print(result)