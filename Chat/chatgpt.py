import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

def generate_text(input):
    input_ids = tokenizer.encode(input, return_tensors='pt')
    output = model.generate(input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2, early_stopping=True)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

print("¡Bienvenido al chatbot de GPT-2! Escribe 'salir' para cerrar la sesión.")
while True:
    user_input = input('Tu: ')
    if user_input.lower() == 'salir':
        print('Chatbot: ¡Hasta luego!')
        break
    else:
        response = generate_text(user_input)
        print('Chatbot:', response)
