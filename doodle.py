import pygame

pygame.init()

# Ширина игрового окна
WIDTH = 400

# Высота игрового окна
HEIGHT = 500

# Создаем игровое окно
window = pygame.display.set_mode([WIDTH, HEIGHT])

# Указываем заголовок окна
pygame.display.set_caption('Doodle Jump')

# Частота кадров
FPS = 60

# Подключаем Clock (задержку между переключением кадров)
clock = pygame.time.Clock()

# Задний фон игры
background = pygame.image.load('assets/background.png').convert()

# Картинка с платформой
platform_img = pygame.image.load('assets/platform.png')

# Картинка с пришельцем
player = pygame.image.load('assets/doodle.png')

# Прямоугольник с координатами игрока
player_rect = player.get_rect()

# Начальные координаты пришельца
player_rect.x = 200
player_rect.y = 420

# Платформы, по которым можно прыгать
platforms = [
    pygame.Rect(200, 480, 85, 24),
]

# Прыгает ли пришелец? (True - Да, False - Нет)
jump = True

# Изменение координаты y пришельца
y_change = 0

def update_player(y_position):
    # Указываем, какие переменные берем извне (глобальные переменные)
    global jump
    global y_change

    # Высота прыжка пришельца
    jump_height = 15

    # Гравитация (величина изменения высоты пришельца)
    gravity = 1

    # Проверяем, что пришельцу нужно прыгнуть
    if jump == True:
        # Перемещаем пришельца вверх (совершаем прыжок)
        y_change = -jump_height

        # Говорим, что пришельцу нужно опуститься
        jump = False

    # Изменяем полученную координату Y пришельца
    y_position += y_change
    
    # Постепенно изменяем координату Y пришельца
    y_change += gravity

    # Возвращаем вычисленную координату Y пришельца
    return y_position

# Функция для проверки столкновения пришельца с платформами
def check_collide(rect_list, j):
    global player_rect
    # Перебираем все платформы на экране
    for i in range(len(platforms)):
        if player_rect.colliderect(rect_list[i]):
            j = True
    return j

# Игровой цикл
while True:
    # Рисуем задний фон на экране
    window.blit(background, [0, 0])

    # Перебираем события игрока
    for event in pygame.event.get():
        # Если игрок нажал крестик
        if event.type == pygame.QUIT:
            # Закрываем игру
            exit()

    # Проверяем, что пришелец прыгает или падает
    jump = check_collide(platforms, jump)

    # Обновляем координату Y пришельца (в игре)
    player_rect.y = update_player(player_rect.y)

    # Рисуем платформу на игровом окне
    window.blit(platform_img, platforms[0])

    # Рисуем пришельца на игровом экране
    window.blit(player, player_rect)
    
    # Обновление игрового окна
    pygame.display.flip()

    # Задержка переключения между кадрами (60 кадров в секунду)
    clock.tick(FPS)