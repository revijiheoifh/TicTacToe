import pygame
import os
import XO
import time

width = 450
height = 450
turn = 0

win = pygame.display.set_mode((width, height))
background_img = pygame.image.load(os.path.join("assets", "background.jpg"))
background = pygame.transform.scale(background_img, (width,height))
cross_img = pygame.image.load(os.path.join("assets", "X.jpg"))
cross = pygame.transform.scale(cross_img, (140,140))
zero_img = pygame.image.load(os.path.join("assets", "O.jpg"))
zero = pygame.transform.scale(zero_img, (140,140))
win_screenXimg = pygame.image.load(os.path.join("assets", "cross_win.jpg"))
win_screenX = pygame.transform.scale(win_screenXimg, (450,450))
win_screenOimg = pygame.image.load(os.path.join("assets", "circle_win.jpg"))
win_screenO = pygame.transform.scale(win_screenOimg, (450,450))
draw_screen_img = pygame.image.load(os.path.join("assets", "Draw.jpg"))
draw_screen = pygame.transform.scale(draw_screen_img, (450,450))

def back():
    win.blit(background, (0,0))

def x(xp, yp):
    # First row
    if xp in range(0,150) and yp in range(0, 145) and XO.row1[0] == "":
        win.blit(cross, (7,0))
        XO.row1[0] = "x"

    elif xp in range(151,300) and yp in range(0, 145) and XO.row1[1] == "":
        win.blit(cross, (157,0))
        XO.row1[1] = "x"

    elif xp in range(301,500) and yp in range(0, 145) and XO.row1[2] == "":
        win.blit(cross, (309,0))
        XO.row1[2] = "x"

    # Second row
    if xp in range(0,150) and yp in range(146, 295) and XO.row2[0] == "":
        win.blit(cross, (7,152))
        XO.row2[0] = "x"
      
    elif xp in range(151,300) and yp in range(146, 295) and XO.row2[1] == "":
        win.blit(cross, (157,152))
        XO.row2[1] = "x"

    elif xp in range(301,500) and yp in range(146, 295) and XO.row2[2] == "":
        win.blit(cross, (309,152))
        XO.row2[2] = "x"


    # Third row
    if xp in range(0,150) and yp in range(295, 495) and XO.row3[0] == "":
        win.blit(cross, (7,310))
        XO.row3[0] = "x"

    elif xp in range(151,300) and yp in range(295, 495) and XO.row3[1] == "":
        win.blit(cross, (157,310))
        XO.row3[1] = "x"

    elif xp in range(301,495) and yp in range(295, 495) and XO.row3[2] == "":
        win.blit(cross, (309,310))
        XO.row3[2] = "x"


def o(xp, yp):
    # First row
    if xp in range(0,150) and yp in range(0, 145) and XO.row1[0] == "":
        win.blit(zero, (7,0))
        XO.row1[0] = "o"

    elif xp in range(151,300) and yp in range(0, 145) and XO.row1[1] == "":
        win.blit(zero, (157,0))
        XO.row1[1] = "o"

    elif xp in range(301,500) and yp in range(0, 145) and XO.row1[2] == "":
        win.blit(zero, (309,0))
        XO.row1[2] = "o"
        
    # Second row
    if xp in range(0,150) and yp in range(146, 295) and XO.row2[0] == "":
        win.blit(zero, (7,152))
        XO.row2[0] = "o"

    elif xp in range(151,300) and yp in range(146, 295) and XO.row2[1] == "":
        win.blit(zero, (157,152))
        XO.row2[1] = "o"

    elif xp in range(301,500) and yp in range(146, 295) and XO.row2[2] == "":
        win.blit(zero, (309,152))
        XO.row2[2] = "o"

    # Third row
    if xp in range(0,150) and yp in range(295, 495) and XO.row3[0] == "":
        win.blit(zero, (7,310))
        XO.row3[0] = "o"

    elif xp in range(151,300) and yp in range(295, 495) and XO.row3[1] == "":
        win.blit(zero, (157,310))
        XO.row3[1] = "o"

    elif xp in range(301,495) and yp in range(295, 495) and XO.row3[2] == "":
        win.blit(zero, (309,310))
        XO.row3[2] = "o"

def winning_screen():
    winner = XO.check_winner()
    if winner == 'o':
        win.blit(win_screenO, (0,0))
    elif winner == 'x':
        win.blit(win_screenX, (0,0))

def drawing():
    draw = XO.check_draw()
    if draw:
        win.blit(draw_screen, (0,0))

def main():
    run = True
    global turn
    back()
    while run:        
        xp, yp = pygame.mouse.get_pos()        
        for events in pygame.event.get(): 
            if events.type == pygame.MOUSEBUTTONDOWN:
                if turn % 2 == 0:
                    x(xp, yp)
                    print(XO.row1, XO.row2, XO.row3)
                    turn += 1
                elif turn % 2 != 0:
                    o(xp, yp)
                    print(XO.row1, XO.row2, XO.row3)
                    turn += 1
            winning_screen()
            drawing()
            if events.type == pygame.QUIT:
                run = False
        
        pygame.display.update()
    pygame.quit()
main()