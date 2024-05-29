import pygame
import os
import sys

# Initialize Pygame and set up the display
pygame.init()
pygame.display.set_caption("Devided")
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

# Load music files
music_files = ["prologue.mp3"]
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

def main():
    font = pygame.font.Font('freesansbold.ttf', 24)
    screen = pygame.display.set_mode([1280, 720])
    timer = pygame.time.Clock()

    # Load images for each scene
    images_dir = 'images'
    images_list = []
    for filename in os.listdir(images_dir):
        image_path = os.path.join(images_dir, filename)
        # Load the image and append it to the list
        image = pygame.image.load(image_path)
        images_list.append(image)

    messages = [['Jadis, dans un monde divisé entre deux races les humains et les monstres',
                 'les frontières étaient strictes',
                 'les humains ne pouvaient pas entrer dans le royaume des monstres et vice versa.'],      
                ['Le royaume des monstres s\'étendait dans les ténèbres, où régnaient l\'injustice et la tyrannie',
                 'Leur monde était cruel, une terre où la peur régnait en maître'],
                ['Après des années de tension, une guerre éclata entre les deux camps',
                 'la guerre a duré des mois... des années... des siècles...'],
                ['Finalement, les humains triomphèrent, scellant les monstres sous terre',
                  'à l\'aide d\'un sortilège interdit',
                  'ils avaient fait un pacte avec les monstres de ne pas l\'utiliser',
                   'mais cela était nécessaire pour arrêter la guerre'],
                ['Durant ces années de quiétude, la société humaine s\'est épanouie dans un cadre de sécurité ',
                   'Les peurs et les tensions qui jadis pesaient sur les épaules des individus se sont dissipées',
                   'laissant place à un sentiment général de confiance et de bien-être. Les communautés ont prospéré',
                   'mais des légendes persistaient, notamment autour d\'une mystérieuse forêt.'],
                ['Les habitants du village affirmaient que cette forêt était hantée ',
                    'et que quiconque s\'y aventurait n\'en revenait jamais'],
                ['...',
                     'cam : ...',
                     'cam : réveille-toi...'],
                ['cam : réveille-toi ! papa t\'attend en bas',
                       'cam : papa est pressé fait vite'], 
                       ['..........'],
                ['(vous : j\'ai toujours fait des expéditions avec mon père mais cette fois... )',
                        '( vous : il avait l\'air d\'être très sérieux... )',
                        '( vous : peut-être que cette expédition était dangereuse ?? )',
                        '( vous : je ne sais pas... je lui fais entièrement confiance )'],
                ['( vous : après avoir rejoint mon père nous sommes partis en expédition dans une forêt inconnue )',
                         '( vous : un seul manque d\'inattention et on se perdait dans la forêt )',
                         '( vous : J\'ai essayé de le suivre mais... )'],
                ['( vous : Ce qui devait arriver arriva... )',
                          '( vous : moi et mon père on s\'est perdu de vue )',
                          '( vous : mais c\'est plutôt moi qui s\'est perdu car lui en revanche il avait la carte )',
                          '( vous : j\'ai essayé de le rejoindre mais... )'],
                ['( vous : je me suis coincé le pied dans des branches et ... )'],    
                           ['(vous : j\'ai trébuché et suis tombé dans l\'inconnue...',
                            ' je me suis évanoui pendant ma chute )'],
                           ['{vous vous réveillez totalement bouleversé par la situation}', 
                            '( vous : où suis-je ? )'],
                            ['{vous trouvez une porte}',
                             '(vous : je vais essayer de l\'ouvrir malgré le risque)',
                             '.......'],
                             ['{en entrant dans la salle vous trouvez une sorte de fleur géante de dos }',
                              '(vous : dois-je lui parler ? )',
                              '(vous : je sais que c\'est risqué mais... je n\'ai pas d\'autres solutions )',
                              'vous : Bon.... bonjour'],
                              ['??? : ahhh t\'es un nouveau ici je ne t\'ai jamais vu avant ',
                               '??? : je me présente moi c\'est fluffy',
                               'fluffy : tu as l\'air perdu ..',
                               'fluffy : quelqu\'un doit t\'apprendre comment ça marche ici ',
                               'fluffy : ici c\'est un monde magique où tout ce dont tu rêvais est possible !',
                               'fluffy : pour commencer tu as ce qu\'on appelle les Hp eh bah c\'est ta santé',
                               'fluffy : il faut prendre soin de toi si tes hp descendent à 0 tu peux dormir à tout jamais...',
                               'fluffy : regarde ton nombre d\'hp : 20 ',
                               'fluffy : il y a aussi ce qu\'on appelle le Level mais aussi ta progression',
                               'fluffy : plus tu avances dans ce monde plus tu gagnes de l\'expérience',
                               'fluffy : et en gagnant de l\'expérience tu gagnes des levels',
                               '...',
                               'fluffy : maintenant que tu en sais beaucoup plus je t\'invite à prendre ça',
                               'fluffy : c\'est une potion bois-la elle te donnera de l\'expérience et des points de vie',
                               '{vous buvez la potion}',
                               '...',
                               '{vos nombres d\'hp ont extrêmement diminué...}',],
                               ['fluffy : HAHAHAHAHAHAAHA ', #son ta3 rire ak ta3ref + tswira ta3 wetcho mbedel yweli yekhla3
                                'fluffy : IMBÉCILE !',
                                'fluffy : DANS CE MONDE C\'EST TUER OU ÊTRE TUÉ',
                                'fluffy : MEURS HAHAHAHAHA',
                                '{vous tombez dans les vapes....}'],
                                ['...',#ecran noir
                                 '??? : réveillez-vous...'],
                                 ['???? : t\'es enfin réveillé ?',#tswira ta3 jane
                                  '???? : je comprends t\'es perdu un peu , moi c\'est jane et toi ?',
                                  'vous : ...',
                                  'jane : je comprends... après ce que tu as vécu tu es bouleversé par la situation',
                                  'jane : disons que tu es tombé dans une forêt magique',
                                  'jane : et dans cette grotte réside le monde des monstres..',
                                  'jane : où jadis vous les humains nous avez scellé sous terre avec un sortilège interdit',
                                  'vous : je croyais que c\'était un conte de fée qu\'on racontait aux enfants pour qu\'ils dorment la nuit',
                                  'jane : non c\'est la triste réalité',
                                  'jane : bon je suppose que tu veux sortir d\'ici retrouver ton père...',
                                  'vous : comment sais-tu que je suis venu avec mon père ..',
                                  'jane : je sais beaucoup de choses sur toi...',
                                  'jane : bon, pour sortir il te faut trouver 3 artefacts'],
                                  ['jane : 1. Le Collier de Feu  || 2. L\'Élixir du Temps || 3. La Pierre du savoir'], #tswira ta3 les 3 artéfact
                                  ['jane : la personne malveillante que tu as croisée tout à l\'heure possédait un artefact Le collier du feu !',
                                   'vous : et les autres détenteurs d\'artefact tu les connais ? ', #tswira ta3 jane
                                   'jane : celui qui détient l\'élixir du temps s\'appelle Midas',
                                   'jane : et la détentrice de la pierre de savoir... je ne la connais pas',
                                   '(vous : elle semble mentir elle doit la connaître)',
                                   'vous : bon je dois partir les chercher ! ',
                                   'jane : ohhh tu ne perds pas de temps !',
                                   'jane : ...',
                                   'jane : je vais te dire un secret',
                                   'jane : je suis ce qu\'on appelle une sainte',
                                   'jane : il y en a plein comme moi tu peux leur faire confiance elles peuvent restaurer tes points de vie',
                                   'jane : regarde...'],
                                   ['{vos hp ont été restauré...}',#son ta3 healing ta3 minecraft
                                    'jane : oh fait attention à toi et n\'oublie pas 20 hp c\'est peu',
                                    'jane : à bientôt je te surveille ..',
                                    '......',
                                    '(vous : elle est trop bizarre)']]
 
    current_scene = 0  # Start from the first scene

    # Start music playback initially
    play_music()

    # Game loop
    running = True
    while running:
        screen.fill((0, 0, 0))  # Clear the screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    if current_scene < len(images_list) - 1:
                        current_scene += 1
                    else:
                        current_scene = 0
                elif event.key == pygame.K_p:
                    pause_music()
                elif event.key == pygame.K_u:
                    unpause_music()
                elif event.key == pygame.K_s:
                    stop_music()
                elif event.key == pygame.K_m:
                    change_music()

        # Display the current image and messages
        image = images_list[current_scene]
        screen.blit(image, (0, 0))
        text_y = 50
        for message in messages[current_scene]:
            text_surface = font.render(message, True, (255, 255, 255))
            screen.blit(text_surface, (50, text_y))
            text_y += 30

        pygame.display.flip()
        timer.tick(60)

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
