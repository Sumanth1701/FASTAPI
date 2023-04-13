from fastapi import FastAPI
import logging
import os
import openai
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='myapp.log',
    filemode='a'
)

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/sentiment_analysis")
def sentiment_analysis(text: str):
    # Log the input text
    logger.info(f"Received request with text")

    # Set up OpenAI API key and prompt
    openai.api_key = "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"
    prompt = f"Please analyze the sentiment of the following text: '{text}'\nSentiment:"

    # Call the OpenAI API and log the response
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    result = response['choices'][0]['text']
    logger.info(f"OpenAI response: {response}")

    # Log the result and return it as a response
    logger.info(f"Returning result='{result}'")
    return {"result":result}
