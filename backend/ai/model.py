from transformers import pipeline

#   multilingual public model that supports Amharic sentiment
analyzer = pipeline(
    "text-classification",
    model="cardiffnlp/twitter-xlm-roberta-base-sentiment"  # works without login or token
)

def analyze_text(text: str):
    """
    Analyze Amharic or English text and return prediction label + score.
    """
    result = analyzer(text)
    return result
