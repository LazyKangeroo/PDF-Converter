from settings import *
from converter import Convert
import pygame
import sys

class Main:
    def __init__(self):
        # general
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('PDF Converter')

        # font intit
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
            # Text for header surface
        self.text_surface_btn = self.font.render("Press to Convert : ", True, BLUE)
        self.text_rect_btn = self.text_surface_btn.get_rect(center=(WIDTH / 3, HEADER_HEIGHT / 2))
            # Text for dropbox surface
        self.text_surface_lbl = self.font.render("Drag & Drop..",True,WHITE)
        self.text_rect_lbl = self.text_surface_lbl.get_rect(center=(WIDTH / 2, HEIGHT / 2 - HEADER_HEIGHT/2))

        # Header Surface
        self.header_surface = pygame.Surface((WIDTH,HEADER_HEIGHT))
        self.header_rect = self.header_surface.get_rect(topleft=(0,0))

        # drop box
        self.dropbox_surface = pygame.Surface((WIDTH,HEIGHT-HEADER_HEIGHT))
        self.dropbox_rect = self.dropbox_surface.get_rect(bottomleft=(0,HEIGHT))

        # modules
        self.convert = Convert()

    def run(self):
        dropped = False
        correct_drop = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.DROPFILE:
                    print('File Dropped')
                    dropped = True # State that file was dropped

                    file_path = event.file

                    path = file_path.split('\\')
                    self.file_name = path[-1]
                    self.file_ex = self.file_name.split('.')
                    self.file_ex = self.file_ex[-1]

                    # Checking if file is supported
                    if self.file_ex in ['docx','doc','pdf']:
                        correct_drop = True # stating correct file type was dropped
                        print('Correct File Type')
                    else:
                        correct_drop = False # stating incorrect file type was dropped
                        print('Incorrect File Type')

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.header_rect.collidepoint(event.pos):
                        print('Header Clicked')
                        if dropped and correct_drop:
                            # Correct file dropped > file gets converted when header is clicked
                            print('...Converting File...')
                            self.convert.getFileInfo(file_path)
                            print('...Complete...')
                            dropped = False

                        elif not correct_drop:
                            print('...Reseting...')
                            dropped = False
                            file_path = ' '

            # Display
            self.window.blit(self.header_surface,self.header_rect)
            self.header_surface.fill(GREY)
            self.header_surface.blit(self.text_surface_btn,self.text_rect_btn)

            self.window.blit(self.dropbox_surface,self.dropbox_rect)

            # Chaning colour of dropbox depending on situation
            if dropped and correct_drop:
                self.dropbox_surface.fill(PURPLE)
            elif not dropped:
                self.dropbox_surface.fill(BLUE)
            elif dropped and not correct_drop:
                self.dropbox_surface.fill(RED)

            self.dropbox_surface.blit(self.text_surface_lbl,self.text_rect_lbl)

            # Update the display
            pygame.display.update()

main = Main()
main.run()