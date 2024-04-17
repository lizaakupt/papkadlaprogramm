import pygame

pygame.init()
win = pygame.display.set_mode((450, 450))


class Board:
    def __init__(self, surface):
        self.surface = surface
    def draw_circle(self, radius,x, y):
        pygame.draw.circle(self.surface, 'purple', (x, y), radius)
    def draw_line_kres(self,start_pos, end_pos, width):
        pygame.draw.line(self.surface, 'black', start_pos, end_pos, width)

    def draw_line(self):
        pygame.draw.line(win, (0, 0, 0), (150, 0), (150, 450), 3)
        pygame.draw.line(win, (0, 0, 0),  (300, 0), (300, 450), 3)
        pygame.draw.line(win, (0, 0, 0),    (0, 300), (450, 300), 3)
        pygame.draw.line(win, (0, 0, 0),  (0, 150), (450, 150), 3)
c = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        mouse = pygame.mouse.get_pos()
        win.fill((255, 255, 255))
        keys = pygame.mouse.get_pressed()


        board = Board(win)
        board.draw_line()



        if keys[0]:
            if 0 < x < 150 and 0 < y < 150:
                board.draw_circle(70, 75, 75)
                board.draw_line_kres((0, 0), (150, 150), 3)
                board.draw_line_kres((150, 0), (0, 150), 3)
            if 150 < x < 300 and 0 < y < 150:
                board.draw_circle(70, 225, 75)
                board.draw_line_kres((150, 0), (300, 150), 3)
                board.draw_line_kres((300, 0), (150, 150), 3)
            if 300 < x < 450 and 0 < y < 150:
                board.draw_circle(70, 375, 75)
                board.draw_line_kres((300, 0), (450, 150), 3)
                board.draw_line_kres((450, 0), (300, 150), 3)
            if 0 < x < 150 and 150 < y < 300:
                board.draw_circle(70, 75, 225)
                board.draw_line_kres((0, 150), (150, 300), 3)
                board.draw_line_kres((150, 150), (0, 300), 3)
            if 150 < x < 300 and 150 < y < 300:
                board.draw_circle(70, 225, 225)
                board.draw_line_kres((150, 150), (300, 300), 3)
                board.draw_line_kres((300, 150), (150, 300), 3)
            if 300 < x < 450 and 150 < y < 300:
                board.draw_circle(70, 375, 225)
                board.draw_line_kres((300, 150), (450, 300), 3)
                board.draw_line_kres((450, 150), (300, 300), 3)
            if 0 < x < 150 and 300 < y < 450:
                board.draw_circle(70, 75, 375)
                board.draw_line_kres((0, 300), (150, 450), 3)
                board.draw_line_kres((150, 300), (0,450), 3)
            if 150 < x < 300 and 300 < y < 450:
                board.draw_circle(70, 225, 375)
                board.draw_line_kres((150, 300), (300, 450), 3)
                board.draw_line_kres((300, 300), (150, 450), 3)
            if 300 < x < 450 and 300 < y < 450:
                board.draw_circle(70, 375, 375)
                board.draw_line_kres((300, 300), (450, 450), 3)
                board.draw_line_kres((450, 300), (300, 450), 3)
           

        pygame.time.delay(20)
        pygame.display.update()