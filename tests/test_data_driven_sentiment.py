import csv
from nlp_model.sentiment_model import predict_sentiment


def load_test_data():
    with open("test_data/sentiment_test_data.csv", "r") as file:
        reader = csv.DictReader(file)
        return list(reader)


def test_sentiment_from_csv():
    data = load_test_data()

    for row in data:
        result = predict_sentiment(row["text"])
        assert result == row["expected_sentiment"]
