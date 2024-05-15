import random
import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
win.fill((176, 196, 222))
font = pygame.font.Font(None, 150)
text_pink = font.render("YOU WIN", True, (255, 20, 147))
text_green = font.render("YOU WIN", True, (0, 100, 100))

class Board:
    def __init__(self, surface):
        self.surface = surface
        self.x1 = 150
        self.y1 = 500
        self.x2 = 350
        self.x3 = 150
        self.y3 = 100
        self.x4 = 350

    def draw_line(self, width):
        pygame.draw.line(win, (255, 20, 147), (self.x1, self.y1), (self.x2, self.y1), 5)
        pygame.draw.line(win, (0, 100, 100), (self.x3, self.y3), (self.x4, self.y3), 5)

    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x1 > 0 and self.x2 > 100:
            self.x1 -= 3
            self.x2 -= 3
        elif keys[pygame.K_RIGHT] and self.x1 < 500 and self.x2 < 600:
            self.x1 += 3
            self.x2 += 3

        if keys[pygame.K_a] and self.x3 > 0 and self.x4 > 100:
            self.x3 -= 3
            self.x4 -= 3
        elif keys[pygame.K_d] and self.x3 < 500 and self.x4 < 600:
            self.x3 += 3
            self.x4 += 3

class Ball:
    def __init__(self, speed):
        self.surface = win
        self.x = 290
        self.y = 225
        self.speed = speed
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])

    def draw_circle(self, radius):
        pygame.draw.circle(self.surface, (255, 0, 0), (self.x, self.y), radius)

    def update(self):
        self.x += self.speed * self.dx
        self.y += self.speed * self.dy
        # Добавление отражения от боковых стенок
        if self.x <= 0 or self.x >= 600:
            self.dx *= -1

    def update_board(self, board):
        if self.x > board.x1 and self.x < board.x2 and self.y == board.y1:
            # self.dx *= -1
            self.dy *= -1
        elif self.x > board.x3 and self.x < board.x4 and self.y == board.y3:
            # self.dx *= -1
            self.dy *= -1

    def side(self):
        if self.y <= 0:
            win.blit(text_pink, (80, 250))
        elif self.y >= 600:
            win.blit(text_green, (80, 250))

figure = Board(win)
ball = Ball(1)
pygame.time.delay(1000)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    win.fill((176, 196, 222))
    ball.draw_circle(15)
    figure.move_by_keys()
    figure.draw_line(10)
    figure.draw_line(10)
    ball.update()
    ball.update_board(figure)
    ball.side()

    pygame.time.delay(5)
    pygame.display.update()