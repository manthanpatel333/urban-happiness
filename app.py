
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

# Read training data from the text file
def load_training_data(file_path):
    training_data = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split("::")
            training_data[key] = value
    return training_data

training_data = load_training_data("training_data.txt")

# Preparing the data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(training_data.keys())
y = list(training_data.values())

# Training the model
model = MultinomialNB()
model.fit(X, y)

def get_response(user_input):
    input_vector = vectorizer.transform([user_input])
    response = model.predict(input_vector)
    return response[0]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    return get_response(user_input)

if __name__ == "__main__":
    app.run(debug=True)
