import pygame

def play_song(song_file):
    pygame.init()
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(song_file)
        print("Playing:", song_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except pygame.error as e:
        print("An error occurred:", e)
    finally:
        pygame.mixer.music.stop()
        pygame.quit()

if __name__ == "__main__":
    song_file = "C:/Users/HP/Downloads/Resident Evil 7 Intro ● 4K.mp3"
    play_song(song_file)
