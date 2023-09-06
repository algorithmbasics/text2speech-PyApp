# Import required modules
import pyttsx3
import PyPDF2
import os

try:
    # Create PDF reader object
    pdf = PyPDF2.PdfReader(open('file.pdf', 'rb'))

    # Initialize text-to-speech engine
    speaker = pyttsx3.init()

    # Loop through pages
    for page_num in range(len(pdf.pages)):

        # Extract text from page
        text = pdf.pages[page_num].extract_text()

        # Clean text by removing newline chars
        clean_text = text.strip().replace('\n', ' ')

        # Print cleaned text
        print(clean_text)

        # Set output file name
        outfile = f"page_{str(page_num)}.mp3"

        # Save audio file
        speaker.save_to_file(clean_text, outfile)

        # Run and wait until processing is finished
        speaker.runAndWait()

    # Clean up
    speaker.stop()

    # play file
    os.startfile(outfile)

except FileNotFoundError:
    print("Error: The 'file.pdf' file was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
