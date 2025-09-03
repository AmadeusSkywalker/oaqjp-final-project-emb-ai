"""
Flask server for EmotionDetection web application.

This server provides a web interface for the emotion detection service.
It handles requests from the frontend and returns formatted emotion analysis results.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Create Flask application
app = Flask(__name__)


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Analyze the provided text for emotions.
    
    This endpoint accepts a GET request with a 'textToAnalyze' parameter,
    processes it through the emotion detector, and returns a formatted response.
    """
    # Get the text from the request
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Check if text was provided
    if not text_to_analyze:
        return "Please provide text to analyze."
    
    # Call the emotion_detector function from the package
    result = emotion_detector(text_to_analyze)
    
    # Format the response as per customer requirements
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    
    return response


if __name__ == '__main__':
    # Run the Flask app on localhost:5000
    app.run(host='0.0.0.0', port=5000, debug=True)