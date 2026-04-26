from nlp_model.text_preprocessor import clean_text


def test_text_cleaning():
    text = "Hello!!! How are you??"
    result = clean_text(text)

    assert result == "hello how are you"
