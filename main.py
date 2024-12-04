import fitz  # PyMuPDF
from boto3 import Session
import os

ACCESS_KEY = os.environ['ACCESS_KEY']
SECRET_KEY = os.environ['SECRET_KEY']

fname = "sample.pdf"  # PDF file name

with fitz.open(fname) as doc:  # Open the PDF document
    all_text = []
    for page in doc:
        # Extract blocks from the page
        blocks = page.get_text("blocks")
        # Sort blocks by their vertical position (top coordinate)
        blocks.sort(key=lambda b: b[1])
        # Append the text of each block in reading order
        for block in blocks:
            all_text.append(block[4])  # The 5th element contains the text

# Join all blocks into a single string with page breaks
text = "\n\n".join(all_text)

polly_client = Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name='us-west-2').client('polly')

response = polly_client.synthesize_speech(VoiceId='Joanna',
                                          OutputFormat='mp3',
                                          Text=text,
                                          Engine='neural')

file = open('speech2.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()

