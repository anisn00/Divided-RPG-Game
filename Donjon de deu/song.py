import pygame
import os
import sys

# Initialize Pygame
pygame.init()

# Set up the display
pygame.display.set_caption("Divided")
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode([1280, 720])

# Load and play background music
music_files = ["a.mp3"]
current_music_index = 0
pygame.mixer.music.load(music_files[current_music_index])
pygame.mixer.music.play(-1)  # Play the music in a loop

# Load font
font = pygame.font.Font('freesansbold.ttf', 24)

# Load images for each scene
images_dir = 'images'
images_list = []
for filename in os.listdir(images_dir):
    image_path = os.path.join(images_dir, filename)
    image = pygame.image.load(image_path)
    images_list.append(image)

# Messages for each scene
messages = [
    ['Jadis, dans un monde divisé entre deux races les humains et les monstres...',
     'les frontières étaient strictes...',
     'les humains ne pouvaient pas entrer dans le royaume des monstres et vice versa.'],
    # ... Add all other message arrays here ...
]

# Function to change music
def change_music():
    global current_music_index
    current_music_index = (current_music_index + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_music_index])
    pygame.mixer.music.play()

# Main game loop
def main():
    timer = pygame.time.Clock()
    counter = 0
    speed = 3
    done = False
    active_message = 0
    scene = 0
    run = True

    while run:
        screen.fill('black')

        # Display the current scene image
        if scene < len(images_list):
            screen.blit(images_list[scene], (0, 0))

        # Draw the message box
        pygame.draw.rect(screen, (0, 0, 0), [0, 625, 1280, 300])

        # Get the current message
        message = messages[scene][active_message]
        if counter < speed * len(message):
            counter += 1
        elif counter >= speed * len(message):
            done = True

        # Event handling
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

        # Render the current message
        snip = font.render(message[:counter // speed], True, (255, 255, 255))
        screen.blit(snip, (50, 650))

        pygame.display.flip()
        timer.tick(60)

        # Stop music if the last scene is reached
        if scene == len(messages) - 1:
            pygame.mixer.music.stop()

# Run the game
main()

# Quit Pygame and exit the program
pygame.quit()
sys.exit()
