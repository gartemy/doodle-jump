import pygame
from random import randint

pygame.init()

WIDTH = 400
HEIGHT = 500

FPS = 60
clock = pygame.time.Clock()

player_left = pygame.image.load('assets/doodle.png')
player_right = pygame.transform.flip(player_left, True, False)
background = pygame.image.load('assets/background.png')
platform_img = pygame.image.load('assets/platform.png')

player = player_left

player_rect = player.get_rect()
player_rect.x = 170
player_rect.y = 400

jump = False
y_change = 0
x_change = 0
player_speed = 3

platforms = [
    pygame.Rect([175, 480, 70, 10]),
]
platforms_num = 5

for i in range(platforms_num):
    platform = platform_img.get_rect()
    while True:
        platform.x = randint(0, 320)
        platform.y = randint(150, 370)
        index = platform.collidelist(platforms)
        if index == -1:
            break
    platforms.append(platform)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Doodle Jump')


def update_player(y_pos):
    global jump
    global y_change
    jump_height = 15
    gravity = 1
    if jump:
        y_change = -jump_height
        jump = False
    y_pos += y_change
    y_change += gravity
    return y_pos


def check_collision(rect_list, j):
    global player_rect
    global y_change
    for i in range(len(rect_list)):
        if rect_list[i].colliderect(player_rect) and j is False and y_change > 0:
            j = True
    return j


def update_platforms(p_list, y_pos, change):
    if y_pos < 250 and change < 0:
        for i in range(len(p_list)):
            p_list[i].y -= change
        else:
            pass
    for item in range(len(p_list)):
        if p_list[item].y > 500:
            p_list[item].x = randint(10, 320)
            p_list[item].y = randint(-10, 0)
    return p_list


while True:
    window.blit(background, (0, 0))

    for i in range(len(platforms)):
        window.blit(platform_img, platforms[i])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -player_speed
            elif event.key == pygame.K_RIGHT:
                x_change = player_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = 0

    jump = check_collision(platforms, jump)
    player_rect.x += x_change
    player_rect.y = update_player(player_rect.y)

    # if player_rect.y < 440:
    #     player_y = update_player(player_rect.y)
    # else:
    #     exit()

    if player_rect.x < -20:
        player_x = -20
    elif player_rect.x > 330:
        player_x = 330
    platforms = update_platforms(platforms, player_rect.y, y_change)

    if x_change > 0:
        player = player_right
    elif x_change < 0:
        player = player_left

    window.blit(player, player_rect)

    pygame.display.flip()
    clock.tick(FPS)
