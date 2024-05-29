import pygame
import time
from subprocess import call

class Button:
    def __init__(self, text, width, height, pos, elevation):
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'

        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = '#354B5E'

        self.text_surf = gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center 

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed:
                    play_song_menu(click_sound)
                    call(["python", "game\/menu.py"])
                    pygame.display.iconify()  # Minimize the window
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77'


pygame.display.set_caption("Devided")
icon = pygame.image.load('image\/logo.png')
pygame.display.set_icon(icon)

pygame.init()


def play_song_menu(song_file):
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(song_file)
        print("Playing:", song_file)
        pygame.mixer.music.play()
    except pygame.error as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    song_menu = r"song\1.mp3"
    click_sound = r"song\mouse.mp3"
    play_song_menu(song_menu)

    logo_image = pygame.image.load("image\/logo.png")

    font = pygame.font.Font('Font\/04B_30__.TTF', 22)
    screen = pygame.display.set_mode([1280, 720])
    timer = pygame.time.Clock()
    clock = pygame.time.Clock()
    gui_font = pygame.font.Font('Font\/04B_30__.TTF', 28)

    messages = ['Bienvenu dans le jeu de choix',
                'Sachez que vos choix sont decisifs sur la suite de l\'histoire',
                'On vous conseille de bien reflechir avant de faire vos choix',
                'La confiance... faut la preter qu\'a ceux qui la meritent',
                'Bonne chance...',
                ' Credit a :',
                'ANIS',
                'AMINE',
                'OMAR',
                'WAEL',
                '',
                '',
                'Amuse-toi bien !',
                '',
                '']

    start_y = 20 
    line_spacing = 30 
    message_delay = 3  

    
    screen.fill('black')
    screen.blit(logo_image, ((screen.get_width() - logo_image.get_width()) // 2, (screen.get_height() - logo_image.get_height()) // 2))
    pygame.display.flip()
    time.sleep(message_delay)

 
    screen.fill('black')
    pygame.display.flip()

  
    for message in messages:
        rendered_msg = font.render(message, True, 'White')
        screen.blit(rendered_msg, ((screen.get_width() - rendered_msg.get_width()) // 2, start_y))
        pygame.display.flip()
        start_y += rendered_msg.get_height() + line_spacing 
        time.sleep(message_delay)
        
    
    button1 = Button('Continue', 200, 40, (1050, 640), 5)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button1.check_click()

        
        button1.draw()
        pygame.display.update()

    pygame.mixer.music.stop()
    pygame.quit()
