import pygame 
from random import randint
from nall import Ball

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)
W, H = 500, 650

sc = pygame.display.set_mode((500,650))
bg = pygame.image.load('images/road.jpg').convert()

coin_image = 'images/coin.png'

clock = pygame.time.Clock()
FPS = 60

coin_images = ['coin.png','coin.png','coin.png']
coin_surf = [pygame.image.load('images/'+path).convert_alpha() for path in coin_images]

def createCoin(group):
    indx = randint(0, len(coin_surf) - 1)
    x = randint(20, W - 20)
    speed = randint(3,7)

    return Ball(x, speed, coin_surf[indx], group)

balls = pygame.sprite.Group()
speed = 2
car_speed = 3

player = pygame.image.load('images/player.png').convert_alpha()
player_rect = player.get_rect(centerx=W//2, bottom = H - 5)

player_sprite = pygame.sprite.Sprite() 
player_sprite.image = player
player_sprite.rect = player.get_rect(centerx=W//2, bottom=H - 5)
font = pygame.font.Font(None, 36)
score = 0
bg_y = 0

createCoin(balls)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createCoin(balls)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_sprite.rect.x -= car_speed
        if player_sprite.rect.x < 0:
            player_sprite.rect.x = 0
    elif keys[pygame.K_RIGHT]:
        player_sprite.rect.x += car_speed
        if player_sprite.rect.x > W - player_sprite.rect.width:
            player_sprite.rect.x = W - player_sprite.rect.width
    elif keys[pygame.K_UP]:
        player_sprite.rect.y -= car_speed
        if player_sprite.rect.y < 0:
            player_sprite.rect.y = 0
    elif keys[pygame.K_DOWN]:
        player_sprite.rect.y += car_speed
        if player_sprite.rect.y > H - player_sprite.rect.height:
            player_sprite.rect.y = H - player_sprite.rect.height
            
    sc.blit(bg, (0,bg_y))
    sc.blit(bg, (0,bg_y + 650))
    bg_y -= 2
    if bg_y == -650:
        bg_y = 0
    balls.draw(sc)

    collisions = pygame.sprite.spritecollide(player_sprite, balls, True)
    score += len(collisions)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    sc.blit(score_text, (10, 10))
    sc.blit(player, player_sprite.rect)

    pygame.display.update()

    clock.tick(FPS)

    balls.update(H)