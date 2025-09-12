from flask import Flask, render_template, request
import pickle

# Load saved model and vectorizer
model = pickle.load(open("language_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""
    if request.method == "POST":
        text = request.form["user_text"]
        text_vec = vectorizer.transform([text])
        result = model.predict(text_vec)[0]
        prediction = f"Predicted Language: {result}"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
