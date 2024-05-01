import pygame

pygame.init()
win = pygame.display.set_mode((450, 450))
win.fill((0, 0, 0))


class Board:
    def __init__(self, surface):
        self.surface = surface
        self.x = 225
        self.y = 225
        self.start_pos = (175, 225)
        self.end_pos = (275, 225)

    def draw_circle(self, radius):
        self.x += 1
        self.y += 1
        pygame.draw.circle(self.surface, 'white', (self.x, self.y), radius)

    def draw_line(self, width):
        pygame.draw.line(win,'white', self.start_pos, self.end_pos, 3)
    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.start_pos -= 3
            self.end_pos -= 3
        elif keys[pygame.K_RIGHT]:
            self.end_pos += 3
            self.start_pos += 3



figure = Board(win)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill(('black'))
    figure.draw_circle(7)
    figure.move_by_keys()
    figure.draw_line(10)



    pygame.time.delay(10)
    pygame.display.update()