import pygame
import sys
import os
import subprocess
icon = pygame.image.load('game\Donjon de deu\logo.png')
pygame.display.set_icon(icon)
# Initialize pygame
pygame.init()

# Set up the display
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Divided")

# Load the background images
background_images = [
    pygame.image.load("game/Donjon de deu/images/enfant_sortant_donjon.jpg").convert(),#0
    pygame.image.load("game/Donjon de deu/images/enfant_sortant_donjon.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/enfant_sortant_donjon.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/enfant_sortant_donjon.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/enfant_sortant_donjon.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/nain_qui_salue.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/nain_qui_salue.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/nain_qui_salue.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/nain_qui_salue.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/nain_qui_salue.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/nain_qui_salue.jpg").convert(),#10
    pygame.image.load("game/Donjon de deu/images/nain_qui_salue.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/nain_qui_salue.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/nain_qui_salue.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/nain_qui_salue.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/nain_qui_salue.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/nain_qui_salue.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/nain_qui_salue.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/foret.jpg").convert(),#18   
    pygame.image.load("game/Donjon de deu/images/desert.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/nain_qui_salue.jpg").convert(),#20
    pygame.image.load("game/Donjon de deu/images/nain_qui_salue.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/nain_qui_salue.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/portail.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/portail.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/nain_qui_salue.jpg").convert(),#scène 1 hna tkhlass #25
    pygame.image.load("game/Donjon de deu/images/nain_qui_salue.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/nain_qui_salue.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/foret.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/desert.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/nain_qui_salue.jpg").convert(),#30
    pygame.image.load("game/Donjon de deu/images/desert.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/enfant_desert.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/enfant_desert.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/enfant_desert.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/enfant_desert.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/enfant_desert.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/enfant_desert.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/enfant_desert.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/enfant_desert.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/enfant_desert.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/enfant_desert.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/enfant_desert.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/z1.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/enfant_foret.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/z1.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/donjon_du_temp.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/donjon_du_temp.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/donjon_du_temp.jpg").convert(),

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
music_files = ["game/Donjon de deu/peace.mp3"]
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
        "{en sortant du donjon vous regardez le collier de fluffy}",
        "(c'est donc ça le collier du feu...)",
        "(il me reste encore 2 donjon a faire celui du temp et du savoir...)",
        "???? : EYY toi !",
        "vous : hien ?",
        "???? : la en bas ! ",
        "vous : AHHHHH C'est quoi ça ! ",
        "vous : t'es un nain ?",
        "??? : pas très poli tout ça",
        "??? : je m'apelle jackson",
        "vous : enchenté Jack...",
        "jack : je t'ai entendu dire que tu voulais allez au donjon du temp et savoir",
        "(comment il a pu m'entendre j'ai parlé dans mes pensé)",
        "jack : je peut lire les pensé hahaah",
        "vous : hien ?? comment !",
        "jack : j'ai été bénie par la détentrice de la pierre du savoir ",
        "vous : je vois.. bon comment allez au donjon du temp ?",
        "jack : donjon du temp ? il y'as plusieurs chemins ",
        "jack : il y'as cette foret magique qui va te menner vers le donjon",#14
        "jack : l'autre coté desert ne mène a rien",
        "vous : attend attend j'était pas tombé dans un grotte de base ?",
        "vous : et la je trouve des foret et des deserts ?",
        "jack : ouais mais c'est pas pareil ici tout est différents",
        "jack : tu n'est pas réelment tombé dans un grotte",
        "jack : t'es plutôt tombé dans une autre dimension",
        "vous : d'accord je ne comprend toujours rien a ce qui ce passe ici",
        "vous :  peu importe ,je peut te faire confiance et passé par la foret ?",
        "jack : la décision revien a toi",
        "choix 1 : passée par la foret et lui faire confiance",
        "choix 2 : passée par le desert et ne pas lui faire confiance",
        " ",
    ]
    background_index = 0  # Initial background index
    
    for text in texts:
        background_index = printf(text, background_index)  # Pass the background index to the printf function
        
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render("Choice 1", True, WHITE)
    option2 = menu_font.render("Choice 2", True, WHITE)
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
                    scene1_choix2()



def scene1_choix1():
    texts = [
        "{vous décider de passée par la foret magique...}",
        "...",
        "{après une longue traversé dans la foret vous apercevez le donjon du temp de loin..}",
        "vous : ahhh le voila ! j'arrive te cherché Midas !",
        " ",
    ]
    background_index = 44
    for text in texts:
        background_index = printf(text, background_index)
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render(" ", True, WHITE)
    option2 = menu_font.render("Continue", True, WHITE)
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
                elif option2_rect.collidepoint(mouse_pos):
                    choice = '2'
                    stop_music()
                    subprocess.call(["python", "game/Donjon de temp/Donjon TEMP.py"])

def scene1_choix2():
    texts = [
        "{après une longue traversé dans le desèrt vous trouvez rien...}",
        "vous : je vais mourire de soif....",
        "jack : eyy , je t'avais dit de me faire confiance hehe",
        "vous : hien tu est ou jack",
        "jack : je te parle par télépathie ",
        "vous : aide moi a sortir d'ici",
        "jack : mmmm d'accord mais tu m'en doit une ",
        "vous : d'accord ...",
        "jack : je vais te téléporter vers la foret magique directement",
        "vous : hien , POURQUOI TU N'AS PAS FAIT SA AVANT",
        "jack : oh oh calmos , c'est pas drole sinon de tout avoir facilment",
        "jack : ferme grand les yeux ça va étre rapide",
        "...",
        "{vous ouvrez les yeux dans la foret magique,vous commencé la traversé}",
        "...",
        "{après une traversé dans la foret vous apercevez le donjon du temp de loin}",
        "vous : ahhh le voila ! j'arrive te cherché Midas !",
        " ",
    ]
    background_index = 31
    for text in texts:
        background_index = printf(text, background_index)
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render(" ", True, WHITE)
    option2 = menu_font.render("Continue", True, WHITE)
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
                elif option2_rect.collidepoint(mouse_pos):
                    choice = '2'
                    stop_music()
                    subprocess.call(["python", "game/Donjon de temp/Donjon TEMP.py"])
                    pygame.quit()
                    sys.exit()



# Main function
def main():
    play_music()
    scene1()

if __name__ == "__main__":
    main()

# Quit pygame
pygame.quit()
sys.exit()
