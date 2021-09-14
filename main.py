# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import pygame
import math
from arrow import up_is_down, down_is_down, left_is_down, right_is_down


# from random import randint


def txt(message, position_txt_x, position_txt_y, color=(255, 255, 255), size_txt=30, font="david"):
    font = pygame.font.SysFont(font, size_txt)
    text = font.render(message, True, color)

    center = []
    for i in text.get_rect():
        center.append(i)
    screen.blit(text, [position_txt_x - center[2] / 2, position_txt_y - center[3] / 2])


def dist(pont1_x, pont1_y, pont2_x, pont2_y):
    return math.sqrt(math.pow(pont1_x - pont2_x, 2) + math.pow(pont1_y - pont2_y, 2))


def collision(rect, circle):
    if rect.x <= circle.x <= rect.x + rect.width:
        if circle.y + circle.rad >= rect.y and circle.y - circle.rad <= rect.y + rect.height:
            return True

    if circle.y + circle.rad >= rect.y and circle.y - circle.rad <= rect.y + rect.height:
        if circle.x + circle.rad >= rect.x and circle.x - circle.rad <= rect.x + rect.width:
            if circle.x + circle.rad - rect.x <= 10:
                return True

    if dist(circle.x, circle.y, rect.x, rect.y) <= circle.rad or \
            dist(circle.x + rect.width, circle.y, rect.x, rect.y) <= circle.rad or \
            dist(circle.x, circle.y + rect.height, rect.x, rect.y) <= circle.rad or \
            dist(circle.x + rect.width, circle.y + rect.height, rect.x, rect.y) <= circle.rad:
        return True
    return False


def ball_collision(ball1, ball2):
    dx = ball1.x - ball2.x
    dy = ball1.y - ball2.y

    distance = math.sqrt(dx * dx + dy * dy)
    if distance < ball1.rad + ball2.rad:
        return True
    else:
        return False


list_enemies = [[], [], [], [], []]
list_walls = []


def create_ball(x, y, group):
    enemies = Obstacles(x, y, 5)
    list_enemies[group].append(enemies)  # noinspection PyTypeChecker


def starter_values():
    global list_walls
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
    wall_15 = Walls(500, 0, 200, height / 2 - 20, 0)
    wall_16 = Walls(500, height / 2 + 20, 200, height / 2 - 20, 0)
    list_walls = [wall_1, wall_2, wall_3, wall_4, wall_5, wall_6, wall_7, wall_8, wall_9, wall_10, wall_11,
                  wall_12, wall_13, wall_14, wall_15, wall_16]


now = datetime.datetime.now()


def restart_now():
    global now
    now = datetime.datetime.now()


class Esmaecer:
    def __init__(self):
        self.cont = 0
        self.one_time = True
        self.esm_color_txt = (0, 0, 0)

    def esm_color(self, color, time):
        dif = datetime.datetime.now() - now
        if dif.microseconds % 2 == 0 and dif.microseconds != 0:
            if 0 <= self.cont <= 5:
                self.esm_color_txt = [int(color[0] / 5 * self.cont), int(color[1] / 5 * self.cont),
                                      int(color[2] / 5 * self.cont)]
            if dif.seconds <= time:
                self.cont += 1
            else:
                self.cont -= 1
        return self.esm_color_txt


class Obstacles:
    def __init__(self, x, y, rad):
        self.x = x
        self.y = y
        self.ini_x = x
        self.ini_y = y
        self.rad = rad
        self.color = 255, 255, 255
        self.accelerator = 0
        self.speed = 10
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
    white = (255, 255, 255)
    # bola = pygame.image.load('data\\images\\bola.png')
    bg1 = pygame.image.load('data\\images\\bg1.png')
    bg2 = pygame.image.load('data\\images\\bg2.png')
    bg3 = pygame.image.load('data\\images\\bg3.png')
    bg4 = pygame.image.load('data\\images\\bg4.png')
    bg5 = pygame.image.load('data\\images\\bg5.png')
    bg6 = pygame.image.load('data\\images\\bg6.png')
    bg7 = pygame.image.load('data\\images\\bg7.png')
    psg = Persona(width / 2, height / 2, 10)

    list_txt = ["Olá", "É bom te ver.", "Fico feliz que esteja aqui", "E que consiga caminhar",
                "as setas são nossas direções", "Talvez...", "eu possa te ensinar algumas coisas",
                "Okay. primeiro;", "tome cuidado com as paredes", "Agora vê aquilo?", "não se deixe acertar por elas",
                "maravilhoso!", "Está pronto para seguir", "Vá em frente", "Há algo esperando por você",
                "Escolhas...", "Teremos tantas durante a vida.", "Algumas simples, como essa", "Para cima há flores",
                "para baixo espinhos", "mantenha-se seguro", "suba", "muito bem!", "Não quero pensar",
                "no que teria no outro lado", "Cuidado!", "Isso foi perigoso!", "Não quero que se machuque", "Okay...",
                "As escolhas podem ficar difíceis", "Mas sempre...", "Sempre!", "Escolha o que for melhor para você",
                "Tudo bem?... bem, vamos prosseguir"]

    esmaecer_white = Esmaecer()
    starter_values()  # faz a primeira definição das paredes
    clock = pygame.time.Clock()
    t1 = 1.0
    t2 = 1.0
    for i in range(5):
        create_ball(900, i * 50, 0)

    for i in range(20):
        create_ball(0, 0, 1)
        create_ball(0, 0, 2)
        create_ball(0, 0, 3)
        create_ball(0, 0, 4)
    next_txt = 0
    velocity = 5
    move_x = 0
    move_y = 0
    close = False
    while not close:
        # _______________________________________________ Desenhos na tela
        screen.fill(black)  # Limpa tela
        screen.blit(bg1, (0 + move_x, 0 + move_y))  # Background 1 até 7
        screen.blit(bg2, (750 + move_x, 0 + move_y))
        screen.blit(bg3, (1500 + move_x, 0 + move_y))
        screen.blit(bg4, (1500 + move_x, -480 + move_y))
        screen.blit(bg5, (2250 + move_x, -480 + move_y))
        screen.blit(bg6, (1500 + move_x, 480 + move_y))
        screen.blit(bg7, (2250 + move_x, 480 + move_y))
        txt(list_txt[next_txt], width / 2, height / 2 + 100, esmaecer_white.esm_color(white, 2), 45, "imprintshadow")
        for i in range(len(list_enemies)):
            for n in list_enemies[i]:
                n.draw_obstacle()  # Desenho de todos os inimigos
        for i in list_walls:
            i.draw_wall()  # Desenho de todas as paredes

        pygame.draw.circle(screen, (255, 255, 255), (psg.x, psg.y), psg.rad)  # Desenho do personagem

        # ________________________________________________________________________ enemies 2
        # Movimentação de inimigos inferiores
        t2 += 0.00002
        for i in range(len(list_enemies[4])):
            list_enemies[4][i].x = 220 * math.cos((t2 * (i + 1)) * 360) * math.cos((t2 * (i + 1))) + 2550 + move_x
            list_enemies[4][i].y = 220 * math.cos((t2 * (i + 1)) * 360) * math.sin((t2 * (i + 1))) + 720 + move_y

        # Colisão de inimigos inferiores
        for i in list_enemies[4]:
            if ball_collision(psg, i):
                psg.x = width / 2
                psg.y = height / 2
                move_x = 0
                move_y = 0
                starter_values()

        # ________________________________________________________________________ enemies 2
        # Movimentação dos inimigos 2 (flores)
        t1 += 0.001
        for i in range(len(list_enemies[1])):
            list_enemies[1][i].x = 250 * math.cos((t1 * (i + 1)) * 3) * math.cos((t1 * (i + 1))) + 2550 + move_x
            list_enemies[1][i].y = 250 * math.cos((t1 * (i + 1)) * 3) * math.sin((t1 * (i + 1))) - 250 + move_y
        for i in range(len(list_enemies[2])):
            list_enemies[2][i].x = 100 * math.cos((t1 * (i + 1)) * 3) * math.cos((t1 * (i + 1))) + 2700 + move_x
            list_enemies[2][i].y = 100 * math.cos((t1 * (i + 1)) * 3) * math.sin((t1 * (i + 1))) - 110 + move_y
        for i in range(len(list_enemies[3])):
            list_enemies[3][i].x = 100 * math.cos((t1 * (i + 1)) * 3) * math.cos((t1 * (i + 1))) + 2700 + move_x
            list_enemies[3][i].y = 100 * math.cos((t1 * (i + 1)) * 3) * math.sin((t1 * (i + 1))) - 390 + move_y
        # Verificação de colisão com inimigos 2

        for n in range(3):
            for i in list_enemies[n + 1]:
                if ball_collision(psg, i):
                    psg.x = width / 2
                    psg.y = height / 2
                    move_x = 0
                    move_y = 0
                    starter_values()

        # _________________________________________________________________________ enemies 1

        # movimentação dos primeiros inimigos
        for i in range(len(list_enemies[0])):
            list_enemies[0][i].accelerator += list_enemies[0][i].speed
            list_enemies[0][i].x = list_enemies[0][i].ini_x + move_x
            list_enemies[0][i].y = list_enemies[0][i].ini_y + move_y + list_enemies[0][i].accelerator
            if list_enemies[0][i].y >= height + move_y or list_enemies[0][i].y <= 0 + move_y:
                list_enemies[0][i].speed = -list_enemies[0][i].speed
        # colisão dos primeiros inimigos
        for i in list_enemies[0]:
            if ball_collision(psg, i):
                psg.x = width / 2
                psg.y = height / 2
                move_x = 0
                move_y = 0
                starter_values()
        # ________________________________________________________________________
        # Fazendo a colisão do personagem com a parede
        for i in list_walls:
            if collision(i, psg):
                psg.x = width / 2
                psg.y = height / 2
                move_x = 0
                move_y = 0
                starter_values()
        # _______________________________________________________ move control
        if left_is_down():
            next_txt += 1
            esmaecer_white.cont = 0
            restart_now()
            for i in list_walls:
                i.x += velocity
            move_x += velocity

        if right_is_down():
            for i in list_walls:
                i.x -= velocity
            move_x -= velocity

        if up_is_down():
            for i in list_walls:
                i.y += velocity
            move_y += velocity

        if down_is_down():
            for i in list_walls:
                i.y -= velocity
            move_y -= velocity

        # ___________________________________________________________
        clock.tick(30)
        pygame.display.update()  # Update de tela
        # Evento de saída
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
                pygame.display.quit()



def continua():
    restart_now()
    black = (0, 0, 0)
    color_txt = (255, 255, 255)
    esmaecer_white = Esmaecer()
    clock = pygame.time.Clock()
    close = False
    while not close:
        screen.fill(black)  # Limpa tela
        txt("Continua...", width / 2, height / 2, esmaecer_white.esm_color(color_txt, 2), 45, "imprintshadow")
        if down_is_down():
            esmaecer_white.cont = 0
            restart_now()
        """
        for i in pygame.font.get_fonts():
            print(i)
        """
        clock.tick(30)
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
    # continua()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
