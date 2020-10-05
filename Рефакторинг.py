#Задиран Б02-922 3 задача
import math
import pygame
from pygame.draw import *
from pygame.math import *

# Инициализация цветов
yellow = (255, 255, 0)
red = (235, 47, 68)
black = (0, 0, 0)
cloud_colour = (254, 249, 249)
green = (15, 83, 14)
pink = (249, 194, 194)
orange = (181, 98, 17)
light_green = (14, 147, 37)
brown = (147, 107, 14)
blue = (158, 234, 245, 0.97)
blue_chill = (14, 147, 145)

def tree(x: int, y: int, scale: float = 1, leaf_colour: tuple = green, rounding_colour: tuple = black):
    '''
    Рисует дерево
    x, y - координата нижнего левого угла ствола
    scale - масштабный фактор
    leaf_colour - цвет кроны дерева
    rounding_colour - цвет контура
    '''
    x1 = int(x+16*scale)
    y1 = int(y-2*50*scale)
    r = 34 
    rect(screen, rounding_colour, (x, y, int(16 * scale), int(70 * scale)))
    circle(screen, leaf_colour, (int((x1 + x) / 2), y1), int(r * scale))
    circle(screen, rounding_colour, (int((x1 + x) / 2), y1), int(r * scale), 1)
    circle(screen, leaf_colour, (int((x1 + x) / 2+(r + 4)*scale), int(y1 + r * scale)), int(r * scale))
    circle(screen, leaf_colour, (int((x1 + x) / 2 - (r + 4) * scale), int(y1 + (r + 2) * scale)), int(r * scale))
    circle(screen, rounding_colour, (int((x1 + x) / 2 + (r + 4) * scale), int(y1 + r * scale)), int(r * scale), 1)
    circle(screen, rounding_colour, (int((x1 + x) / 2 - (r + 4) * scale), int(y1 + (r + 2) * scale)), int(r * scale), 1)
    circle(screen, leaf_colour, (int((x1 + x) / 2), int(y1 + (2*r-16) * scale)), int(r * scale))
    circle(screen, rounding_colour, (int((x1 + x) / 2), int(y1 + (2 * r - 16) * scale)), int(r * scale), 1)
    circle(screen, leaf_colour, (int((x1 + x) / 2-(r - 7) * scale), int(y1 + (2 * r + 10) * scale)), int(r * scale))
    circle(screen, rounding_colour, (int((x1 + x) / 2-(r - 7) * scale), int(y1 + (2 * r + 10) * scale)), int(r * scale), 1)
    circle(screen, leaf_colour, (int((x1 + x) / 2 + (r - 10) * scale), int(y1 + (2 * r + 15) * scale)), int(r * scale))
    circle(screen, rounding_colour, (int((x1 + x) / 2 + (r - 10) * scale), int(y1 + (2 * r + 15) * scale)), int(r * scale), 1)
    pass


def cloud(x: int, y: int, scale: float = 1, cloud_colour: tuple = cloud_colour, rounding_colour: tuple = black):
    '''
    Рисует облако
    x, y - координата центра левого нижнего кружка в облаке
    scale - масштабный фактор
    cloud_colour - цвет кроны облака
    rounding_colour - цвет контура
    '''    
    r = 30 * scale
    for i in range(4):
        circle(screen, cloud_colour, (int(x + r * i * 1.15), int(y)), int(r))
        circle(screen, rounding_colour, (int(x +r * i * 1.15), int(y)), int(r), 1)

    for i in range(2):
        circle(screen, cloud_colour, (int(x - r * i * 1.2 + r * 2.3), int(y - r * 0.9)), int(r))
        circle(screen, rounding_colour, (int(x - r * i * 1.2 + r * 2.3), int(y - r * 0.9)), int(r), 1)
    pass

 
def house(x: int, y: int, scale: float = 1, roof_colour: tuple = red, walls_colour:tuple = brown, window_colour:tuple = blue_chill,
          window_rounding_colour: tuple = orange, walls_rounding: tuple = black):
    '''
    Рисует дом
    x, y - координата левого нижнего края дома
    scale - масштабный фактор
    roof_colour - цвет крыши
    walls_colour - цвет стен
    window_colour - цвет окна
    window_rounding_colour - цвет контура окна
    walls_rounding - цвет контура дома
    '''
    width = int(160 * scale)
    height = int(0.75 * width)
    x1 = x + width
    y2 = int(y + height/3)
    x2 = int(x + width/3)

    polygon(screen, roof_colour, [(x, y), (int((x + x1) / 2), int(y - height * 0.7)), (x1, y), (x, y)])
    polygon(screen, walls_rounding, [(x, y), (int((x + x1) / 2), int(y - height * 0.7)), (x1, y), (x, y)], 1)
    rect(screen, walls_colour, (x, y, width, height))
    rect(screen, walls_rounding, (x, y, width, height), 1)
    rect(screen, window_colour, (x2, y2, int(width / 3), int(height / 3)))
    rect(screen, window_rounding_colour, (x2, y2, int(width / 3), int(height / 3)), 1)
    pass


def sun(x: int, y: int, scale: float = 1, sun_colour: tuple = pink, rounding_colour: tuple = black):
    '''
    Рисует солнце
    x, y - координата центра солнца
    scale - масштабный фактор
    sun_colour - цвет солнца
    rounding_colour - цвет контура
    '''    
    r = 37          # Внутренний радиус солнца
    R = 40          # Внешний радиус солнца
    v = []
    N = 20          # Количество лучей
    for i in range(N):
        y1 = int(y - r * math.sin(i * 2 * math.pi / (N - 1)))
        y2 = int(y - R * math.sin(i*2*math.pi/(N-1) + math.pi/(N - 1)))
        x1 = int(x + r * math.cos(i * 2 * math.pi / (N - 1)))
        x2 = int(x + R * math.cos(i * 2 * math.pi / (N - 1) + math.pi/(N-1)))
        v.append((x1, y1))
        v.append((x2, y2))

    polygon(screen, sun_colour, v)
    polygon(screen, rounding_colour, v, 1)
    pass

def drawing(surface: pygame.display):
    '''
    функция рисования всей картины
    surface - экран рисования
    '''
    # Отрисовка неба и земли
    rect(screen, blue, (0, 0, 720, 240))
    rect(screen, light_green, (0, 240, 720, 240))
    # Все остальное
    house(90, 260, scale = 1)
    house (250, 200, 0.3, black, orange, green, blue_chill)
    cloud(370, 130, scale = 0.6)
    cloud(150, 100, scale = 0.8)
    cloud(550, 105, scale = 0.85)
    tree(320, 300, scale = 1)
    house(420, 250, scale = 0.7)
    tree(580, 260, scale = 0.7)
    sun(60, 60, scale = 1)
    
pygame.init()
FPS = 30
screen = pygame.display.set_mode((720, 480))

drawing(screen)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()