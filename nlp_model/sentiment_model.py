def predict_sentiment(text):
    positive_words = ["happy", "good", "great", "excellent", "love"]
    negative_words = ["bad", "sad", "hate", "terrible", "poor"]

    text = text.lower()

    if any(word in text for word in positive_words):
        return "positive"

    if any(word in text for word in negative_words):
        return "negative"

    return "neutral"
