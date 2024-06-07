from settings import *
import docx
import pygame
import sys
import os
import comtypes.client

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
        dropped = True
        converted = False
        while True:
            for event in pygame.event.get():
                if event.type != pygame.QUIT:
                    if event.type == pygame.DROPFILE:
                        print('File dropped')
                        self.file = event.file

                        # Handle the dropped file
                        self.file_name = os.path.basename(self.file)
                        self.file_type = self.file.split('.')[-1].lower()

                        if not self.file_type in ['doc', 'docx']:
                            print('Unsupported File type was dropped')
                            continue
                        dropped = True
                        print(f"Dropped file: {self.file}")
                        print(f"File name: {self.file_name}")


                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos
                        if self.header_rect.collidepoint(mouse_pos):
                            print('Header')
                            # print('Should be converting')
                            #converted = self.convert()
                else:
                    pygame.quit()
                    sys.exit()

            # Display

            self.heading_surface.fill(WHITE)
            self.heading_surface.blit(self.text_surface_btn, self.text_rect_btn)
            self.window.blit(self.heading_surface, (0, 0))

            self.drop_surface.blit(self.text_surface_lbl,self.text_rect_lbl)
            self.window.blit(self.drop_surface, self.drop_surface_rect)
            pygame.draw.rect(self.window, WHITE, self.drop_surface_rect, 1)

            if dropped:  # When file gets dropped, change the color of drop surface
                self.drop_surface.fill(PURPLE)
                dropped = False
            else:
                self.drop_surface.fill(BLUE)

            # if converted:  # When file is done converting, change back the color of drop surface
            #     self.drop_surface.fill(BLUE)
            #     converted = False

            # Update the display
            pygame.display.update()


if __name__ == '__main__':
    main = Main()
    main.run()
