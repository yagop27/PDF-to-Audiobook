import fitz  # PyMuPDF
from boto3 import Session
import os

# Load AWS credentials from environment variables
ACCESS_KEY = os.environ.get('ACCESS_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

if not ACCESS_KEY or not SECRET_KEY:
    raise EnvironmentError("Missing AWS credentials in environment variables.")


def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file, sorted by reading order.

    :param pdf_file: Path to the PDF file
    :return: Extracted text as a string
    """
    try:
        with fitz.open(pdf_file) as doc:
            all_text = []
            for page in doc:
                blocks = page.get_text("blocks")
                blocks.sort(key=lambda b: b[1])  # Sort by vertical position
                for block in blocks:
                    all_text.append(block[4])  # Extract text from the block
            return "\n\n".join(all_text)
    except Exception as e:
        raise RuntimeError(f"Failed to extract text from PDF: {e}")


def synthesize_speech(text, output_file, access_key, secret_key):
    """
    Converts text to speech using AWS Polly.

    :param text: Text to be synthesized
    :param output_file: Output MP3 file name
    :param access_key: AWS access key
    :param secret_key: AWS secret key
    """
    try:
        session = Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name='us-west-2'
        )
        polly_client = session.client('polly')
        response = polly_client.synthesize_speech(
            VoiceId='Joanna',
            OutputFormat='mp3',
            Text=text,
            Engine='neural'
        )
        with open(output_file, 'wb') as file:
            file.write(response['AudioStream'].read())
    except Exception as e:
        raise RuntimeError(f"Failed to synthesize speech: {e}")


if __name__ == "__main__":
    pdf_file = input("Enter the path to the PDF file: ")
    output_file = input("Enter the output MP3 file name: ")

    try:
        print("Extracting text from PDF...")
        text = extract_text_from_pdf(pdf_file)
        print("Text extraction successful!")

        print("Converting text to speech...")
        synthesize_speech(text, output_file, ACCESS_KEY, SECRET_KEY)
        print(f"Speech synthesis complete! File saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
