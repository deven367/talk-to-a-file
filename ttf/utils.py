import os

import anthropic
from PyPDF2 import PdfReader
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt


# Function to send a message to the OpenAI chatbot model and return its response
def send_message(message_log: list) -> str:
    """_summary_

    Args:
        message_log (list): _description_

    Raises:
        ValueError: _description_

    Returns:
        str: _description_
    """
    try:
        api_key = os.environ["ANTHROPIC_API_KEY"]
    except KeyError:
        raise ValueError("ANTHROPIC_API_KEY not found in environment variables")

    client = anthropic.Client(api_key=api_key)

    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=3800,
        system="Respond like a no non-sense assistant who answers to the point without any bullshit",
        messages=message_log,
    )
    return response.content[0].text



def chat_with(user_input:str)-> None:
    """_summary_

    Args:
        user_input (str): _description_
    """
    # Initialize the conversation history with a message from the chatbot
    # message_log = [{"role": "system", "content": "You are a helpful assistant."}]
    message_log = []

    # Set a flag to keep track of whether this is the first request in the conversation
    first_request = True

    console = Console()

    # Start a loop that runs until the user types "quit"
    while True:
        if first_request:
            # If this is the first request, get the user's input and add it to the conversation history
            # user_input = input("You: ")
            # user_input = Prompt.ask("You   ")
            message_log.append(
                {"role": "user", "content": [{"type": "text", "text": user_input}]}
            )

            # Send the conversation history to the chatbot and get its response
            response = send_message(message_log)

            # Add the chatbot's response to the conversation history and print it to the console
            message_log.append({"role": "assistant", "content": [{"type": "text", "text": response}]})
            # print(f"AI assistant: {response}")

            console.print(Markdown(f"Haiku : {response}\n\n---"))
            # Set the flag to False so that this branch is not executed again
            first_request = False
        else:
            # If this is not the first request, get the user's input and add it to the conversation history
            # user_input = input("You: ")
            user_input = Prompt.ask("You   ")

            # If the user types "quit", end the loop and print a goodbye message
            if user_input.lower() == "quit" or user_input.lower() == "exit":
                # print("Goodbye!")
                console.print("Goodbye!")
                break

            message_log.append(
                {"role": "user", "content": [{"type": "text", "text": user_input}]}
            )

            # Send the conversation history to the chatbot and get its response
            response = send_message(message_log)

            # Add the chatbot's response to the conversation history and print it to the console
            message_log.append({"role": "assistant", "content": [{"type": "text", "text": response}]})
            # print(f"AI assistant: {response}")
            console.print(Markdown(f"Haiku : {response}\n\n---"))


def summarize_pdf_old(client: anthropic.Client, path: str, prompt:str) -> str:
    """_summary_

    Args:
        client (anthropic.Client): _description_
        path (str): _description_
        prompt (str): _description_

    Returns:
        str: _description_
    """
    reader = PdfReader(path)
    text = "\n".join([page.extract_text() for page in reader.pages])

    message_log = []
    message_log.append(
                {"role": "user", "content": [{"type": "text", "text": prompt + ":\n\n" + text}]}
            )

    # prompt = f"{anthropic.HUMAN_PROMPT}: Summarize the following text, should be readable:\n\n{text}\n\n{anthropic.AI_PROMPT}:\n\nSummary"

    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=3800,
        system="Respond like a no non-sense assistant who answers to the point without any bullshit",
        messages=message_log,
    )

    return response.content[0].text