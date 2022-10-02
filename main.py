from flask import Flask, request, jsonify,render_template
from flask_cors import CORS, cross_origin
import joblib
import pandas as pd

global page
app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('main.html')


@app.route("/LogisticsRegression.html", methods=['GET'])
@cross_origin()
def home_logistics_regression():
    global page
    page='logistics_regression'
    return render_template('LogisticsRegression.html')


@app.route("/RandomForest.html", methods=['GET'])
@cross_origin()
def home_random_forest():
    global page
    page = 'random_forest'
    return render_template('RandomForest.html')

@app.route("/MultinomialNaiveBayes.html", methods=['GET'])
@cross_origin()
def home_multinomial_naive_bayes():
    global page
    page = 'multinomial_naive_bayes'
    return render_template('MultinomialNaiveBayes.html')

@app.route("/classifyNews", methods=['POST'])
@cross_origin()
def predictRoutespeech():
    global page
    data = request.json['data']
    df = pd.DataFrame([{'text': str(data)}])
    if page=='logistics_regression':
        model_load = joblib.load('saved model\LogisticRegression()TfidfVectorizer().pkl')
        transformer_load = joblib.load('saved model\TfidfVectorizer().pkl')
    elif page == 'random_forest':
        model_load = joblib.load('saved model\RandomForestClassifier()CountVectorizer().pkl')
        transformer_load = joblib.load('saved model\CountVectorizer().pkl')
    elif page == 'multinomial_naive_bayes':
        model_load = joblib.load('saved model\MultinomialNB()CountVectorizer().pkl')
        transformer_load = joblib.load('saved model\CountVectorizer().pkl')
    result = model_load.predict(transformer_load.transform(df['text']))


    if (result == 0):
        return jsonify({"Result" : 'BUSINESS'})
    elif (result == 1):
        return jsonify({"Result" : 'ENTERTAINMENT'})
    elif (result == 2):
        return jsonify({"Result" : 'POLITICS'})
    elif (result == 3):
        return jsonify({"Result" : 'SPORTS'})
    elif (result == 4):
        return jsonify({"Result" : 'TECHNOLOGY'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)