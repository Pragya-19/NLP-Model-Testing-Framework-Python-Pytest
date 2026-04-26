from nlp_model.sentiment_model import predict_sentiment


def test_positive_sentiment():
    result = predict_sentiment("I am very happy today")
    assert result == "positive"


def test_negative_sentiment():
    result = predict_sentiment("This is a terrible product")
    assert result == "negative"


def test_neutral_sentiment():
    result = predict_sentiment("I am going to the market")
    assert result == "neutral"
