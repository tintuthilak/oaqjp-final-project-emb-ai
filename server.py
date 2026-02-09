from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

def get_formatted_response(data) :
    dominant = data.get("dominant_emotion")

    emotion_wo_dominant = {emotion: score for emotion, score in data.items() if emotion != "dominant_emotion"}
    emotions_list = list(emotion_wo_dominant.items())
    emotions = [f"'{emotion}': {score}" for emotion, score in emotions_list[:-1]]
    emotions.append(f"'{emotions_list[-1][0]}': {emotions_list[-1][1]}")

    score_text = ", ".join(emotions[:-1]) + " and " + emotions[-1] if len(emotions) > 1 else emotions[0]
    
    result = (
        f"For the given statement, the system response is {score_text}. "
        f"The dominant emotion is {dominant}."
    )

@app.route("/emotionDetector")
def sent_analyzer():
    ''' 
    This function receives the text from the HTML interface and 
    runs emotion detection over the text.
    The output returned shows the emotions with its confidence 
    score and the dominant emotion for the provided text.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid Input!!!!"

    return get_formatted_response(response)

@app.route("/")
def render_index_page():
    ''' 
    Renders the main application page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)