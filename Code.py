import pygame
import sys
from button import Button

pygame.init()

WIDTH, HEIGHT = 1900, 1050
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pomodoro Timer")
CLOCK = pygame.time.Clock()
BACKDROP = pygame.image.load("D:\VS Studio\Python on VS Studio\Projects\PomodoroTimer/backdrop.png")
WHITE_BUTTON = pygame.image.load("D:\VS Studio\Python on VS Studio\Projects\PomodoroTimer/button.png")
FONT = pygame.font.Font("D:\VS Studio\Python on VS Studio\Projects\SpaceInvaders/Gametext.ttf", 120)
timer_text = FONT.render("25:00", True, "white")
timer_text_rect = timer_text.get_rect(center = (WIDTH / 2, HEIGHT / 2-25))
START_STOP_BUTTON = Button(WHITE_BUTTON, (WIDTH / 2, HEIGHT / 2 + 100), 170, 60, "START", pygame.font.Font("D:\VS Studio\Python on VS Studio\Projects\SpaceInvaders/Gametext.ttf", 25), "#000000", "#3F48CC")
POMODORO_BUTTON = Button(WHITE_BUTTON, (WIDTH / 2 - 200, HEIGHT / 2 - 135), 120, 30, "Pomodoro", pygame.font.Font("D:\VS Studio\Python on VS Studio\Projects\SpaceInvaders/Gametext.ttf", 25), "#000000", "#3F48CC")
SHORT_BREAK_BUTTON = Button(WHITE_BUTTON, (WIDTH / 2 - 65, HEIGHT / 2 - 135), 120, 30, "Short Break", pygame.font.Font("D:\VS Studio\Python on VS Studio\Projects\SpaceInvaders/Gametext.ttf", 25), "#000000", "#3F48CC")
LONG_BREAK_BUTTON = Button(WHITE_BUTTON, (WIDTH / 2 + 65, HEIGHT / 2 - 135), 120, 30, "Long Break", pygame.font.Font("D:\VS Studio\Python on VS Studio\Projects\SpaceInvaders/Gametext.ttf", 25), "#000000", "#3F48CC")
LONG_POMODORO_BUTTON = Button(WHITE_BUTTON, (WIDTH / 2 + 210, HEIGHT / 2 - 135), 150, 30, "Long Pomodoro", pygame.font.Font("D:\VS Studio\Python on VS Studio\Projects\SpaceInvaders/Gametext.ttf", 25), "#000000", "#3F48CC")
POMODORO_LENGTH = 1500 
SHORT_BREAK_LENGTH = 300 
LONG_BREAK_LENGTH = 600 
LONG_POMODORO_LENGTH = 3000

current_seconds = POMODORO_LENGTH
pygame.time.set_timer(pygame.USEREVENT, 1000)
started = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if START_STOP_BUTTON.check_for_input(pygame.mouse.get_pos()):
                if started:
                    started = False
                else:
                    started = True
            if POMODORO_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = POMODORO_LENGTH
                started = False
            if SHORT_BREAK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = SHORT_BREAK_LENGTH
                started = False
            if LONG_BREAK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = LONG_BREAK_LENGTH
                started = False
            if LONG_POMODORO_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = LONG_POMODORO_LENGTH
                started = False
            if started:
                START_STOP_BUTTON.text_input = "STOP"
                START_STOP_BUTTON.text = pygame.font.Font("D:\VS Studio\Python on VS Studio\Projects\SpaceInvaders/Gametext.ttf", 20).render(
                                        START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
            else:
                START_STOP_BUTTON.text_input = "START"
                START_STOP_BUTTON.text = pygame.font.Font("D:\VS Studio\Python on VS Studio\Projects\SpaceInvaders/Gametext.ttf", 20).render(
                                        START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
        if event.type == pygame.USEREVENT and started:
            current_seconds -= 1

    SCREEN.fill("#3F48CC")
    SCREEN.blit(BACKDROP, BACKDROP.get_rect(center=(WIDTH/2, HEIGHT/2)))

    START_STOP_BUTTON.update(SCREEN)
    START_STOP_BUTTON.change_color(pygame.mouse.get_pos())
    POMODORO_BUTTON.update(SCREEN)
    POMODORO_BUTTON.change_color(pygame.mouse.get_pos())
    SHORT_BREAK_BUTTON.update(SCREEN)
    SHORT_BREAK_BUTTON.change_color(pygame.mouse.get_pos())
    LONG_BREAK_BUTTON.update(SCREEN)
    LONG_BREAK_BUTTON.change_color(pygame.mouse.get_pos())
    LONG_POMODORO_BUTTON.update(SCREEN)
    LONG_POMODORO_BUTTON.change_color(pygame.mouse.get_pos())

    if current_seconds >= 0:
        display_seconds = current_seconds % 60
        display_minutes = int(current_seconds / 60) % 60
    timer_text = FONT.render(f"{display_minutes:02}:{display_seconds:02}", True, "white")
    SCREEN.blit(timer_text, timer_text_rect)

    pygame.display.update()