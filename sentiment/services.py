from transformers import pipeline

# Load the pre-trained sentiment analysis model from Hugging Face
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]  # Get the first result
    return {"label": result["label"], "score": result["score"]}
