import pygame
import sys
import os
import docx
import comtypes.client
from settings import *

class Main:
    def __init__(self):
        # General setup
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('PDF Converter')

        # Font setup
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.text_surface_btn = self.font.render("Press to Convert : ", True, TEXT)
        self.text_rect_btn = self.text_surface_btn.get_rect(center=(WIDTH / 3, HEADING_HEIGHT / 2))

        self.text_surface_lbl = self.font.render("Drag & Drop..",True,GREY)
        self.text_rect_lbl = self.text_surface_lbl.get_rect(center=(WIDTH / 2, HEIGHT / 2 - HEADING_HEIGHT/2))

        # Drop surface
        self.drop_surface = pygame.Surface((WIDTH, HEIGHT - HEADING_HEIGHT))
        self.drop_surface_rect = self.drop_surface.get_rect(bottomright=(WIDTH, HEIGHT))

        # Heading surface
        self.heading_surface = pygame.Surface((WIDTH, HEADING_HEIGHT))
        self.header_rect = pygame.Rect(0, 0, WIDTH, HEADING_HEIGHT)

    def run(self):
        converted = False
        dropped = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.DROPFILE:
                    print('File dropped')
                    self.file = event.file

                    # Handle the dropped file
                    self.file_name = os.path.basename(self.file)
                    self.file_type = self.file.split('.')[-1].lower()

                    if self.file_type in ['doc', 'docx']:
                        dropped = True
                        print(f"Dropped file: {self.file}")
                        print(f"File name: {self.file_name}")
                    else:
                        print('Unsupported File type was dropped')

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if self.header_rect.collidepoint(mouse_pos):
                        print('Header')
                        if dropped:
                            print('Should be converting')
                            converted = self.convert()

            # Display
            if dropped:  # When file gets dropped, change the color of drop surface
                self.drop_surface.fill(PURPLE)
                dropped = False
            else:
                self.drop_surface.fill(BLUE)

            if converted:  # When file is done converting, change back the color of drop surface
                self.drop_surface.fill(BLUE)
                converted = False

            self.drop_surface.blit(self.text_surface_lbl,self.text_rect_lbl)
            self.window.blit(self.drop_surface, self.drop_surface_rect)
            pygame.draw.rect(self.window, WHITE, self.drop_surface_rect, 1)

            self.heading_surface.fill(WHITE)
            self.heading_surface.blit(self.text_surface_btn, self.text_rect_btn)
            self.window.blit(self.heading_surface, (0, 0))

            # Update the display
            pygame.display.update()

    def convert(self):
        print('...Starting Conversion...')
        print('File being converted...')

        path = os.path.splitext(self.file)
        pdf_path = f'{path[0]}.pdf'
        print(pdf_path)

        doc = docx.Document(self.file)

        word = comtypes.client.CreateObject('Word.Application')
        docx_path = os.path.abspath(self.file)
        pdf_path = os.path.abspath(pdf_path)

        pdf_format = 17
        word.Visible = False
        in_file = word.Documents.Open(docx_path)
        in_file.SaveAs(pdf_path, FileFormat=pdf_format)
        in_file.Close()

        word.Quit()
        print('...File Finished Converting')
        return True

if __name__ == '__main__':
    main = Main()
    main.run()
