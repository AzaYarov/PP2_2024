def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Enter Your Name')

    username = get_username(screen)
    print('Your username is:', username)

if __name__ == '__main__':
    main()
# Подключение к базе данных