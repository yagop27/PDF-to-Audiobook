<h1>PDF to Speech Conversion</h1>

This Python script extracts text from a PDF file and converts it to speech using AWS Polly, saving the output as an MP3 file. The script is designed to help users create audio versions of their PDF documents efficiently.

<h2>Features</h2>
  - Extracts text from PDF files using PyMuPDF.
  - Converts the extracted text to high-quality speech using AWS Polly.
  - Allows users to specify custom PDF input and MP3 output file names.
  - Handles errors gracefully with clear error messages.

<h2>Requirements</h2>

  1- Python Libraries:

    - PyMuPDF (fitz)
    - boto3
    
  Install the required libraries:

    pip install pymupdf boto3

2- AWS Credentials:

  - Set up AWS access and secret keys in environment variables:
    ```
    export ACCESS_KEY='your-access-key'
    export SECRET_KEY='your-secret-key'
    
<h2>Usage</h2>

  1- Clone the repository or download the script.
  2- Run the script:

    python pdf_to_speech.py
  3- Provide the path to your PDF file and the desired name for the output MP3 file when prompted.

<h2>Error Handling</h2>

The script ensures:

  - Valid AWS credentials are set.
  - The PDF file exists and can be read.
  - The output MP3 file is safely written.

If any error occurs, a clear message is displayed to help diagnose the issue.
