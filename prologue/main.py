import pygame
import os
import sys
import subprocess

# Initialize Pygame and set up the display
pygame.init()
pygame.display.set_caption("Devided")
icon = pygame.image.load('game/prologue/logo.png')
pygame.display.set_icon(icon)
font = pygame.font.Font('freesansbold.ttf', 24)
screen = pygame.display.set_mode([1280, 720])
timer = pygame.time.Clock()

# Load images for each scene
images_dir = 'game/prologue/images'
images_list = []
for filename in os.listdir(images_dir):
    image_path = os.path.join(images_dir, filename)
    # Load the image and append it to the list
    image = pygame.image.load(image_path)
    images_list.append(image)

# Load music files
music_files = ["game/prologue/prologue.mp3"]
current_music_index = 0
pygame.mixer.music.load(music_files[current_music_index])

# Flag to check if music is playing
music_playing = False

# Function to play music
def play_music():
    global music_playing
    if not music_playing:
        pygame.mixer.music.play(start=0)  # Start from the beginning
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

# Function to change music
def change_music():
    global current_music_index
    current_music_index = (current_music_index + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_music_index])
    play_music()

# Start music playback initially
play_music()

messages = [['Jadis, dans un monde divisé entre deux races les humains et les monstres',
             'les frontières étaient strictes',
             'les humains ne pouvaient pas entrer dans le royaume des monstres et vice versa.'],      
            ['Le royaume des monstres s\'étendait dans les ténèbres, où régnaient l\'injustice et la tyrannie',
             'Leur monde était cruel, une terre où la peur régnait en maître'],
            ['Après des années de tension, une guerre éclata entre les deux camps',
             'la geurre a duré des mois.. des année ... des siècle...'],
            ['Finalement, les humains triomphèrent, scellant les monstres sous terre',
              'à l\'aide d\'un sortilège interdit',
              'ils avaient fait un pact avec les monstre de ne pas l\'utiliser',
               ' mais cela était néssecaire pour arreter la geurre'],
            ['Durant ces années de quiétude, la société humaine s\'est épanouie dans un cadre de sécurité ',
               'Les peurs et les tensions qui jadis pesaient sur les épaules des individus se sont dissipées',
               'laissant place à un sentiment général de confiance et de bien-être. Les communautés ont prospéré',
               'mais des légendes persistaient, notamment autour d\'une mystérieuse forêt.'],
            ['Les habitants du village affirmaient que cette forêt était hantée ',
                'et que quiconque s\'y aventurait n\'en revenait jamais'],
            ['...',
                 'cam : ...',
                 'cam : reveille t...'],
            ['cam : reveille toi ! papa t\'attend en bas',
                   'cam : papa est préssé fait vite'], 
                   ['..........'],
            ['(vous : j\'ai toujours fait des expiditions avec mon père mais cette fois... )',
                    '( vous : il avait l\'air d\'être très serieux... )',
                    '( vous : peut étre que cette expédition était dangereuse ?? )',
                    '( vous : je ne sais pas... je lui fait entièrment confiance )'],
            ['( vous : après avoir rejoint mon père nous somme partie en expidition dans une foret inconnue )',
                     '( vous : un seul manque d\'inatention et on se perdait dans la foret )',
                     '( vous : J\'ai essayé de le suivre mais... )'],
            ['( vous : Ce qui devait arriver arriva... )',
                      '( vous : moi et mon père on s\'est perdu de vue )',
                      '( vous : mais c\'est plus-tôt moi qui s\'est perdu car lui en revanche il avait la carte )',
                      '( vous : j\'ai essayé de le rejoindre mais... )'],
            ['( vous : je me suis coincé le pied dans des branche et ... )'],    
                       ['(vous : j\'ai trébucher et suis tomber dans l\'inconnue...',
                        ' je me suis évanouie pendant ma chute )'],
                       ['{vous vous reveilliez totalment boulversé par la situation}', 
                        '( vous : ou suis-je ? )'],
                        ['{vous trouvez une porte}',
                         '(vous : je vais essayer de l\'ouvrir malgré le risque)',
                         '.......'],
                         ['{en entrant dans la salle vous trouvez une sorte de fleur géante de dos }',
                          '(vous : dois-je lui parler ? )',
                          '(vous : je sais que c\'est risqué mais... je n\'ai pas d\'autres solution )',
                          'vous : Bon.... bonjour'],
                          ['??? : ahhh t\'es un nouveau ici je ne t\'ai jamais vu avant ',
                           '??? : je me présente moi c\'est fluffy',
                           'fluffy : tu a l\'air perdu ..',
                           'fluffy : quelqu\'un doit t\'apprendre comment ça marche ici ',
                           'fluffy : ici c\'est un monde magique ou tout ce dont tu révais est possible !',
                           'fluffy : pour commencer tu a ce qu\'on apelle les Hp eh bah c\'est t\'as santé',
                           'fluffy : il faut prendre soin de toi si t\'es hp décende a 0 tu peut dormir a tout jamais...',
                           'fluffy : regarde ton nombre d\'hp : 20 ',
                           'fluffy : il y\'as aussi ce qu\'on appelle le Level mais aussi ta progression',
                           'fluffy : plus tu avance dans ce monde plus tu gagne de l\'experience',
                           'fluffy : et en gagnant de l\'experience tu gagne des levels',
                           '...',
                           'fluffy : maintenant que tu en sais beaucoup plus je t\'invite a prendre ça',
                           'fluffy : c\'est une potion bois la elle te donnera de l\'experience et des point de vie',
                           '{vous buvez la potion}',
                           '...',
                           '{vos nombres d\'hp ont extrement diminué...}',],
                           ['fluffy : HAHAHAHAHAHAAHA ', #son ta3 rire ak ta3ref + tswira ta3 wetcho mbedel yweli yekhla3
                            'fluffy : IMBECILE !',
                            'fluffy : DANS CE MONDE C\'EST TUER OU ETRE TUER',
                            'fluffy : MEURS HAHAHAHAHA',
                            '{vous tombez dans les vapes....}'],
                            ['...',#ecran noir
                             '??? : réveillez vous...'],
                             ['???? : t\'es enfin reveiller ?',#tswira ta3 jane
                              '???? : je comprend t\'es perdu un peu , moi c\'est jane et toi ?',
                              'vous : ...',
                              'jane : je comprend... après ce que tu a vécu tu est bouversé par la situation',
                              'jane : disons que tu es tombé dans une forêt magique',
                              'jane : et dans cette grotte réside le monde des monstres..',
                              'jane : ou jadis vous les humains vous nous avez scellé sous-terre avec un sortilège interdit',
                              'vous : je croyais que c\'était un conte de fée qu\'on racontait au enfant pour qu\'ils dorment la nuit',
                              'jane : non c\'est la triste réalité',
                              'jane : bon je suppose que tu veut sortir d\'ici retrouvez ton père...',
                              'vous : comment sait tu que je suis venu avec mon père ..',
                              'jane : je sais beaucoup de chose sur toi...',
                              'jane : bon, pour sortir il te faut trouver 3 artéfact'],
                              ['jane : 1. Le Collier de Feu  || 2. L\'Élixir du Temps || 3. La Pierre du savoir'], #tswira ta3 les 3 artéfact
                              ['jane : la personne malvaillante que  tu a croiser tout a l\'heure possedait un artéfact Le collier du feu !',
                               'vous : et les autres détenteur d\'artéfact tu les connais ? ', #tswira ta3 jane
                               'jane : celui qui détient l\'élixir du temp s\'apelle Midas',
                               'jane : et la détenteuse de la pièrre de savoir... je ne la connais pas',
                               '(vous : elle semble mentir elle doit la connaitre)',
                               'vous : bon je dois partir les cherchez ! ',
                               'jane : ohhh tu ne perd pas de temp !',
                               'jane : ...',
                               'jane : je vais te dire un secret',
                               'jane : je suis ce qu\'on apelle une sainte',
                               'jane : il y\'en a plein comme moi tu peut leurs faire confiance elle peuvent réstaurer t\'es point de vie',
                               'jane : regarde...'],
                               ['...'],#tswira ta3 jane dir haja ki chgrol heal
                               ['vous : je me sens beaucoup mieux !!',#retour sur la meme photo de jane
                                '{vos point de vie on été rétablie}',
                                'vous : merci beaucoup !',
                                'jane : si tu veut rester ici tu sera toujour le bienvenue',
                                'jane : je te souhaite bonne chance pour retrouvez t\'es parents'],
                                ['{vous vous reveilliez et partez a l\'opossé d\'ou se trouve jane}',
                                 '...',
                                 '( vous : je vais découvrir ce monde...)',
                                 '(vous :  mais je dois chercher les artéfact pour retrouver mon père et ma famille)'],#écran noir
                                ['vous : je vais commencez avec ce donjon de feu je vais régler le compte a ce fluffy ! '],
                                [' '],]                                

snip = font.render('', True, 'white')
counter = 0
speed = 3
done = False
active_message = 0
run = True

scene = 0

while run:
    screen.fill('black')

    # Check if the scene is within bounds
    if 0 <= scene < len(messages):
        # Display images for the current scene
        if scene < len(images_list):
            screen.blit(images_list[scene], (0, 0))

        pygame.draw.rect(screen, (0, 0, 0), [0, 625, 1280, 300])

        message = messages[scene][active_message]  # Active message selection
        if counter < speed * len(message):
            counter += 1
        elif counter >= speed * len(message):
            done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done:
                    if active_message < len(messages[scene]) - 1:
                        active_message += 1
                        done = False
                        counter = 0
                    elif scene < len(messages) - 1:
                        scene += 1
                        active_message = 0
                        done = False
                        counter = 0
                elif event.key == pygame.K_p:
                    pause_music()
                elif event.key == pygame.K_u:
                    unpause_music()
                elif event.key == pygame.K_s:
                    stop_music()
                elif event.key == pygame.K_m:
                    change_music()

        snip = font.render(message[:counter // speed], True, (255, 255, 255))
        screen.blit(snip, (50, 650))

    pygame.display.flip()
    timer.tick(60)
stop_music()
subprocess.call(["python", "game/Donjon de deu/donjon_feu.py"])
pygame.quit()
sys.exit()
