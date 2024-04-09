import pygame 
from random import randint
from random import randrange
from nall import Ball

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 5000)
W, H = 500, 650
car_sound = pygame.mixer.Sound("zvuk-shosse.mp3")
sc = pygame.display.set_mode((500,650))
bg = pygame.image.load('images/road.jpg').convert()

coin_image = 'images/coin.png'
player2 = 'images/2.png'
clock = pygame.time.Clock()
FPS = 60
player_images = ['2.png']
coin_images = ['coin.png']
coin_surf = [pygame.image.load('images/'+path).convert_alpha() for path in coin_images]
car_surf = [pygame.image.load('images/'+path).convert_alpha() for path in player_images]

def createCoin(group):
    indx = randint(0, len(coin_surf) - 1)
    x = randint(20, W - 20)
    speed = randint(3,5)
    return Ball(x, speed, coin_surf[indx], group)
speed1 = 1
def createCar(group):
    indx = randint(0, len(car_surf) - 1)
    x = randint(20, W - 20)
    speed = speed1
    return Ball(x, speed, car_surf[indx], group)

balls = pygame.sprite.Group()
cars = pygame.sprite.Group()

 # Скорость врага
player_speed = 5  # Скорость игрока
player = pygame.image.load('images/player.png').convert_alpha()
player_rect = player.get_rect(centerx=W//2, bottom = H - 5)

player_sprite = pygame.sprite.Sprite() 
player_sprite.image = player
player_sprite.rect = player.get_rect(centerx=W//2, bottom=H - 5)

font = pygame.font.Font(None, 36)
score = 0
bg_y = 0
car_sound.play()
createCoin(balls)
createCar(cars)

# Задаем переменную для отслеживания количества заработанных монет
coins_earned = 0
# Задаем значение N для увеличения скорости врага после заработки N монет
N = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createCoin(balls)
            createCar(cars)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_sprite.rect.x -= player_speed
        if player_sprite.rect.x < 0:
            player_sprite.rect.x = 0
    elif keys[pygame.K_RIGHT]:
        player_sprite.rect.x += player_speed
        if player_sprite.rect.x > W - player_sprite.rect.width:
            player_sprite.rect.x = W - player_sprite.rect.width
    elif keys[pygame.K_UP]:
        player_sprite.rect.y -= player_speed
        if player_sprite.rect.y < 0:
            player_sprite.rect.y = 0
    elif keys[pygame.K_DOWN]:
        player_sprite.rect.y += player_speed
        if player_sprite.rect.y > H - player_sprite.rect.height:
            player_sprite.rect.y = H - player_sprite.rect.height
            
    sc.blit(bg, (0,bg_y))
    sc.blit(bg, (0,bg_y + 650))
    
    bg_y -= 2
    if bg_y == -650:
        bg_y = 0
    
    balls.draw(sc)
    cars.draw(sc)
    collisions = pygame.sprite.spritecollide(player_sprite, balls, True)
    car_collisions = pygame.sprite.spritecollide(player_sprite, cars, True)
    score += len(collisions)
    if collisions:
        score += randrange(0,2)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    sc.blit(score_text, (10, 10))
    sc.blit(player, player_sprite.rect)
    
    if len(car_collisions) >= 1:
        font_end = pygame.font.Font(None, 48)
        end_text = font_end.render(f'Game over', True, (0, 0, 0))
        end1_text = font_end.render(f'Your score: {score}', True, (0, 0, 0))
        end2_text = font_end.render(f'Your speed: {speed1}', True, (0, 0, 0))
        sc.blit(end_text, (170,300))
        sc.blit(end1_text, (170,330))
        sc.blit(end2_text, (170,360))
        pygame.display.update()  # Update the display to show the "Game Over" text
        pygame.time.delay(2000)  # Delay for 2 seconds before quitting
        pygame.quit()
        exit()
        
    # Проверяем, заработал ли игрок N монет
    if score >= N:
        speed1 += 1  # Увеличиваем скорость врага
        N += 5  # Увеличиваем значение N для следующего уровня увеличения скорости врага
        
    pygame.display.update()
    clock.tick(FPS)
    cars.update(H)
    balls.update(H)
