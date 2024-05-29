import pygame
import sys
import os
import subprocess
# Initialize pygame
icon = pygame.image.load('game/Donjon de temp/logo.png')
pygame.display.set_icon(icon)
pygame.init()

# Set up the display
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Divided")

# Load the background images
background_images = [
    pygame.image.load("game/Donjon de temp/images/enfant.jpg").convert(),#0
    pygame.image.load("game/Donjon de temp/images/enfant.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/enfant.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/enfant.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/enfant.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/z1.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/chemin.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/chemin.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/tableau.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/tableau.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/tableau.jpg").convert(),#10
    pygame.image.load("game/Donjon de temp/images/tableau.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/tableau.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/tableau.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/z1.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/2porte.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/2porte.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/2porte.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/2porte.jpg").convert(),#18
    pygame.image.load("game/Donjon de temp/images/donjon_savoir.png").convert(),
    pygame.image.load("game/Donjon de temp/images/donjon_savoir.png").convert(),
    pygame.image.load("game/Donjon de temp/images/donjon_savoir.png").convert(),
    pygame.image.load("game/Donjon de temp/images/donjon_savoir.png").convert(),
    pygame.image.load("game/Donjon de temp/images/garde.png").convert(),
    pygame.image.load("game/Donjon de temp/images/garde.png").convert(),
    pygame.image.load("game/Donjon de temp/images/garde.png").convert(),
    pygame.image.load("game/Donjon de temp/images/garde.png").convert(),
    pygame.image.load("game/Donjon de temp/images/garde.png").convert(),
    pygame.image.load("game/Donjon de temp/images/real.png").convert(),
    pygame.image.load("game/Donjon de temp/images/real.png").convert(),
    pygame.image.load("game/Donjon de temp/images/real.png").convert(),
    pygame.image.load("game/Donjon de temp/images/real.png").convert(),
    pygame.image.load("game/Donjon de temp/images/real.png").convert(),
    pygame.image.load("game/Donjon de temp/images/real.png").convert(),
    pygame.image.load("game/Donjon de temp/images/real.png").convert(),
    pygame.image.load("game/Donjon de temp/images/real.png").convert(),
    pygame.image.load("game/Donjon de temp/images/real.png").convert(),
    pygame.image.load("game/Donjon de temp/images/real.png").convert(),
    pygame.image.load("game/Donjon de temp/images/real.png").convert(),
    pygame.image.load("game/Donjon de temp/images/real.png").convert(),  
    pygame.image.load("game/Donjon de temp/images/troue.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/troue.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/troue.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/troue.jpg").convert(),

]
# Scale the background images to fit the screen size
for i in range(len(background_images)):
    background_images[i] = pygame.transform.scale(background_images[i], (width, height))

# Set up the font
font = pygame.font.Font(None, 36)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 100, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize music
music_files = ["game/Donjon de temp/dbd.mp3"]
current_music_index = 0
pygame.mixer.music.load(music_files[current_music_index])

# Flag to check if music is playing
music_playing = False

# Function to play music
def play_music():
    global music_playing
    if not music_playing:
        pygame.mixer.music.play(start=0)  # Start from 0 seconds
        music_playing = True

# Function to pause music
def pause_music():
    pygame.mixer.music.pause()

# Function to unpause music
def unpause_music():
    pygame.mixer.music.unpause()

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()
    global music_playing
    music_playing = False
# Function to display text letter by letter
def printf(text, background_index, delay=60):
    text_surface = font.render("", True, (255, 255, 255))
    index = 0
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    background_index = (background_index + 1) % len(background_images)  # Change background image
                    return background_index  # Return updated background index
                elif event.key == pygame.K_1:
                    return '1'
                elif event.key == pygame.K_2:
                    return '2'
                elif event.key== pygame.K_3:
                    return '3'

        if index < len(text):
            text_surface = font.render(text[:index+1], True, (255, 255, 255))
            index += 1

        screen.blit(background_images[background_index], (0, 0))  # Change background image
        pygame.draw.rect(screen, (0, 0, 0), [0, 625, 1280, 300])
        screen.blit(text_surface, (50, 650))
        
        pygame.display.flip()
        
        pygame.time.wait(delay)  # Delay between each letter
        


def scene1():
    texts = [
        "{vous sortez du donjon avec le collier du feu et l'elexir du temp}",
        "vous : il me reste plus que la pierre du savoir...",
        "vous : et je peut retrouver mes parent...",
        "vous : ma soeur aussi...",
        "vous : je vais traverser ce portail",
        "...",
        "{vous appercevez 2 chemain le quel prendre}",
        " ",
    ]
    background_index = 0  # Initial background index
    
    for text in texts:
        background_index = printf(text, background_index)  # Pass the background index to the printf function
        
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render("Gauche", True, WHITE)
    option2 = menu_font.render("Droite", True, WHITE)
    option1_rect = option1.get_rect(bottomleft = (60, 685))
    option2_rect = option2.get_rect(bottomright = (1200, 685))
    screen.blit(option1, option1_rect)
    screen.blit(option2, option2_rect)
    pygame.display.flip()
    
    choice = None
    while choice not in ['1', '2']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if option1_rect.collidepoint(mouse_pos):
                    choice = '1'
                    scene1_choix1()
                elif option2_rect.collidepoint(mouse_pos):
                    choice = '2'
                    mort()





def mort():
    texts = [
        "{vous Tomber dans un piège profond...}",
        "vous: AAAAAAAAAAAAAAAAAAAAAAAAAA",
        "{vous faites une chute fatal}",
        " ",
    ]
    background_index = 40  # Initial background index
    
    for text in texts:
        background_index = printf(text, background_index)  # Pass the background index to the printf function
        
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render("Restart", True, WHITE)
    option2 = menu_font.render("Quitter", True, WHITE)
    option1_rect = option1.get_rect(bottomleft = (60, 685))
    option2_rect = option2.get_rect(bottomright = (1200, 685))
    screen.blit(option1, option1_rect)
    screen.blit(option2, option2_rect)
    pygame.display.flip()
    
    choice = None
    while choice not in ['1', '2']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if option1_rect.collidepoint(mouse_pos):
                    choice = '1'
                    scene1()
                elif option2_rect.collidepoint(mouse_pos):
                    choice = '2'
                    pygame.quit()
                    sys.exit()
                    



def scene1_choix1():
    texts = [
        "{vous avencez dans la grotte et vous trouver une inscription sur un mur}",
        "vous : hien ? A M A",
        "vous : ça doit surment etre quelque chose d'important qu'il faut retenir",
        "vous : mais qu'est ce que ça veut dire ?",
        "vous : on verra cela plus tard...",
        "vous : je dois continuer mon chemin",
        "...",
        "{vous arrivez devant 2 porte une porte avec une tete de Mort et l'autre avec des Anges}",
        "vous : je ne sais pas quelle porte choisir",
        "  ",
    ]
    background_index = 8  # Initial background index
    
    for text in texts:
        background_index = printf(text, background_index)  # Pass the background index to the printf function
        
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render("Mort", True, WHITE)
    option2 = menu_font.render("Anges", True, WHITE)

    option1_rect = option1.get_rect(bottomleft = (60, 685))
    option2_rect = option2.get_rect(bottomright = (1200, 685))

    screen.blit(option1, option1_rect)
    screen.blit(option2, option2_rect)

    pygame.display.flip()
    
    choice = None
    while choice not in ['1', '2']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if option1_rect.collidepoint(mouse_pos):
                    choice = '1'
                    scene1_choix1_2()                   
                elif option2_rect.collidepoint(mouse_pos):
                    choice = '2'
                    mort()
                


def scene1_choix1_2():
    texts = [
        "{vous traversez la porte et trouver 2 autres porte identique a ceux d'avant}",
        "vous : je ne sais pas quelle porte choisir",
        "  ",
    ]
    background_index = 16  # Initial background index
    
    for text in texts:
        background_index = printf(text, background_index)  # Pass the background index to the printf function
        
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render("Mort", True, WHITE)
    option2 = menu_font.render("Anges", True, WHITE)

    option1_rect = option1.get_rect(bottomleft = (60, 685))
    option2_rect = option2.get_rect(bottomright = (1200, 685))

    screen.blit(option1, option1_rect)
    screen.blit(option2, option2_rect)

    pygame.display.flip()
    
    choice = None
    while choice not in ['1', '2']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if option1_rect.collidepoint(mouse_pos):
                    choice = '1'
                    mort()                  
                elif option2_rect.collidepoint(mouse_pos):
                    choice = '2'
                    scene1_choix1_3()



def scene1_choix1_3():
    texts = [
        "{vous traversez la porte et trouver encore 2 autres porte identique a ceux d'avant}",
        "vous : Encore ? mais ça s'arrete jamais !"
        "vous : quel porte je dois choisir ?",
        "  ",
    ]
    background_index = 15  # Initial background index
    
    for text in texts:
        background_index = printf(text, background_index)  # Pass the background index to the printf function
        
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render("Mort", True, WHITE)
    option2 = menu_font.render("Anges", True, WHITE)

    option1_rect = option1.get_rect(bottomleft = (60, 685))
    option2_rect = option2.get_rect(bottomright = (1200, 685))

    screen.blit(option1, option1_rect)
    screen.blit(option2, option2_rect)

    pygame.display.flip()
    
    choice = None
    while choice not in ['1', '2']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if option1_rect.collidepoint(mouse_pos):
                    choice = '1'
                    scene2()                
                elif option2_rect.collidepoint(mouse_pos):
                    choice = '2'
                    mort()



def scene2():
    texts = [
        "vous : ouff j'ai enfin traverser tout ça !",
        "vous : le voila enfin le donjon du savoir !",
        "vous : je vais de suite y'aller",
        "...",
        "Garde du Donjon : tu ne rentrera pas dans ce donjon !",
        "vous : j'ai l'habitude maintenant donne ton enigme",
        "Garde Donjon : dis donc tu est mal poli pour un microbe",
        "??? : eyyy laisse le tranquille il est a moi",
        "Garde Donjon : Votre majésté ... je m'excuse il est a vous",
        "vous : qui est tu ?",
        "??? : c'est ma vraie aparence...",
        "??? : je suis jane",
        "vous : j- ja- ",
        "vous : JANE ! T UNE REINE DE DONJON TU MA TRAHIS !",
        "Jane : je me suis servis de toi pour avoir le collier du feu et la potion du temp",
        "jane : pour régner sur ce royaume et devenir leurs dieu",
        "vous : ... je peut donc faire confiance a personne",
        "jane : donne les moi je ne veut pas te faire de mal",
        "vous : si tu veut les prendre faudra me passer sur le corp",
        "jane : d'accord tu l'aura voulu",
        " "
    ]
    background_index = 19  # Initial background index
    
    for text in texts:
        background_index = printf(text, background_index)  # Pass the background index to the printf function
        
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render("Tuer Jane", True, WHITE)
    option2 = menu_font.render("l'epargner", True, WHITE)

    option1_rect = option1.get_rect(bottomleft = (60, 685))
    option2_rect = option2.get_rect(bottomright = (1200, 685))

    screen.blit(option1, option1_rect)
    screen.blit(option2, option2_rect)

    pygame.display.flip()
    
    choice = None
    while choice not in ['1', '2']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if option1_rect.collidepoint(mouse_pos):
                    choice = '1'
                    stop_music()
                    subprocess.call(["python", "game/ENDGAME/endgame.py"])               
                elif option2_rect.collidepoint(mouse_pos):
                    choice = '2'
                    stop_music()
                    subprocess.call(["python", "game/ENDGAME/endgame.py"])




# Main function
def main():
    play_music()
    scene1()


if __name__ == "__main__":
    main()

# Quit pygame
pygame.quit()
sys.exit()
