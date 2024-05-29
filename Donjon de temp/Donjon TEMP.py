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
    pygame.image.load("game/Donjon de temp/images/photo_enfant_donjon_temp.jpg").convert(),#0
    pygame.image.load("game/Donjon de temp/images/photo_enfant_donjon_temp.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/photo_enfant_donjon_temp.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/photo_enfant_donjon_temp.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/photo_enfant_donjon_temp.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/photo_enfant_donjon_temp.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/photo_enfant_donjon_temp.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/photo_enfant_donjon_temp.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/photo_enfant_donjon_temp.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/photo_enfant_donjon_temp.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/photo_enfant_donjon_temp.jpg").convert(),#10
    pygame.image.load("game/Donjon de temp/images/enigme_donjon_temp.png").convert(),
    pygame.image.load("game/Donjon de temp/images/enigme_donjon_temp.png").convert(),
    pygame.image.load("game/Donjon de temp/images/enigme_donjon_temp.png").convert(),
    pygame.image.load("game/Donjon de temp/images/enigme_donjon_temp.png").convert(),
    pygame.image.load("game/Donjon de temp/images/enigme_donjon_temp.png").convert(),
    pygame.image.load("game/Donjon de temp/images/enigme_donjon_temp.png").convert(),
    pygame.image.load("game/Donjon de temp/images/photo_enfant_donjon_temp.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/photo_enfant_donjon_temp.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/photo_enfant_donjon_temp.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/photo_enfant_donjon_temp.jpg").convert(),#20
    pygame.image.load("game/Donjon de temp/images/photo_enfant_donjon_temp.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/photo_enfant_donjon_temp.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/photo_enfant_donjon_temp.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/photo_enfant_donjon_temp.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/enigme2.png").convert(),
    pygame.image.load("game/Donjon de temp/images/enigme2.png").convert(),
    pygame.image.load("game/Donjon de temp/images/enigme2.png").convert(),
    pygame.image.load("game/Donjon de temp/images/enigme2.png").convert(),
    pygame.image.load("game/Donjon de temp/images/enigme2.png").convert(),
    pygame.image.load("game/Donjon de temp/images/enigme2.png").convert(),#30
    pygame.image.load("game/Donjon de temp/images/AT.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/AT.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/AT.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/AT.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/AT.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/z1.jpg").convert(),
    pygame.image.load("game/Donjon de temp/images/z1.jpg").convert(),#37
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),#38
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),#40
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),#45
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),#50
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),#55
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),#60
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d1.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d2.png").convert(),#64
    pygame.image.load("game/Donjon de temp/images/d2.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d2.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d2.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d2.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d2.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d2.png").convert(),#70
    pygame.image.load("game/Donjon de temp/images/d2.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d2.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d2.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d2.png").convert(),#74
    pygame.image.load("game/Donjon de temp/images/d3.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d3.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d3.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d3.png").convert(),
    pygame.image.load("game/Donjon de temp/images/d3.png").convert(),
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
music_files = ["game/Donjon de temp/n.mp3"]
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
        "{en arrivant devant la porte du donjon vous trouvez un garde}",
        "Garde Donjon : que faites vous ici Humain",
        "vous : je cherche le roi de ce donjon ",
        "vous : mi- midas c'est ça ?",
        "Garde Donjon : hmmmm je vois tu connais midas",
        "Garde Donjon : je vois que tu posède le collier du feu que est il arrivé a fluffy",
        "vous : peut-importe laisse moi rentrer !",
        "Garde Donjon : malheureusment tu ne peut pas entré dans ce donjon",
        "Garde Donjon : a moin que tu réponde a mon énigme ",
        "vous : D'accord je suis prèt pour ton énigme !",
        "...",
        "Garde Donjon : Dans l'éternel ballet des astres, je trace mon chemin,",
        "Garde Donjon: Les mortels tentent de me saisir, mais je reste lointain.",
        "Garde Donjon : Je suis un flux incessant, une énigme sans fin",
        "Garde Donjon : Certains me voient comme un allié, d'autres redoutent mon destin.",
        "Garde Donjon : Suis-je le temps qui s'écoule inexorablement || ou bien l'horloge qui en garde le secret",#16
        " ",
    ]
    background_index = 0  # Initial background index
    
    for text in texts:
        background_index = printf(text, background_index)  # Pass the background index to the printf function
        
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render("le temps qui s'écoule inexorablement", True, WHITE)
    option2 = menu_font.render("l'horloge qui en garde le secret", True, WHITE)
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
        "Garde Donjon : bonne réponse tu est donc digne de rentré dans ce donjon",
        "Garde Donjon : si tu aurait mal répondu tu serait probablement mort...",
        "Garde Donjon : entre dans le donjon",
        "...",
        "vous : ouff j'ai encore eu de la chance cette fois",
        "{vous entrer dans le donjon}",
        "  ",
    ]
    background_index = 0
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
                    scene2_midas()


def scene1_choix2():
    texts = [
        "Garde Donjon : mauvaise réponse !",
        "Garde Donjon : tu n'as pas le droit de rentré dans ce donjon",
        "vous : hien comment ça !",
        "vous : je refuse , il faut que je rentre quoi qu'il advienne",
        "Garde Donjon : tu est donc tétu...",
        "Garde Donjon : Voici donc une autre enigme",
        "vous : hien ? une autre ? d'accord.... ",
        "Garde Donjon : ça sera une enigme de calcul",
        "Garde Donjon : Je suis un nombre entre 1 et 10 ,Si tu me multiplies par 2",
        "Garde Donjon : puis tu ajoutes 5, et ensuite tu divises le résultat par 3,",
        "Garde Donjon : tu obtiens le même nombre que si tu m'avais simplement ajouté 2",
        "Garde Donjon : Quel est ce nombre ?",
        "réponse 1 : le nombre 12       réponse 2 : le nombre 6         réponse 3: le nombre 9",
        "  ",
    ]
    background_index = 17  # Initial background index
    
    for text in texts:
        background_index = printf(text, background_index)  # Pass the background index to the printf function
        
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render("Nombre 12", True, WHITE)
    option2 = menu_font.render("Nombre 6", True, WHITE)
    option3=menu_font.render("Nombre 9",True,WHITE)
    option1_rect = option1.get_rect(bottomleft = (60, 685))
    option2_rect = option2.get_rect(bottomright = (1200, 685))
    option3_rect = option3.get_rect(center=(640 , 673))
    screen.blit(option1, option1_rect)
    screen.blit(option2, option2_rect)
    screen.blit(option3, option3_rect)
    pygame.display.flip()
    
    choice = None
    while choice not in ['1', '2','3']:
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
                elif option3_rect.collidepoint(mouse_pos):
                    choice = '3'
                    scene2_choix1()

def scene2_choix1() :
    texts = [
        "Garde Donjon : Mauvaise Réponse !",
        "Garde Donjon : Fait t'es adieux !",
        "vous : NON Attend !",
        "{le garde vous attaque vos Hp décende énormément...}",
        "vous : jane dé- désolé...",
        "{vous ètes mort}",
        "  ",
    ]
    background_index = 31  # Initial background index
    
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


def scene2_choix2() :
    texts = [
        "Garde Donjon : mmm je vois",
        "Garde Donjon : tu a eu de la chance cette fois !",
        "vous : comment ça ? ",
        "Garde Donjon : c'est la bonne réponse tu est digne de rentré dans le donjon",
        "vous : ouff j'ai encore eu de la chance cette fois",
        "{vous entrer dans le donjon}",
        "  ",
    ]
    background_index = 0
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
                    scene2_midas()

def scene2_midas():
    texts = [
        "????? : HAHAHAHAHA",
        "????? : Le tueur de mon frère Fluffyyyy.",
        "????? : Tu m'as enfin atteint",
        "vous : Mais qui est tu ?",
        "vous : Le frere de Fluffy ? La fleur !! HAHAHAHA",
        "????? : Je suis MIDAS, le Seigneur des Monstres et le frère de Fluffy, mon frère décédé.",
        "Midas : Quels étaient les derniers mots de mon frère ?",
        "  ",
        
    ]
    background_index = 38  # Initial background index
    
    for text in texts:
        background_index = printf(text, background_index)  # Pass the background index to the printf function
        
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render("Rends-le fou", True, WHITE)
    option2 = menu_font.render("Demande-lui à propos de colier", True, WHITE)
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
                    scene2_midas_choix1()
                elif option2_rect.collidepoint(mouse_pos):
                    choice = '2'
                    scene2_midas_choix2()


def scene2_midas_choix1() :
    texts = [
        "vous : Ton frère pleurait comme un bébé",
        "vous : Maintenant où est Ta potion",
        "Midas : HAHAHAHAHA, ",
        "Midas : Petit enfant, tu ne me connais pas",
        "{ Vous Avez 2 hp }",
        "  ",
    ]
    background_index = 45
    for text in texts:
        background_index = printf(text, background_index)
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render("Utiliser le colier", True, WHITE)
    option2 = menu_font.render("Ne pas utiliser le colier", True, WHITE)
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
                    scene2_midas_choix2_1()
                elif option2_rect.collidepoint(mouse_pos):
                    choice = '2'
                    scene2_midas_choix2_2()    


def scene2_midas_choix2() :
    texts = [
        "vous : De toute façon, oublions ton petit frère.",
        "Midas : Je peux voir ton arrogance, j'aime ça.",
        "Midas : HAHAHAHAHA",
        "vous : J'ai aussi perdu ma famille, alors ce n'est pas grave",
        "vous : Maintenant donne-moi ta potion, sinon tu regretteras ce qui va se passer",
        "{ Vous Avez 2 hp }",
        "Midas : Quoi?? HAHAHAHA",
        "  ",
    ]
    background_index = 56
    for text in texts:
        background_index = printf(text, background_index)
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render("Utiliser le colier", True, WHITE)
    option2 = menu_font.render("Ne pas utiliser le colier", True, WHITE)
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
                    scene2_midas_choix2_1()
                elif option2_rect.collidepoint(mouse_pos):
                    choice = '2'
                    scene2_midas_choix2_2()
                    
def scene2_midas_choix2_2() :
    texts = [
        "vous : Tu es comme ton frère, juste un monstre sans cerveau.",
        "Midas : Hmm, je peux sentir ta faiblesse.",
        "Midas : HAHAHAHAHA, ",
        "vous : Qu est-ce que tu dis? Je suis plus fort que toi.",
        "Midas : Ah, vraiment? Voici la potion devant toi, viens la prendre si tu oses.",
        "  ",
    ]
    background_index = 64
    for text in texts:
        background_index = printf(text, background_index)
    
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render("Utiliser le colier et prendre la potion", True, WHITE)
    option2 = menu_font.render("Ne pas utiliser le colier", True, WHITE)
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
                    scene2_midas_choix2_1()
                elif option2_rect.collidepoint(mouse_pos):
                    choice = '2'
                    scene2_midas_choix2_2_2()
                    
def scene2_midas_choix2_2_2() :
    texts = [
        "{ Tu t'es approché lentement de la potion. }",
        "Midas : HAHAHAHAH.",
        "Midas : Petit imbécile. ",
        "Midas : Rejoins mon frère et ta famille.",
        "vous : Nonnnn.",
        "  ",
    ]
    background_index = 65
    for text in texts:
        background_index = printf(text, background_index)
    
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render("Restart", True, WHITE)
    option2 = menu_font.render("Quit", True, WHITE)
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
                    scene2_midas_choix2_2()
                elif option2_rect.collidepoint(mouse_pos):
                    choice = '2'
                    pygame.quit()
                    sys.exit()                  
 
 
 
def scene2_midas_choix2_1() :
    texts = [
        "vous : Maintenant, je vais te montrer ce que ton frère m'a donné.",
        "Midas : Ne me fais pas me souvenir de ma famille.",
        "{ Midas Pleure }",
        "vous : C'est le moment où je vais l'utiliser.",
        "vous : Maintenant, meurs simplement et rejoins ton frère",
        "{À ce moment-là, Midas continue de se souvenir de sa famille et pleure toujours.}",
        "Midas : Que La Famille",
        "vous : Mais tu étais un si bon frère.",
        "{Tu as pris la potion et tu es parti}",
        "vous : Ces monstres ne sont pas si méchants, peut-être que Jane me ment à propos de ce monde?",
        "  ",
    ]
    background_index = 70
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
                    subprocess.call(["python", "game/Donjon de temp/after_donjon_temp.py"])                 
# Main function
def main():
    play_music()
    scene1()


if __name__ == "__main__":
    main()

# Quit pygame
pygame.quit()
sys.exit()
