from transformers import T5ForConditionalGeneration
from prepare_tokenizer import tokenizer


model = T5ForConditionalGeneration.from_pretrained('./trained_model')

def generate_answer(question):
    input_ids = tokenizer.encode(question, add_special_tokens=True, return_tensors='pt')
    output = model.generate(input_ids, max_length=600, num_return_sequences=1)
    decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)
    return decoded_output

