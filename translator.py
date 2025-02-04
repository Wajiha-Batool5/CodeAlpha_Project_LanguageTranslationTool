from transformers import MarianMTModel, MarianTokenizer

# Specify the model name for the desired language pair
model_name = 'Helsinki-NLP/opus-mt-en-es'  # Example: English to Spanish

# Load the tokenizer and model
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Function to translate text
def translate(text):
    tokenized_text = tokenizer.prepare_seq2seq_batch([text], return_tensors='pt')
    translation = model.generate(**tokenized_text)
    translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)
    return translated_text

# Example usage
input_text = "Hello, how are you?"
translated_text = translate(input_text)
print(f"Translated Text: {translated_text}")