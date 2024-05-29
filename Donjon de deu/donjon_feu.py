import pygame
import sys
import subprocess
# Initialize pygame
pygame.init()

# Set up the display
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Divided")

# Load the background images
background_images = [
    pygame.image.load("game/Donjon de deu/images/a_garde_donjon.png").convert(),#0
    pygame.image.load("game/Donjon de deu/images/a_garde_donjon.png").convert(),
    pygame.image.load("game/Donjon de deu/images/a_garde_donjon.png").convert(),
    pygame.image.load("game/Donjon de deu/images/a_garde_donjon.png").convert(),
    pygame.image.load("game/Donjon de deu/images/a_garde_donjon.png").convert(),
    pygame.image.load("game/Donjon de deu/images/a_garde_donjon.png").convert(),
    pygame.image.load("game/Donjon de deu/images/a_garde_donjon.png").convert(),
    pygame.image.load("game/Donjon de deu/images/a_garde_donjon.png").convert(),
    pygame.image.load("game/Donjon de deu/images/a_garde_donjon.png").convert(),
    pygame.image.load("game/Donjon de deu/images/a_garde_donjon.png").convert(),
    pygame.image.load("game/Donjon de deu/images/a_garde_donjon.png").convert(),#10
    pygame.image.load("game/Donjon de deu/images/a_garde_donjon.png").convert(),
    pygame.image.load("game/Donjon de deu/images/a_garde_donjon.png").convert(),
    pygame.image.load("game/Donjon de deu/images/a_garde_donjon.png").convert(),
    pygame.image.load("game/Donjon de deu/images/a_garde_donjon.png").convert(),#14    # Add more frames if needed
    pygame.image.load("game/Donjon de deu/images/b_garde_laisse_entrer.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/c_fluffy_donjon_feu.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/c_fluffy_donjon_feu.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/c_fluffy_donjon_feu.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/c_fluffy_donjon_feu.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/c_fluffy_donjon_feu.jpg").convert(),#20
    pygame.image.load("game/Donjon de deu/images/c_fluffy_donjon_feu.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/c_fluffy_donjon_feu.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/c_fluffy_donjon_feu.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/c_fluffy_donjon_feu.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),#25
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),#30
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/black.jpg").convert(),#34
    pygame.image.load("game/Donjon de deu/images/black.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/black.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/black.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/black.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),#40
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/black.jpg").convert(),#43
    pygame.image.load("game/Donjon de deu/images/f.png").convert(),
    pygame.image.load("game/Donjon de deu/images/f.png").convert(),
    pygame.image.load("game/Donjon de deu/images/f.png").convert(),
    pygame.image.load("game/Donjon de deu/images/f.png").convert(),
    pygame.image.load("game/Donjon de deu/images/f.png").convert(),
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),#50
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),#51
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/d_fluffy_sourire_démonique.jpg").convert(),
    pygame.image.load("game/Donjon de deu/images/ff.png").convert(),
    pygame.image.load("game/Donjon de deu/images/ff.png").convert(),
    pygame.image.load("game/Donjon de deu/images/ff.png").convert(),
    pygame.image.load("game/Donjon de deu/images/ff.png").convert(),
    pygame.image.load("game/Donjon de deu/images/ff.png").convert(),
    

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
music_files = ["game/Donjon de deu/a.mp3"]
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
        "{en arrivant devant la porte du donjon vous trouvez un garde}",
        "????? : que faites vous ici Humain",
        "vous : je cherche fluffy",
        "????? : fluffy ? hahahahaha le roi de ce donjon",
        "????? : malheureusment tu ne peut pas entré dans ce donjon",
        "????? : a moin que tu réponde a mon énigme ",
        "vous : D'accord je suis prèt a tout pour retrouver fluffy",
        "...",
        "????? :Dans les flammes éternelles, je suis enchaîné",
        "????? : Ma chaleur brûlante, jamais elle ne faiblit.",
        "????? : Les pécheurs redoutent ma fureur ardente",
        "????? : Mais certains disent que je suis le remède à leur tourment.",
        "????? : Suis-je le brasier de l'enfer : 1 || ou le souffle du démon : 2 ?",
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
        "???? : bonne réponse tu est donc digne de rentré dans ce donjon",
        "...",
        "vous : ouff j'ai eu de la chance",
    ]
    background_index = 13
    for text in texts:
        background_index = printf(text, background_index)


def scene1_choix2():
    texts = [
        "???? : mauvaise réponse !",
        "???? : tu n'as pas le droit de rentré dans ce donjon ",
        "vous : hien comment ça !!!!!!!",
        "vous : j'ai promis a jane de sortir d'ici c'est pas toi qui va m'arreter ",
        "???? : hien ? tu as bien dit jane ",
        "???? : tu la connais d'ou ?!",
        "vous : peut-importe laisse moi rentrer ",
        "???? : si c'est jane qui vous envoie je ne peut refusé ",
        "...",
        "vous : ouff j'ai eu de la chance",
    ]
    background_index = 6
    for text in texts:
        background_index = printf(text, background_index)

def scene2():
    texts = [
        "{en entrant dans le donjon vous voyez fluffy de loin avec un grand sourire ...}",
        "vous :  flu.. fluffy ?",
        "fluffy : hien c'est toi ??",
        "fluffy : mais comment ça se fait ? je t'avais pourtant achevé..",
        "vous :  on va dire que j'ai eu un peu de chance...",
        "vous : je suis vennu prendre ton collier de feu",
        "fluffy : hien ? comment tu sais ? ",
        "fluffy : tu connais un roi de donjon ???",
        "fluffy : peu importe...",
        "fluffy : JE VAIS DEVOIR TE TUER MAINTENAT !!!",
        "choix 1 : tuer fluffy                 choix 2 : l'épargner",
        "  ",
    ]
    background_index = 16  # Initial background index
    
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
                    scene2_choix1()
                elif option2_rect.collidepoint(mouse_pos):
                    choice = '2'
                    scene2_choix2()


def scene2_choix1() :
    texts = [
        "vous : tu as essayé de me tuer la première fois....",
        "vous : je vais te traiter comme tu a fait avec moi !",
        "vous : je vais te tuer et prendre le collier",
        "vous : FAIT T'ES ADIEUX",
    ]
    background_index = 27
    for text in texts:
        background_index = printf(text, background_index)

def scene2_choix2() :
    texts = [
        "vous : tu as essayé de me tuer la première fois....",
        "vous : J'aurais pu te traiter comme tu as fait avec moi mais...",
        "vous : je n'ai pas été élevé pour être un monstre.",
        "vous : je vais juste te prendre ton collier et te laisse en vie",
        "vous : PRÉPARE TOI TU VA ME LE PAYER CHÈRE ! ",
    ]
    background_index = 26
    for text in texts:
        background_index = printf(text, background_index)


def fight_choix1():
    texts = [
        "vous : Je n'ai qu'un dernier souhait.",
        "vous : Dans ma tradition familiale, quand quelqu'un va mourir",
        "vous : nous donnons une fleur à la dernière personne qu'il voit.",
        "vous : Peux-tu prendre cette fleur pour moi ?",
        "fluffy : Non, je déteste tous les humains.",
        "vous : Prends-la puis tue-moi. J'ai tout perdu.",
        "fluffy : Oh, gamin, j'ai dit non donc non.",
        "vous : hmm...",
        "vous : Je vais jeter la fleur à Fluffy, et tout envoyer valser.",
        "vous : Prends-la.",
        "{La fleur explose et absorbe tout le pouvoir de Fluffy.}",
        "vous : Maintenant, la mort est ton destin.",
        "vous : Dors pour longtemps.",
        " ",
    ]
    
    
    background_index = 51  # Initial background index
    
    for text in texts:
        background_index = printf(text, background_index)  # Pass the background index to the printf function
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
                    subprocess.call(["python", "game/Donjon de deu/after_fight_fluffy.py"])
                    
                    
                    
                        
def fight_choix2():
    texts = [
         "vous : Avec 40 HP, je vais te tuer et faire de ce donjon ta tombe.",
         "fluffy : Oh vraiment, montre-moi de quoi tu es capable",
         "{Tu as sauté sur Fluffy}",
         "vous : Meuuuuuuuuuuuuuurs !",
         "fluffy : HAHAHAHAHAHA",
         "fluffy : Tu es mort maintenant",
         "vous : Quois !!",
         "{0 HP}",
         "fluffy : HAHAHAHAHAHAHA",
         " ",
     ]
    background_index = 25
    for text in texts:
        background_index = printf(text, background_index)  # Pass the background index to the printf function
        
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
                    fight_scene1()
                elif option2_rect.collidepoint(mouse_pos):
                    choice = '2'
                    pygame.quit()
                    sys.exit()  
def fight_scene1():
    texts = [
        "fluffy : Me tuer, vraiment.",
        "fluffy : Tu es tellement un insecte devant moi.",
        "fluffy : J'ai le pouvoir, toi tu n'as rien.",
        "fluffy : Maintenant, tu as 40 HP, gamin.",
        "{En cet instant précis ...}",
        "{il réalisa qu'il n'avait pas le pouvoir de tuer Fluffy.}",
        "vous : ... ",
        "vous : Que puis-je faire maintenant ?",
        "vous : Pense, pense, je suis à la porte de la mort.",
        "fluffy : HAHAHAHAHA",
        "fluffy : C'est maintenant le moment. HAHAHAHA",
        "fluffy : Des derniers mots, gamin ?",
        "{En ce moment, Tu te rappelles qu'il y a six ans.} ",
        "{ton père t'a offert une fleur et t'a recommandé d'en prendre soin.}",
        "{Ton père a dit : cette fleur a un tel pouvoir magique}",
        "{Qu'elle peut t'aider quand tu te rends compte que tu es mort.}",
        "{Pour l'utiliser, donne-la à ton ennemi.}",
        "{Utilise-la avec sagesse.}",
        "fluffy : Gamin, tu es étouffé ou quoi ? Au revoir.",
        " ",
        
    ]
    background_index = 30  # Initial background index
    
    for text in texts:
        background_index = printf(text, background_index)  # Pass the background index to the printf function
        
    menu_font = pygame.font.Font(None, 40)
    option1 = menu_font.render("Utilise la fleur", True, WHITE)
    option2 = menu_font.render("Ne pas utiliser la fleur", True, WHITE)
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
                    fight_choix1()
                elif option2_rect.collidepoint(mouse_pos):
                    choice = '2'
                    fight_choix2()


# Main function
def main():
    play_music()
    scene1()
    scene2()
    fight_scene1()

if __name__ == "__main__":
    main()

# Quit pygame
pygame.quit()
sys.exit()
