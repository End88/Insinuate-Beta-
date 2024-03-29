# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame
import math
from random import randint


def left_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        return True
    return False


def right_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        return True
    return False


def up_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        return True
    return False


def down_is_down():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        return True
    return False


def dist(pont1_x, pont1_y, pont2_x, pont2_y):
    return math.sqrt(math.pow(pont1_x - pont2_x, 2) + math.pow(pont1_y - pont2_y, 2))


def collision(rect, circle):
    if rect.x <= circle.x <= rect.x + rect.width:
        if circle.y + circle.rad >= rect.y and circle.y - circle.rad <= rect.y + rect.height:
            if circle.y + circle.rad - rect.y <= 10:
                return 1
            else:
                return 2

    if circle.y + circle.rad >= rect.y and circle.y - circle.rad <= rect.y + rect.height:
        if circle.x + circle.rad >= rect.x and circle.x - circle.rad <= rect.x + rect.width:
            if circle.x + circle.rad - rect.x <= 10:
                return 3
            else:
                return 4

    if dist(circle.x, circle.y, rect.x, rect.y) <= circle.rad:
        return 5
    elif dist(circle.x + rect.width, circle.y, rect.x, rect.y) <= circle.rad:
        return 6
    elif dist(circle.x, circle.y + rect.height, rect.x, rect.y) <= circle.rad:
        return 7
    elif dist(circle.x + rect.width, circle.y + rect.height, rect.x, rect.y) <= circle.rad:
        return 8
    return 0


def ball_collision(ball1, ball2):
    dx = ball1.x - ball2.x
    dy = ball1.y - ball2.y

    distance = math.sqrt(dx * dx + dy * dy)
    if distance < ball1.rad + ball2.rad:
        return True
    else:
        return False


list_enemies = [[], []]


def create_ball(x, y, group):
    enemies = Obstacles(x, y, 5)
    list_enemies[group].append(enemies)


class Obstacles:
    def __init__(self, x, y, rad):
        self.x = x
        self.y = y
        self.rad = rad
        self.color = 255, 255, 255
        n = pygame.time.get_ticks()
        self.second_created = n

    def draw_obstacle(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.rad)


class Walls:
    def __init__(self, x, y, swidth, sheight, angle=0):
        self.x = x
        self.y = y
        self.width = swidth
        self.height = sheight
        self.angle = angle
        self.color = (102, 102, 102)

    def draw_wall(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


class Persona:
    def __init__(self, x, y, rad):
        self.x = x
        self.y = y
        self.rad = rad


def phase_one():
    black = (0, 0, 0)
    # bola = pygame.image.load('data\\images\\bola.png')
    bg1 = pygame.image.load('data\\images\\bg1.png')
    bg2 = pygame.image.load('data\\images\\bg2.png')
    bg3 = pygame.image.load('data\\images\\bg3.png')
    bg4 = pygame.image.load('data\\images\\bg4.png')
    bg5 = pygame.image.load('data\\images\\bg5.png')
    bg6 = pygame.image.load('data\\images\\bg6.png')
    bg7 = pygame.image.load('data\\images\\bg7.png')

    def starter_values():
        global psg, list_walls
        psg = Persona(width / 2, height / 2, 10)
        wall_1 = Walls(0, 0, 750, 25, 0)
        wall_2 = Walls(0, 480 - 25, 750, 25, 0)
        wall_3 = Walls(0, 0, 25, 480, 0)
        wall_4 = Walls(750, 0, 750, 25, 0)
        wall_5 = Walls(750, 480 - 25, 750, 25, 0)
        wall_6 = Walls(1500, -480, 25, 480 + 25, 0)
        wall_7 = Walls(1500, 480 - 25, 25, 480, 0)
        wall_8 = Walls(2250 - 25, 0, 25, 480, 0)
        wall_9 = Walls(1500, -480, 750, 25, 0)
        wall_10 = Walls(2250, -480, 750, 25, 0)
        wall_11 = Walls(1500, 960 - 25, 750, 25, 0)
        wall_12 = Walls(2250, 960 - 25, 750, 25, 0)
        wall_13 = Walls(2250 - 25, 480, 750 + 25, 25, 0)
        wall_14 = Walls(2250 - 25, 0 - 25, 750 + 25, 25, 0)
        list_walls = [wall_1, wall_2, wall_3, wall_4, wall_5, wall_6, wall_7, wall_8, wall_9, wall_10, wall_11,
                      wall_12, wall_13, wall_14]
    starter_values()
    clock = pygame.time.Clock()
    t = 1.0
    create_ball(600, 0, 0)
    create_ball(width/2, height/2, 1)
    bola_move_x = 0
    bola_move_y = 0
    velocity = 5
    move_x = 0
    move_y = 0
    close = False
    while not close:
        # _______________________________________________ Desenhos na tela

        for i in range(len(list_enemies)):
            for n in list_enemies[i]:
                n.draw_obstacle()
        """ Perfect circle
        t += 2/1
        for i in list_enemies[1]:
            i.x += 5 * math.cos(t * 45) * math.cos(t)
            i.y += 5 * math.cos(t * 45) * math.sin(t)
        
         Flor!!!
        t += 3/1
        for i in list_enemies[1]:
            i.x += 150 * math.cos(t * 360) * math.cos(t)
            i.y += 150 * math.cos(t * 360) * math.sin(t)
        
        t += 3
        for i in list_enemies[1]:
            i.x = 150 * math.cos(t * (2 * math.pi + 0.3)) * math.cos(t) + 500
            i.y = 150 * math.cos(t * (2 * math.pi + 0.3)) * math.sin(t) + 300
        
        t += 3
        for i in list_enemies[1]:
            i.x = 150 * math.cos(t * (2 * math.pi + 0.5)) * math.cos(t) + 500
            i.y = 150 * math.cos(t * (2 * math.pi + 0.5)) * math.sin(t) + 300
        """

        t += 3
        for i in list_enemies[1]:
            i.x = 150 * math.cos(t * (2 * math.pi)) * math.cos(t) + 500
            i.y = 150 * math.cos(t * (2 * math.pi)) * math.sin(t) + 300
        # ___________________________________________________________
        clock.tick(60)
        pygame.display.update()  # Update de tela
        # Evento de saída
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
                pygame.display.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    size = width, height = 750, 480
    screen = pygame.display.set_mode(size)
    phase_one()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
