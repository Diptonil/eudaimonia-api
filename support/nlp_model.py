import text2emotion
import pandas
import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


def predict_mood(corpus):
    result = text2emotion.get_emotion(corpus)
    result['Fear'] /= 4
    result['Angry'] += 0.09
    return result


def predict_emotion(corpus):
    dataset = pandas.read_csv('support/isear.csv', header=None, names=('Emotion', 'Text', 'NaN'))
    dataset.drop(dataset.columns[2], axis=1, inplace=True)
    stemmer = PorterStemmer()
    words = stopwords.words('english')
    dataset['Cleaned'] = dataset['Text'].apply(lambda x: " ".join([stemmer.stem(i) for i in re.sub('[^a-zA-Z]', ' ', x).split() if i not in words]).lower())
    vectorizer = TfidfVectorizer(min_df=3, stop_words='english', sublinear_tf=True, norm='l2', ngram_range=(1, 2))
    final_features = vectorizer.fit_transform(dataset['Cleaned']).toarray()
    x = dataset['Cleaned']
    y = dataset['Emotion']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    pipeline = Pipeline([('vect', vectorizer), ('chi', SelectKBest(chi2, k=1200)), ('clf', LogisticRegression(random_state=0, max_iter=200))])
    pipeline.fit(x_train, y_train)
    return {'emotion': pipeline.predict([corpus])[0], 'accuracy': pipeline.score(x_test, y_test)}
