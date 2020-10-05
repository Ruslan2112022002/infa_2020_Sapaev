#Б02-010 Сапаев Руслан задача 2 лабораторная 4

import pygame
from pygame.draw import *

def flower(screen, surface, x, y, angle, zoom):
    flower_rot = pygame.transform.rotozoom(surface, angle, zoom)
    flower_rot.set_colorkey((0, 0, 0))
    screen.blit(flower_rot,(x, y))
    
def Bush (screen, x, y, zoom, bush_color, flower_color, border_color):
    flower_surf = pygame.Surface((70*zoom, 35*zoom))
    flower_surf.fill((0, 0, 0))
    ellipse(flower_surf,  flower_color, (17 * zoom,  0 * zoom, 25 * zoom, 13 * zoom))
    ellipse(flower_surf,  border_color, (17 * zoom,  0 * zoom, 25 * zoom, 13 * zoom), 1)
    ellipse(flower_surf,  flower_color, ( 5 * zoom,  4 * zoom, 25 * zoom, 13 * zoom))
    ellipse(flower_surf,  border_color, ( 5 * zoom,  4 * zoom, 25 * zoom, 13 * zoom), 1)
    ellipse(flower_surf,  flower_color, (32 * zoom,  3 * zoom, 25 * zoom, 13 * zoom))
    ellipse(flower_surf,  border_color, (32 * zoom,  3 * zoom, 25 * zoom, 13 * zoom), 1)
    ellipse(flower_surf, (255, 255, 0), (21 * zoom, 11 * zoom, 25 * zoom, 13 * zoom))
    ellipse(flower_surf,  flower_color, ( 0 * zoom, 13 * zoom, 25 * zoom, 13 * zoom))
    ellipse(flower_surf,  border_color, ( 0 * zoom, 13 * zoom, 25 * zoom, 13 * zoom), 1)
    ellipse(flower_surf,  flower_color, (39 * zoom,  9 * zoom, 25 * zoom, 13 * zoom))
    ellipse(flower_surf,  border_color, (39 * zoom,  9 * zoom, 25 * zoom, 13 * zoom), 1)
    ellipse(flower_surf,  flower_color, (13 * zoom, 17 * zoom, 25 * zoom, 13 * zoom))
    ellipse(flower_surf,  border_color, (13 * zoom, 17 * zoom, 25 * zoom, 13 * zoom), 1)
    ellipse(flower_surf,  flower_color, (32 * zoom, 18 * zoom, 25 * zoom, 13 * zoom))
    ellipse(flower_surf,  border_color, (32 * zoom, 18 * zoom, 25 * zoom, 13 * zoom), 1)
    circle(screen, bush_color,(x, y), 100 * zoom)
    flower(screen, flower_surf, x - 80, y - 30,  15, 0.8)
    flower(screen, flower_surf, x - 10, y - 70,   0, 0.8)
    flower(screen, flower_surf, x - 10, y - 20, -15, 0.8)
    flower(screen, flower_surf, x - 60, y + 20,   8, 0.8)
    flower(screen, flower_surf, x - 80, y - 60,  15, 0.6)
    flower(screen, flower_surf, x + 50, y - 10, -70, 0.8)
    
 
def Body(screen, x, y, zoom, color_body):
    ellipse(screen, color_body,(x - 68 * zoom, y -  32 * zoom, 140 * zoom,  64 * zoom))
    ellipse(screen, color_body,(x + 38 * zoom, y - 120 * zoom,  40 * zoom, 105 * zoom))
    ellipse(screen, color_body,(x + 43 * zoom, y - 140 * zoom,  50 * zoom,  32 * zoom))

def Eyes(screen: pygame.display, x, y, zoom, color_body, color_eye_1, color_eye_2):
    ellipse(screen, color_eye_2, (x + 52 * zoom, y - 138 * zoom, 24 * zoom, 20 * zoom))  
    ellipse(screen, color_eye_1, (x + 65 * zoom, y - 133 * zoom, 10 * zoom,  8 * zoom))
    glasik = pygame.Surface((12 * zoom, 6 * zoom), pygame.SRCALPHA)
    ellipse(glasik, color_body, (0, 0, 11 * zoom, 11 * zoom))
    glasik_rot = pygame.transform.rotate(glasik, -30)
    screen.blit(glasik_rot, (x + 58 * zoom, y - 138 * zoom))
    
def Horns(screen, x, y, zoom, color_body):
        polygon(screen, color_body, [(x            , y            ), (x - 10 * zoom, y - 10 * zoom),
                                     (x - 15 * zoom, y - 20 * zoom), (x - 18 * zoom, y - 30 * zoom), 
                                     (x - 10 * zoom, y - 20 * zoom), (x            , y - 10 * zoom), 
                                     (x +  5 * zoom, y - 11 * zoom)])
        polygon(screen, color_body, [(x + 14 * zoom, y -  4 * zoom), (x +  4 * zoom, y - 14 * zoom), 
                                     (x -  1 * zoom, y - 24 * zoom), (x -  4 * zoom, y - 34 * zoom), 
                                     (x +  4 * zoom, y - 24 * zoom), (x + 14 * zoom, y - 14 * zoom), 
                                     (x + 19 * zoom, y -  4 * zoom)])
                
def Legs(screen, x, y, zoom, color_body):
    ellipse(screen, color_body, (x - 10 * zoom, y + 20 * zoom, 20 * zoom, 48 * zoom))
    ellipse(screen, color_body, (x - 10 * zoom, y - 25 * zoom, 20 * zoom, 50 * zoom))
    ellipse(screen, color_body, (x -  5 * zoom, y + 65 * zoom, 20 * zoom, 15 * zoom))


def Kozel(screen, x, y, zoom, color_body, color_eye_1, color_eye_2):
    Body(screen, x, y, zoom, color_body)
    Eyes(screen, x, y, zoom, color_body, color_eye_1, color_eye_2)
    Horns(screen,x + 50 * zoom, y - 130 * zoom, zoom / 1.5, color_body)
    Legs(screen, x + 45 * zoom, y + 38 * zoom, zoom, color_body)
    Legs(screen, x - 25 * zoom, y + 38 * zoom, zoom, color_body)
    Legs(screen, x - 51 * zoom, y + 13 * zoom, zoom, color_body)
    Legs(screen, x + 23 * zoom, y + 13 * zoom, zoom, color_body)

pygame.init()

pixels_x = 600  
pixels_y = 900
FPS = 30
Screen = pygame.display.set_mode((pixels_x, pixels_y))

Screen.fill((170, 220, 135))
rect(Screen, (175, 220, 230), (0, 0, pixels_x, 400))
polygon(Screen, ((180, 180, 180)), [( -1, 280), ( 70,  90), (125, 220), (205, 120),
                       (360, 360), (470, 110), (500, 160), (600,  30), 
                       (600, 530), (345, 530), (340, 525), (340, 480), 
                       (335, 470), (330, 460), (326, 455), (320, 450), 
                       (320, 450), (130, 450), ( 75, 460), ( 55, 460), 
                       ( 30, 460), ( -1, 480)])
polygon(Screen, ((0, 0, 0)), [( -1, 280), ( 70,  90), (125, 220), (205, 120),
                       (360, 360), (470, 110), (500, 160), (600,  30), 
                       (600, 530), (345, 530), (340, 525), (340, 480), 
                       (335, 470), (330, 460), (326, 455), (320, 450), 
                       (320, 450), (130, 450), ( 75, 460), ( 55, 460), 
                       ( 30, 460), ( -1, 480)], 1)
Kozel(Screen, 200, 500, 0.8, (255, 255, 255), (0, 0, 0), (230, 130, 255))
Bush(Screen, 460, 650, 1, (110, 200, 60), (255, 255, 255), (180, 180, 180))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

