from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/emotionDetector")
def sent_detector():
    """
    This gets the text from the user and detects the emotion
    """

    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    print(response)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dom_emotion = response['dominant_emotion']

    if dom_emotion == None:
        return "Invalid input, please try again!"

    return f"For the given statement, the system response is \
            'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, \
            'joy': {joy}, and 'sadness': {sadness}. The dominant \
            emotion is {dom_emotion}."

@app.route("/")
def render_index_page():
    """
    Send the index.html to the user.
    """

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
