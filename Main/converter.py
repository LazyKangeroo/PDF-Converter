import docx
import os
import comtypes.client

class Convert:
    def __init__(self) -> None:
        pass

    def getFileInfo(self):
        path = ''
        og_path = input('Enter File Path : ')
        print('------------------------------------------------------')

        split_path = og_path.split('\\')
        print(f'Splitted path : {split_path}')
        file_name = split_path[-1]
        print(f'File name : {file_name}')
        split_path.pop(-1)
        print(f'Path without file name : {split_path}')

        print('##################################################################')
        for i in split_path:
            if i == split_path[0]:
                path = i
            else:
                path = f"{path}\\{i}"
            print(i)
            print(path)
        print('##################################################################')
        print(f'Path put together : {path}')

        file_extention = file_name.split('.')
        file_name = file_extention[0]
        file_extention = file_extention[-1]
        print(f'File Extention : {file_extention}')
        print(f'File Name without Extention : {file_name}')

        self.docxTopdf(path,file_name)

    def docxTopdf(self,file_path,file_name):
        word_path = f'{file_path}\\{file_name}.docx'
        pdf_path = f'{file_path}\\{file_name}.pdf'

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
        return


convert = Convert()
convert.getFileInfo()