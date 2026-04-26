from nlp_model.sentiment_model import predict_sentiment


def test_empty_input():
    result = predict_sentiment("")
    assert result == "neutral"


def test_numeric_input():
    result = predict_sentiment("12345")
    assert result == "neutral"
