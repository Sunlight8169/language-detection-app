# Project Description Example:
## Language Detection App 📝🌐

### Description:
This is a learning project for language detection. The app can detect the language of any text input by the user and show which language it belongs to.

### Features:

Uses Multinomial Naive Bayes (MultinomialNB) model from scikit-learn.

Uses CountVectorizer from sklearn.feature_extraction.text to convert text into features.

Trained on sample dataset and achieved 95% accuracy.

Simple frontend with one input box for user to type/paste text.

### Files in this repository:

app.py → Main backend code using Flask, loads the model and returns prediction.

model.pkl → Trained MultinomialNB model saved using joblib.

templates/index.html → Simple frontend with input box for user text.

requirements.txt → Python packages required for running the app.

### How it works:

User enters text in the input box.

Flask backend receives the text.

Text is converted into feature vector using CountVectorizer.

Model predicts the language.

Prediction is returned to user.
