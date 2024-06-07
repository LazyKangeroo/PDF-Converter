import docx
import os
import comtypes.client

class Convert:
    def __init__(self) -> None:
        pass

    def docxTopdf(self):
        word_path = 'Test.docx'
        pdf_path = 'Test.pdf'

        doc = docx.Document(word_path)

        word = comtypes.client.CreateObject('Word.Application')
        docx_path = os.path.abspath(word_path)
        pdf_path = os.path.abspath(pdf_path)

        pdf_format = 17
        word.Visible = False
        in_file = word.Documents.Open(docx_path)
        in_file.SaveAs(pdf_path, FileFormat=pdf_format)
        in_file.Close()

        word.Quit()