import click
from PyPDF2 import PdfReader

from ttf.utils import chat_with


def chat_with_file(path: str, prompt:str) -> str:
    """_summary_

    Args:
        path (str): _description_
        prompt (str): _description_

    Returns:
        str: _description_
    """

    if path.endswith('.pdf'):
        reader = PdfReader(path)
        text = "\n".join([page.extract_text() for page in reader.pages])

    elif path.endswith('.txt'):
        text = open(path, 'r').read()
    else:
        extension = path.split('.')[-1]
        raise ValueError(f'Files ending in "{extension}" are not yet supported')

    user_input = prompt + ":\n\n" + text
    chat_with(user_input)



@click.command()
@click.option("--file", "-f", type=click.Path(exists=True), required=True)
@click.option("--prompt", "-pr", type=str, default="Summarize the following text")
def main(pdf, prompt):
    """_summary_

    Args:
        pdf (_type_): _description_
        prompt (_type_): _description_
    """
    chat_with_file(pdf, prompt)

if __name__ == "__main__":
    main()
