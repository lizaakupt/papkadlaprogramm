import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))


class Circle:
    def __init__(self, surface, color, x, y, radius, dir):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.surface = surface
        self.dir = dir

    def move(self):
        if self.x > 500:
            self.dir = -1
        elif self.x < 0:
            self.dir = 1
        self.x = self.x + 3*self.dir


    def draw(self):
        pygame.draw.circle(self.surface, self.color, (self.x, self.y), self.radius)



c = []
for i in range(100):
    c.append(Circle(win, (255, i*2.5, (255-i*2.5)), 4*i, 4*i, 20, 1))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((145, 45, 255))
    for i in c:
        i.draw()
        i.move()
    pygame.time.delay(10)
    pygame.display.update()