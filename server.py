from flask import Flask, render_template, request, json
from EmotionDetection.emotion_detection import emotion_detection 

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector():
    """
    This route handles the emotion detection for a given text.
    """
    # Get the 'textToAnalyze' parameter from the request
    text_to_analyze = request.args.get('textToAnalyze', '')

    # Call the emotion detection function
    result = emotion_detection(text_to_analyze)

    # Convert JSON string to Python dictionary
    result_dict = json.loads(result)

    # Format the response
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result_dict['anger']}, "
        f"'disgust': {result_dict['disgust']}, "
        f"'fear': {result_dict['fear']}, "
        f"'joy': {result_dict['joy']} and "
        f"'sadness': {result_dict['sadness']}. "
        f"The dominant emotion is {result_dict['dominant_emotion']}."
    )

    return formatted_response

@app.route("/")
def render_index_page():
    '''
    This function initiates the rendering of the main application
    page over the Flask channel.
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5003, debug=True)