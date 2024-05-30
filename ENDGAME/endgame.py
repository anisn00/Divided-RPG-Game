import pygame
import sys
import os
import subprocess
# Initialize pygame
icon = pygame.image.load('game\ENDGAME\logo.png')
pygame.display.set_icon(icon)
pygame.init()

# Set up the display
width, height = 1280, 720


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Divided")

# Load the background images
background_images = [
    pygame.image.load("game/ENDGAME/images/real.png").convert(),#0
    pygame.image.load("game/ENDGAME/images/real.png").convert(),
    pygame.image.load("game/ENDGAME/images/real.png").convert(),
    pygame.image.load("game/ENDGAME/images/real.png").convert(),
    pygame.image.load("game/ENDGAME/images/real.png").convert(),
    pygame.image.load("game/ENDGAME/images/real.png").convert(),
    pygame.image.load("game/ENDGAME/images/enfant_po.jpg").convert(),
    pygame.image.load("game/ENDGAME/images/explose_potion.png").convert(),#7
    pygame.image.load("game/ENDGAME/images/explose_potion.png").convert(),
    pygame.image.load("game/ENDGAME/images/attaque_temp.png").convert(),
    pygame.image.load("game/ENDGAME/images/attaque_temp.png").convert(),
    pygame.image.load("game/ENDGAME/images/explose_potion.png").convert(),
    pygame.image.load("game/ENDGAME/images/explose_potion.png").convert(),
    pygame.image.load("game/ENDGAME/images/jane.png").convert(),
    pygame.image.load("game/ENDGAME/images/jane.png").convert(),
    pygame.image.load("game/ENDGAME/images/attaque_feu.png").convert(),#15
    pygame.image.load("game/ENDGAME/images/attaque_feu.png").convert(),
    pygame.image.load("game/ENDGAME/images/attaque_feu.png").convert(),
    pygame.image.load("game/ENDGAME/images/attaque_feu.png").convert(),
    pygame.image.load("game/ENDGAME/images/jane.png").convert(),
    pygame.image.load("game/ENDGAME/images/jane.png").convert(),#20
    pygame.image.load("game/ENDGAME/images/jane.png").convert(),
    pygame.image.load("game/ENDGAME/images/jane.png").convert(),
    pygame.image.load("game/ENDGAME/images/jane.png").convert(),
    pygame.image.load("game/ENDGAME/images/double_attaque.png").convert(),
    pygame.image.load("game/ENDGAME/images/double_attaque.png").convert(),
    pygame.image.load("game/ENDGAME/images/kamehamea.png").convert(),
    pygame.image.load("game/ENDGAME/images/kamehamea.png").convert(),
    pygame.image.load("game/ENDGAME/images/kamehamea.png").convert(),
    pygame.image.load("game/ENDGAME/images/affaiblie.png").convert(),
    pygame.image.load("game/ENDGAME/images/affaiblie.png").convert(),#30
    pygame.image.load("game/ENDGAME/images/affaiblie.png").convert(),
    pygame.image.load("game/ENDGAME/images/affaiblie.png").convert(),
    pygame.image.load("game/ENDGAME/images/affaiblie.png").convert(),
    pygame.image.load("game/ENDGAME/images/affaiblie.png").convert(),
    pygame.image.load("game/ENDGAME/images/affaiblie.png").convert(),
    pygame.image.load("game/ENDGAME/images/affaiblie.png").convert(),
    pygame.image.load("game/ENDGAME/images/histoire.png").convert(),
    pygame.image.load("game/ENDGAME/images/histoire.png").convert(),
    pygame.image.load("game/ENDGAME/images/histoire.png").convert(),
    pygame.image.load("game/ENDGAME/images/histoire.png").convert(),#40
    pygame.image.load("game/ENDGAME/images/histoire.png").convert(),
    pygame.image.load("game/ENDGAME/images/affaiblie.png").convert(),
    pygame.image.load("game/ENDGAME/images/affaiblie.png").convert(),
    pygame.image.load("game/ENDGAME/images/janerap.png").convert(),
    pygame.image.load("game/ENDGAME/images/janerap.png").convert(),
    pygame.image.load("game/ENDGAME/images/calin.png").convert(),
    pygame.image.load("game/ENDGAME/images/calinou.png").convert(),
    pygame.image.load("game/ENDGAME/images/calinou.png").convert(),
    pygame.image.load("game/ENDGAME/images/calinou.png").convert(),
    pygame.image.load("game/ENDGAME/images/calinou.png").convert(),#50
    pygame.image.load("game/ENDGAME/images/calinou.png").convert(),
    pygame.image.load("game/ENDGAME/images/z1.jpg").convert(),
    pygame.image.load("game/ENDGAME/images/z1.jpg").convert(),
    pygame.image.load("game/ENDGAME/images/h.png").convert(),
    pygame.image.load("game/ENDGAME/images/h.png").convert(),
    pygame.image.load("game/ENDGAME/images/h.png").convert(),
    pygame.image.load("game/ENDGAME/images/h.png").convert(),
    pygame.image.load("game/ENDGAME/images/h.png").convert(),
    pygame.image.load("game/ENDGAME/images/perefille.png").convert(),
    pygame.image.load("game/ENDGAME/images/perefille.png").convert(),#60
    pygame.image.load("game/ENDGAME/images/perefille.png").convert(),
    pygame.image.load("game/ENDGAME/images/perefille.png").convert(),
    pygame.image.load("game/ENDGAME/images/perefille.png").convert(),
    pygame.image.load("game/ENDGAME/images/z1.jpg").convert(),
    pygame.image.load("game/ENDGAME/images/z1.jpg").convert(),
    pygame.image.load("game/ENDGAME/images/z1.jpg").convert(),
    pygame.image.load("game/ENDGAME/images/jane_attaque.png").convert(),#67
    pygame.image.load("game/ENDGAME/images/jane_attaque.png").convert(),
    pygame.image.load("game/ENDGAME/images/jane_attaque.png").convert(),
    pygame.image.load("game/ENDGAME/images/jane_attaque.png").convert(),
    pygame.image.load("game/ENDGAME/images/jane_attaque.png").convert(),
    pygame.image.load("game/ENDGAME/images/jane_attaque.png").convert(),
    pygame.image.load("game/ENDGAME/images/z1.jpg").convert(),
    pygame.image.load("game/ENDGAME/images/z1.jpg").convert(),
    pygame.image.load("game/ENDGAME/images/z1.jpg").convert(),

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
music_files = ["game/ENDGAME/eld.mp3"]
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
        "Jane : QUE LE COMBAT COMMENCE",
        "Vous : D'accord tu va voir de quoi je suis capable",
        "Vous : je ne suis plus le meme qui s'est fait avoir par fluffy",
        "Vous : je suis devenu plus fort et plus intelligent",
        "Vous : Bon Bon Bon je commence avec quoi ",
        " ",
    ]
    background_index = 0  # Initial background index
    
    for text in texts:
        background_index = printf(text, background_index)  # Pass the background index to the printf function
        
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render("Utiliser La potion du temp", True, WHITE)
    option1_rect = option1.get_rect(bottomleft = (60, 685))

    screen.blit(option1, option1_rect)

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




def scene1_choix1():
    texts = [
        "Vous : voyons voir ce que fait cette potion",
        "{le temp s'arrete}",
        "vous : JE VAIS PRENDRE L'OCCASION ET L'ATTAQUER",
        "{la vie de jane decend enormément...}",
        "{le temp revient a la normal}",
        "{la potion de temp se casse}",
        "vous : il me reste que le collier maintenant",
        "Jane : tu est devenue fort dis donc",
        "Jane : a mon tour de te montrer de quoi je suis capable ",
        "{jane charge son attaque}",
        "Vous : HIEEEEEEEEN",
        "{l'attaque de jane ou atteint elle est inésquivable...} ",
        "{vos HP décende énormément}",
        "vous : ...",
        "vous : je dois utiliser le collier du feu il me reste plus que ça...",
        "vous : mais si je l'utilise il risque de casser aussi ",
        "vous : et je n'aurai pas de quoi me défendre",
        "  ",
    ]
    background_index = 6  # Initial background index
    
    for text in texts:
        background_index = printf(text, background_index)  # Pass the background index to the printf function
        
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render("Utiliser le collier", True, WHITE)
    option2 = menu_font.render("Ne pas l'utiliser", True, WHITE)
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
                    scene2_choix1()                   
                elif option2_rect.collidepoint(mouse_pos):
                    choice = '2'
                    scene2_choix2()


def scene2_choix2() :
    texts = [
        "Jane : tu va goutter a mon attaque spécial",
        "Jane : tient toi prèt",
        "vous : NON Attend !",
        "{jane charge une très grande attaque inésquivable}",
        "Jane : AAAAAAAAAAAAAAAAAA",
        "Vous : NOOOOOOOOOOOOOOOOOOOOOOON",
        "Vous : pa-... papa...",
        "{vous êtes mort}",
        "  ",
    ]
    background_index = 67  # Initial background index
    
    for text in texts:
        background_index = printf(text, background_index)  # Pass the background index to the printf function
        
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render("restart", True, WHITE)
    option2 = menu_font.render("quitter", True, WHITE)
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






def scene2_choix1() :
    texts = [
        "Vous : je vais utiliser donc le collier du feu...",
        "Jane : ahahah prépare toi a recevoir mon attaque la plus forte",
        "vous : Prépare toi aussi ",
        "vous : AAAAAAAAAAAAAAAAA",
        "Jane : AAAAAAAAAAAAAAAAAA",
        "{vos Hp décende a 1%}",
        "{jane est extrément affaiblie}",
        "jane : tu- tu est devenue très fort depuis la dernière fois...",
        "jane : et dire que fluffy t'avait one shot",
        "vous : Tu n'es pas comme la dernière fois, où est la faible Jane ? ",
        "Jane : HAHAHAHAHA,",
        "Jane : Petit enfant, je ne t'ai pas dit que j'ai le pouvoir de guérison",
        "Jane : Maintenant, qui va te sauver ?",
        "vous : Reflichi, reflichi !, je dois faire quelque chose.",
        "{Il y a deux ans.}",
        "{Ton père te racontait une histoire avant de dormir.}",
        "{L'histoire incluait une citation sur la réalité des créatures}",
        "{Les méchants doivent être aimés, et les bons doivent prendre soin d'eux}",
        "{Un câlin peut résoudre tous les problèmes.}",
        "vous : Ah, la citation concernait cette situation...",
        "vous : Vraiment, mon père me manque.",
        "{À ce moment-là, Jane se rapproche de toi.}",#-------------------------------------------------------
        "vous : Je dois la prendre dans mes bras.",
        "{Tu as sauté sur Jane et elle était choquée.}",
        "{Jane a disparu et réapparaît comme votre sœur.}",#
        "vous : Sis, c'est toi, Quoi.",
        "vous : Ma sœur, comment oses-tu...",
        "vous :vien ...",
        "vous : la",
        "{Tes yeux commencent à se fermer tout seuls, et tu ne sais pas ce qui s'est passé.}",
        "????? : Fre---re!!!, freere",#z1
        "????? : Réveille-toi",#22
        "vous : Quoi.., Qui",
        "vous : OUF, ma sœur...",
        "vous : Je peux enfin me reposer.",
        "ta sœur: Réveille-toi, notre père nous attend.",
        "{Soudain, ton père entre dans la pièce.}",#
        "Ton pere : Que se passe-t-il, tout va bien ?",
        "vous : Papa, je t'aime, tu es le meilleur.",
        "vous : Ensuite, tu commences à pleurer.",
        "{cela était qu'un simple cauchmard...}",
        " ",
        " La Fin .",
        " ",
    ]
    background_index = 23  # Initial background index
    
    for text in texts:
        background_index = printf(text, background_index)  # Pass the background index to the printf function
        
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render(" ", True, WHITE)
    option2 = menu_font.render("End", True, WHITE)
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
                    subprocess.call(["python", "game/outro.py"])




# Main function
def main():
    play_music()
    scene1()


if __name__ == "__main__":
    main()

# Quit pygame
pygame.quit()
sys.exit()
