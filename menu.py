import pygame
import sys
import math
import threading
import pygame_menu as pm
import subprocess

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

WIDTH, HEIGHT = 1280, 720

icon_image = pygame.image.load("image/logo.png")
pygame.display.set_icon(icon_image)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Divided")

clock = pygame.time.Clock()
fps = 60

FONT = pygame.font.Font("Font/BLKCHCRY.TTF", 100)

# Clock
CLOCK = pygame.time.Clock()

# Work
WORK = 190000009

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 100, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

bg = pygame.image.load("image/img1.png").convert()
bg_width = bg.get_width()

scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1

custom_font = pygame.font.Font("Font/BLKCHCRY.TTF", 80)
custom_font1 = pygame.font.Font("Font/BLKCHCRY.TTF", 48)

# Loading BG
LOADING_BG = pygame.image.load("image/Loading Bar Background.png")
LOADING_BG_RECT = LOADING_BG.get_rect(center=(640, 360))

# Loading Bar and variables
loading_bar = pygame.image.load("image/Loading Bar.png")
loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))
loading_finished = False
loading_progress = 0
loading_bar_width = 0

def main():
    graphics = [("Low", "low"),
                ("Medium", "medium"),
                ("High", "high"),
                ("Ultra High", "ultra high")]

    resolution = [("1920x1080", "1920x1080"),
                  ("1920x1200", "1920x1200"),
                  ("1280x720", "1280x720"),
                  ("2560x1440", "2560x1440"),
                  ("3840x2160", "3840x2160")]

    difficulty = [("Easy", "Easy"),
                  ("Medium", "Medium"),
                  ("Expert", "Expert")]

    perspectives = [("FPP", "fpp"),
                    ("TPP", "tpp")]

    def printSettings():
        print("\n\n")
        settingsData = settings.get_input_data()
        for key in settingsData.keys():
            print(f"{key}\t:\t{settingsData[key]}")

    settings = pm.Menu(title="Settings",
                       width=WIDTH,
                       height=HEIGHT,
                       theme=pm.themes.THEME_GREEN)

    settings._theme.widget_font_size = 25
    settings._theme.widget_font_color = BLACK
    settings._theme.widget_alignment = pm.locals.ALIGN_LEFT

    settings.add.text_input(title="User Name : ", textinput_id="username")

    settings.add.dropselect(title="Graphics Level", items=graphics,
                            dropselect_id="graphics level", default=0)
    settings.add.dropselect_multiple(title="Window Resolution", items=resolution,
                                     dropselect_multiple_id="Resolution",
                                     open_middle=True, max_selected=1,
                                     selection_box_height=6)

    settings.add.toggle_switch(
        title="Music", default=True, toggleswitch_id="music")
    settings.add.toggle_switch(
        title="Sounds", default=False, toggleswitch_id="sound")

    settings.add.selector(title="Difficulty\t", items=difficulty,
                          selector_id="difficulty", default=0)

    settings.add.range_slider(title="FOV", default=60, range_values=(
        50, 100), increment=1, value_format=lambda x: str(int(x)), rangeslider_id="fov")

    settings.add.selector(title="Perspective", items=perspectives,
                          default=0, style="fancy", selector_id="perspective")

    settings.add.clock(clock_format="%d-%m-%y %H:%M:%S",
                       title_format="Local Time : {0}")

    settings.add.button(title="Print Settings", action=printSettings,
                        font_color=WHITE, background_color=GREEN)
    settings.add.button(title="Restore Defaults", action=settings.reset_value,
                        font_color=WHITE, background_color=RED)
    settings.add.button(title="Return To Main Menu",
                        action=pm.events.BACK, align=pm.locals.ALIGN_CENTER)

    settings.mainloop(screen)

def draw_text(text, font, colors, surface, x, y):
    rendered_chars = []
    total_width = 0
    for char, color in zip(text, colors):
        char_rendered = font.render(char, 1, color)
        rendered_chars.append(char_rendered)
        total_width += char_rendered.get_width()

    offset_x = x - total_width // 2
    for char_rendered in rendered_chars:
        surface.blit(char_rendered, (offset_x, y))
        offset_x += char_rendered.get_width()

def doWork():
    global loading_finished, loading_progress
    for i in range(WORK):
        math_equation = 523687 / 789456 * 89456
        loading_progress = i
    loading_finished = True

def main_menu():
    global scroll
    while True:
        clock.tick(fps)
        for i in range(0, tiles):
            screen.blit(bg, (i * bg_width + scroll, 0))

        scroll -= 1.5

        if abs(scroll) > bg_width:
            scroll = 0

        draw_text("Divided", custom_font, [WHITE, RED, WHITE, WHITE, WHITE, WHITE, WHITE], screen, SCREEN_WIDTH // 2, 100)
        draw_text("Main Menu", custom_font1, [WHITE, WHITE, WHITE, WHITE, BLACK, WHITE, WHITE, WHITE, WHITE], screen, SCREEN_WIDTH // 2, 225)
        menu_font = pygame.font.Font("Font/BLKCHCRY.TTF", 40)
        option1 = menu_font.render("Start Game", True, WHITE)
        option4 = menu_font.render("Exit", True, WHITE)

        option1_rect = option1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        option4_rect = option4.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))

        screen.blit(option1, option1_rect)
        screen.blit(option4, option4_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if option1_rect.collidepoint(mouse_pos):
                    try:
                        pygame.mixer.music.stop()  # Stop playing the song
                        subprocess.call(["python", "game/prologue/main.py"])
                    except Exception as e:
                        print("Error while executing prologue script:", e)
                    pygame.quit()
                    sys.exit()
                elif option4_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

finished = FONT.render("Press Enter!", True, "white")
finished_rect = finished.get_rect(center=(640, 360))

threading.Thread(target=doWork).start()

menu_song = r"song/menu_song.mp3"

def play_song_menu(song_file):
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(song_file)
        print("Playing:", song_file)
        pygame.mixer.music.play()
    except pygame.error as e:
        print("An error occurred:", e)

play_song_menu(menu_song)
settings_menu_active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if not settings_menu_active:
                    main_menu()
                else:
                    settings.mainloop(screen)

    screen.fill("#0d0e2e")

    if not loading_finished:
        loading_bar_width = loading_progress / WORK * 720
        loading_bar_scaled = pygame.transform.scale(loading_bar, (int(loading_bar_width), 150))
        loading_bar_rect = loading_bar_scaled.get_rect(midleft=(280, 360))
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        screen.blit(loading_bar_scaled, loading_bar_rect)
    else:
        screen.blit(LOADING_BG, LOADING_BG_RECT)
        screen.blit(finished, finished_rect)

    pygame.display.update()
    CLOCK.tick(60)

    if settings_menu_active:
        settings.mainloop(screen)
