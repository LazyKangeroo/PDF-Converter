import docx
import os
import comtypes.client
from pdf2docx import Converter

class Convert:
    def __init__(self):
        pass

    def getFileInfo(self,og_path):
        # User inputs the file path
        # og_path = input('Enter File Path : ')
        print('------------------------------------------------------')

        # Splitting the path to extract the file name and path
        split_path = og_path.split(os.sep)  # Use os.sep for cross-platform compatibility
        file_name = split_path[-1]  # Extracting the file name
        split_path = split_path[:-1]  # Removing the last element (file name) from the path

        # Constructing the path without the file name
        path = os.sep.join(split_path)

        # Separating the file name and extension
        file_ex = file_name.rsplit('.', 1)  # Splits the string at the last dot
        file_name = file_ex[0]  # File name without extension
        file_ext = file_ex[-1]  # File extension

        print(f'File EX : {file_ext}')

        # Constructing the DOCX and PDF paths
        word_path = os.path.join(path, f'{file_name}.docx')
        pdf_path = os.path.join(path, f'{file_name}.pdf')

        print(f'Word Path : {word_path}')
        print(f'PDF Path : {pdf_path}')

        if file_ext in ['docx']:
            self.docxTopdf(word_path, pdf_path)
        elif file_ext in ['pdf']:
            self.pdfTodocx(word_path, pdf_path)

    def docxTopdf(self, docx_path, pdf_path):
        try:
            # Creating a Word application instance
            word = comtypes.client.CreateObject('Word.Application')
            word.Visible = False

            # Opening the DOCX file
            in_file = word.Documents.Open(docx_path)

            # Saving the file as PDF
            in_file.SaveAs(pdf_path, FileFormat=17)  # 17 corresponds to PDF format

            # Closing the document and quitting Word
            in_file.Close()
            word.Quit()

        except Exception as e:
            print(f"An error occurred: {e}")

    def pdfTodocx(self,docx_path,pdf_path):
        try:
            # Using the built-in function, convert the PDF file to a document file by saving it in a variable.
            cv = Converter(pdf_path)
            # Storing the Document in the variable's initialised path
            cv.convert(docx_path)
            # Conversion closure through the function close()
            cv.close()

        except Exception as e:
            print(f"An error occurred : {e}")

# convert = Convert()
# convert.getFileInfo()
