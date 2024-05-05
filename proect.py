import pygame

pygame.init()
win = pygame.display.set_mode((450, 450))
win.fill((0, 0, 0))


class Board:
    def __init__(self, surface):
        self.surface = surface
        self.x = 225
        self.y = 225
        self.x1 = 175
        self.y1 = 225
        self.x2 = 275
        self.y2 = 225


    def draw_circle(self, radius):
        self.x += 1
        self.y += 1

        pygame.draw.circle(self.surface, 'white', (self.x, self.y), radius)

    def draw_line(self, width):
        pygame.draw.line(win,'white', (self.x1, self.y1), (self.x2, self.y2), 3)


    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x1 -= 3
            self.x2 -= 3

        elif keys[pygame.K_RIGHT]:
            self.x1 += 3
            self.x2 += 3

    def updated(self):
        if self.x > 450 or self.y > 450:
            self.x = -1
            self.y = -1
        elif self.x < 0 or self.y < 0:
            self.y = +1
            self.x = +1



figure = Board(win)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    win.fill(('black'))
    figure.draw_circle(7)
    figure.move_by_keys()
    figure.draw_line(10)
    figure.updated()

    pygame.time.delay(5)
    pygame.display.update()