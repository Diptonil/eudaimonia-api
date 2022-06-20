from nrclex import NRCLex 


def get_emotions(text, emotion_list_preprocessed):
    emotion = NRCLex(text)
    for element in emotion.top_emotions:
        emotion_tag = element[0]
        if emotion_tag == 'anticip':
            emotion_tag = 'anticipation'
        emotion_list_preprocessed[emotion_tag] += float(element[1])


def clean_output(emotion_list_preprocessed):
    emotion_list_processed = dict()
    if emotion_list_preprocessed['joy'] != 0:
        emotion_list_processed['joy'] = emotion_list_preprocessed['joy']
    if emotion_list_preprocessed['disgust'] != 0:
        emotion_list_processed['disgust'] = emotion_list_preprocessed['disgust']
    if emotion_list_preprocessed['sadness'] != 0:
        emotion_list_processed['sadness'] = emotion_list_preprocessed['sadness']
    if (emotion_list_preprocessed['surprise'] != 0) and (emotion_list_preprocessed['surprise'] > emotion_list_preprocessed['anticipation']):
        emotion_list_processed['surprise'] = emotion_list_preprocessed['surprise']
    if (emotion_list_preprocessed['negative'] != 0) and (emotion_list_preprocessed['positive'] < emotion_list_preprocessed['negative']):
        emotion_list_processed['negative'] = emotion_list_preprocessed['negative']
    if (emotion_list_preprocessed['positive'] != 0) and (emotion_list_preprocessed['positive'] > emotion_list_preprocessed['negative']):
        emotion_list_processed['positive'] = emotion_list_preprocessed['positive']
    if (emotion_list_preprocessed['trust'] != 0) and (emotion_list_processed.get('surprise', None) is None):
        emotion_list_processed['trust'] = emotion_list_preprocessed['trust']
    if (emotion_list_preprocessed['anticipation'] != 0) and (emotion_list_preprocessed['surprise'] < emotion_list_preprocessed['anticipation']):
        emotion_list_processed['anticipation'] = emotion_list_preprocessed['anticipation']
    if emotion_list_preprocessed['fear'] != 0:
        emotion_list_processed['fear'] = emotion_list_preprocessed['fear']
    if emotion_list_preprocessed['anger'] != 0:
        emotion_list_processed['anger'] = emotion_list_preprocessed['anger']
    return emotion_list_processed
         

def predict_mood(corpus):
    sentences = (corpus).split(sep='.')
    sentences = [sentence.strip() for sentence in sentences]
    emotion_list_preprocessed = {'joy': 0, 'disgust': 0, 'sadness': 0, 'surprise':0, 'negative': 0, 'positive': 0, 'trust': 0, 'anticipation': 0, 'fear': 0, 'anger': 0}
    for sentence in sentences:
        get_emotions(sentence, emotion_list_preprocessed)
    emotion_list_processed = clean_output(emotion_list_preprocessed)
    return emotion_list_processed
