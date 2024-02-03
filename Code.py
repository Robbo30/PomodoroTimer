import pygame
import sys
from button import Button

pygame.init()

WIDTH, HEIGHT = 1900, 1050
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pomodoro Timer")
CLOCK = pygame.time.Clock()
BACKDROP = pygame.image.load("D:\VS Studio\Python on VS Studio\Projects\PomodoroTimer/backdrop.png")
WHITEBUTTON = pygame.image.load("D:\VS Studio\Python on VS Studio\Projects\PomodoroTimer/button.png")
FONT = pygame.font.Font("D:\VS Studio\Python on VS Studio\Projects\SpaceInvaders/Gametext.ttf", 120)
timerText = FONT.render("25:00", True, "white")
timerText_rect = timer_text.get_rect(center = (WIDTH / 2, HEIGHT / 2-25))
STARTSTOPBUTTON = Button(WHITEBUTTON, (WIDTH / 2, HEIGHT / 2 + 100), 170, 60, "START", pygame.font.Font("D:\VS Studio\Python on VS Studio\Projects\SpaceInvaders/Gametext.ttf", 25), "#000000", "#3F48CC")
POMODORO_BUTTON = Button(WHITEBUTTON, (WIDTH / 2 - 200, HEIGHT / 2 - 135), 120, 30, "Pomodoro", pygame.font.Font("D:\VS Studio\Python on VS Studio\Projects\SpaceInvaders/Gametext.ttf", 25), "#000000", "#3F48CC")
SHORTBREAKBUTTON = Button(WHITEBUTTON, (WIDTH / 2 - 65, HEIGHT / 2 - 135), 120, 30, "Short Break", pygame.font.Font("D:\VS Studio\Python on VS Studio\Projects\SpaceInvaders/Gametext.ttf", 25), "#000000", "#3F48CC")
LONGBREAK_BUTTON = Button(WHITEBUTTON, (WIDTH / 2 + 65, HEIGHT / 2 - 135), 120, 30, "Long Break", pygame.font.Font("D:\VS Studio\Python on VS Studio\Projects\SpaceInvaders/Gametext.ttf", 25), "#000000", "#3F48CC")
LONGPOMODORO_BUTTON = Button(WHITEBUTTON, (WIDTH / 2 + 210, HEIGHT / 2 - 135), 150, 30, "Long Pomodoro", pygame.font.Font("D:\VS Studio\Python on VS Studio\Projects\SpaceInvaders/Gametext.ttf", 25), "#000000", "#3F48CC")
POMODOROLENGTH = 1500 
SHORTBREAKLENGTH = 300 
LONGBREAKLENGTH = 600 
LONGPOMODOROLENGTH = 3000

currentSecs = POMODORO_LENGTH
pygame.time.set_timer(pygame.USEREVENT, 1000)
started = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if STARTSTOPBUTTON.checkInput(pygame.mouse.get_pos()):
                if started:
                    started = False
                else:
                    started = True
            if POMODOROBUTTON.checkInput(pygame.mouse.get_pos()):
                currentSecs= POMODOROLENGTH
                started = False
            if SHORTBREAKBUTTON.checkInput(pygame.mouse.get_pos()):
                currentSecs = SHORTBREAKLENGTH
                started = False
            if LONGBREAKBUTTON.checkInput(pygame.mouse.get_pos()):
                currentSecs = LONGBREAKLENGTH
                started = False
            if LONGPOMODOROBUTTON.checkInput(pygame.mouse.get_pos()):
                currentSecs = LONGPOMODOROLENGTH
                started = False
            if started:
                STARTSTOPBUTTON.text_input = "STOP"
                STARTSTOPBUTTON.text = pygame.font.Font("D:\VS Studio\Python on VS Studio\Projects\SpaceInvaders/Gametext.ttf", 20).render(
                                        STARTSTOPBUTTON.textInput, True, STARTSTOPBUTTON.baseColour)
            else:
                STARTSTOPBUTTON.textInput = "START"
                STARTSTOPBUTTON.text = pygame.font.Font("D:\VS Studio\Python on VS Studio\Projects\SpaceInvaders/Gametext.ttf", 20).render(
                                        STARTSTOPBUTTON.textInput, True, STARTSTOPBUTTON.baseColour)
        if event.type == pygame.USEREVENT and started:
            currentSecs = currentSecs - 1

    SCREEN.fill("#3F48CC")
    SCREEN.blit(BACKDROP, BACKDROP.get_rect(centre= (WIDTH/2, HEIGHT/2)))

    STARTSTOPBUTTON.updateScreen(SCREEN)
    STARTSTOPBUTTON.colourChange(pygame.mouse.get_pos())
    POMODOROBUTTON.updateScreen(SCREEN)
    POMODOROBUTTON.colourChange(pygame.mouse.get_pos())
    SHORTBREAKBUTTON.updateScreen(SCREEN)
    SHORTBREAKBUTTON.colourChange(pygame.mouse.get_pos())
    LONGBREAKBUTTON.updateScreen(SCREEN)
    LONGBREAKBUTTON.colourChange(pygame.mouse.get_pos())
    LONGPOMODOROBUTTON.updateScreen(SCREEN)
    LONGPOMODOROBUTTON.colourChange(pygame.mouse.get_pos())

    if currentSecs >= 0:
        displaySecs = currentSecs % 60
        displayMins = int(currentSecs / 60) % 60
    timerText = FONT.render(f"{displayMins:02}:{displaySecs:02}", True, "white")
    SCREEN.blit(timerText, timerText_rect)

    pygame.display.updateScreen()
