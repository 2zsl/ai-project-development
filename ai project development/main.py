import os
import PyPDF2
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import prompts

# Loading the env file
_ = load_dotenv(find_dotenv())
client = OpenAI(
    api_key=os.environ.get('OPEN_API_KEY')
)

model = "gpt-4-turbo"
temperature = 0.7
max_tokens = 0
topic = " "

# Reading the PDF file
book = ""

# Prompts
system_message = prompts.system_message
prompt = prompts.generate_prompt(book, )

# helper function

def get_summary():
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}     
        ]
    )


# completion = client.chat.completions.create(
  # model="gpt-3.5-turbo",
  # messages=[
  #  {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
  #  {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)