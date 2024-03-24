import pygame
import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))


class Circle:
    def __init__(self, surface, color, x, y, radius):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.surface = surface

    dir = +-1
        x = self.x + 3 * dir
    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)

    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 3
        elif keys[pygame.K_RIGHT]:
            self.x += 3
        elif keys[pygame.K_UP]:
            self.y -= 3
        elif keys[pygame.K_DOWN]:
            self.y += 3


abc = Circle(win, (255, 255, 0), 250, 250, 20)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((145, 45, 255))
    abc.draw()
    abc.move_by_keys()
    pygame.time.delay(10)
    pygame.display.update()
