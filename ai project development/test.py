import os
from OpenAI import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("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"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",)