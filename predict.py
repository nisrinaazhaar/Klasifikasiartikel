from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification

import torch

# load tokenizer
tokenizer = AutoTokenizer.from_pretrained("Nisrinaazhaar/bert-model")

# load model
model = AutoModelForSequenceClassification.from_pretrained(
    "Nisrinaazhaar/bert-model"
)

# label mapping
labels = {
    0: "Computer Science",
    1: "Economy",
    2: "Medical"
}

def predict_article(text):

    # tokenize
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=512
    )

    # prediction
    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits

    # probability
    probs = torch.softmax(
    outputs.logits,
    dim=1
    )

    all_scores = probs[0].tolist()

    confidence, predicted_class = torch.max(
        probs,
        dim=1
    )

    label = labels[predicted_class.item()]

    return (
        label,
        confidence.item(),
        all_scores
    )
