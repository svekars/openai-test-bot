import openai
import requests
from bs4 import BeautifulSoup

openai.api_key = "YOUR_API_KEY"
model_engine = "text-davinci-003"
model_prompt = (f"What would you like to know about PyTorch?")

url = "https://pytorch.org"

response = requests.get(url)

sp = BeautifulSoup(response.content, 'html.parser')
questions = sp.find_all('h2', class_= 'question' )
answers = sp.find_all('div', class_= 'answer')

qs = {}
for i in range(len(questions)):
    question = questions[i].text.strip()
    answer = answers[i].text.strip()
    qs[question] = answer

def answer_qs(question):
    prompt = model_prompt + question
    response = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens = 1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = response.choices[0].text.strip()
    return answer

while True:
    user_input = input('What would you like to learn? (type "exit" to quit): ')
    if user_input.lower() == 'exit':
        break
    if user_input in qs:
        print(qs[user_input])
    else:
        print(answer_qs(user_input))
