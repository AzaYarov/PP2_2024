import pygame 

pygame.init()

fps = 60
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
active_color = (0, 0, 255)  
active_size = 0  
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Paint")
painting = []
pen_image = pygame.image.load("pen.png")
eraser_image = pygame.image.load("eraser.png")
def draw_menu():
    pygame.draw.rect(screen, 'gray', [0,0,WIDTH,70])
    pygame.draw.line(screen, 'black', (0,70), (WIDTH, 70), 3)

    
    
    pen = pygame.draw.rect(screen, 'white', [10,10,50,50])
    screen.blit(pen_image, (20, 14))
    eraser = pygame.draw.rect(screen, 'black', [70,10,50,50])
    screen.blit(eraser_image, (80, 14))
    rectangle = pygame.draw.rect(screen, 'black', [130,10,50,50])
    circle = pygame.draw.rect(screen, 'black', [190,10,50,50])
    

    tools = [pen,eraser,rectangle,circle]

    blue = pygame.draw.rect(screen, (0,0,255), [WIDTH-35,10,25,25])
    red  = pygame.draw.rect(screen, (255,0,0), [WIDTH-35,35,25,25])
    green = pygame.draw.rect(screen, (0,255,0), [WIDTH-60,10,25,25])
    yellow = pygame.draw.rect(screen, (255,255,0), [WIDTH-60,35,25,25])
    teal = pygame.draw.rect(screen, (0,255,255), [WIDTH-85,10,25,25])
    purple  = pygame.draw.rect(screen, (255,0,255), [WIDTH-85,35,25,25])
    white = pygame.draw.rect(screen, (255,255,255), [WIDTH-110,35,25,25])
    black = pygame.draw.rect(screen, (0,0,0), [WIDTH-110,10,25,25])

    rgbs = [(0,0,255), (255,0,0), (0,255,0), (255,255,0), (0,255,255), (255,0,255), (255,255,255), (0,0,0)]
    

    color = [blue,red,green,yellow,teal,purple,white,black]

    return tools,color, rgbs

def draw_painting(paints):
    for i in paints:
        pygame.draw.circle(screen,i[0],i[1],i[2])


run = True
while run:
    timer.tick(fps)
    screen.fill('white')
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    if mouse[1] > 70:
        pygame.draw.circle(screen,active_color, mouse,active_size)
    if left_click and mouse[1] > 70:
        painting.append((active_color,mouse,active_size))
    draw_painting(painting)
    tools, colors, rgbs = draw_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        for i in range(len(tools)):
            if tools[i].collidepoint(event.pos):
                active_size = 20 - (i*5)

        for i in range(len(colors)):
            if colors[i].collidepoint(event.pos):
                active_color = rgbs[i]
    pygame.display.flip()

pygame.quit()

