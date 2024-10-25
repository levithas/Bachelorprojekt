from transformers import pipeline

fill_mask = pipeline(
    "fill-mask",
    model="google/mobilebert-uncased",
    tokenizer="google/mobilebert-uncased"
)

text = """
I love it to
"""

for i in range(100):
    text = fill_mask(text + fill_mask.tokenizer.mask_token + " ")[0]['sequence']

print(text)