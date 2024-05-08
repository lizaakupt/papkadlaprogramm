import random
import pygame

pygame.init()
win = pygame.display.set_mode((450, 450))
win.fill((128, 128, 128))
font = pygame.font.Font(None, 100)
text_pink = font.render("YOU WIN", True, (255, 20, 147))
text_blue = font.render("YOU WIN", True, (0, 255, 255))



class Board:
    def __init__(self, surface):
        self.surface = surface
        self.x1 = 150
        self.y1 = 400
        self.x2 = 250
        self.x3 = 150
        self.y3 = 50
        self.x4 = 250

    def draw_line(self, width):
        pygame.draw.line(win, (255, 20, 147), (self.x1, self.y1), (self.x2, self.y1), 3)
        pygame.draw.line(win, (0, 255, 255), (self.x3, self.y3), (self.x4, self.y3), 3)

    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x1 -= 3
            self.x2 -= 3

        elif keys[pygame.K_RIGHT]:
            self.x1 += 3
            self.x2 += 3

        if keys[pygame.K_a]:
            self.x3 -= 3
            self.x4 -= 3

        elif keys[pygame.K_d]:
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
        pygame.draw.circle(self.surface, 'white', (self.x, self.y), radius)

    def update(self):
        self.x += self.speed * self.dx
        self.y += self.speed * self.dy



    def update_board(self, board):
        if self.x > board.x1 and self.x < board.x2 and self.y == board.y1:
            self.dx *= -1
            self.dy *= -1
        elif self.x > board.x3 and self.x < board.x4 and self.y == board.y3:
            self.dx *= -1
            self.dy *= -1
    def side(self):
        if self.y <= 0:
            win.blit(text_pink, (80, 170))
        elif self.y >= 450:
            win.blit(text_blue, (80, 170))



figure = Board(win)
ball = Ball(1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((128, 128, 128))
    ball.draw_circle(7)
    figure.move_by_keys()
    figure.draw_line(10)
    figure.draw_line(10)
    ball.update()
    ball.update_board(figure)
    ball.side()

    pygame.time.delay(5)
    pygame.display.update()