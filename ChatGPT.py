import openai

openai.api_key = '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'
response = openai.Completion.create(
    engine='text-davinci-003',  # Specify the engine ID or name
    prompt='Hello, how are you?',  # Your conversation prompt
    max_tokens=50,  # Maximum length of the response
    temperature=0.7,  # Controls the randomness of the response
    n=1,  # Number of responses to generate
    stop=None,  # Specify a custom stop sequence if desired
)

reply = response.choices[0].text.strip()
print(reply)
