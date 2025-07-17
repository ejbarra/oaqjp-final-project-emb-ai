"""
Flask application for emotion detection analysis.

"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize Flask application
app = Flask("emotionDetector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze emotions in the provided text.

    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Call the emotion_detector function to analyze the text
    response = emotion_detector(text_to_analyze)
    # Extract the dominant_emotion from the response
    dominant_emotion = response['dominant_emotion']
    # Check if the dominant_emotion is None (indicates error or invalid input)
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    # Format the response according to the specified requirements
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is **{response['dominant_emotion']}**."
    )
    return formatted_response
@app.route("/")
def render_index_page():
    """
    Render the main index page.
    
    This function serves the main HTML interface for the emotion detection
    application.
    """
    return render_template('index.html')


def main():
    """
    Main function to run the Flask application.

    """
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
