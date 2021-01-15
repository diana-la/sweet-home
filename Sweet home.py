import pygame
from random import randrange
from PIL import Image
import sys

pygame.init()

pygame.mixer.music.load('I Never Came Home Again.ogg')  # загрузка музыки
pygame.mixer.music.play(-1)  # воспроизведение

window_width = 1000
window_hight = 500
size_window = [window_width, window_hight]
window = pygame.display.set_mode(size_window)  # размер окна

pygame.display.set_caption('Sweet home')  # заголовок окна

WITHE = (225, 225, 225)

background = pygame.image.load('Sprite_home.png')

# snake

def snake():
    go_font_scole = pygame.font.SysFont('Arial', 26)
    go_font = pygame.font.SysFont('Arial', 50)
    size = 50
    red = (255, 0, 0)
    green = (0, 225, 0)
    black = (0, 0, 0)
    clock_tick = 5
    down = True
    left = True
    right = True
    up = True
    score = 0
    x, y = randrange(0, window_hight, size), randrange(0, window_hight, size)
    apple = randrange(0, window_hight, size), randrange(0, window_hight, size)
    lenght = 1
    snake = [(x, y)]
    dx, dy = 0, 0
    runn = True
    while runn:  # самый простой цикл для выхода
        window.fill(pygame.Color(black))
        [(pygame.draw.rect(window, pygame.Color(green), (i, j, size, size))) for i, j in snake]
        pygame.draw.rect(window, pygame.Color(red), (*apple, size, size))
        go_score = go_font_scole.render(f'Score: {score}', 1, pygame.Color('orange'))
        window.blit(go_score, (5, 5))
        x += dx * size
        y += dy * size
        snake.append((x, y))
        snake = snake[-lenght:]  # изначально одна голова
        if snake[-1] == apple:
            apple = randrange(0, window_hight, size), randrange(0, window_hight, size)
            lenght += 1
            score += 1
            clock_tick += 1
        if x < 0 or x > window_width - size or y < 0 or y > window_hight - size or len(snake) != len(set(snake)):
            go_end = go_font.render('Game over', 1, red)
            window.blit(go_end, (window_width // 3, window_hight // 3))
            pygame.display.flip()

        pygame.display.flip()
        clock.tick(clock_tick)  # указывает кол-во фреймов
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # если пользователь нажимает quit- приложение закрывается
                runn = False

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_RIGHT or event.key == ord('d') and right):  # если идёт вправо, то влево нет
                    dx, dy = 1, 0
                    down = True
                    left = False
                    right = True
                    up = True

                elif (event.key == pygame.K_LEFT or event.key == ord('a') and left):  # если идёт влево, то вправо нет
                    dx, dy = -1, 0
                    down = True
                    left = True
                    right = False
                    up = True

                elif (event.key == pygame.K_UP or event.key == ord('w') and up):  # если идёт вверх, то вниз нет
                    dx, dy = 0, -1
                    down = False
                    left = True
                    right = True
                    up = True

                elif (event.key == pygame.K_DOWN or event.key == ord('s') and down):  # если идёт вниз, то вверх нет
                    dx, dy = 0, 1
                    down = True
                    left = True
                    right = True
                    up = False
                    # нажали escape

                elif event.key == pygame.K_ESCAPE:
                    runn = False


# загрузка изображений в списки


class SpriteSplit:

    def __init__(self, file_name):
        self.sprite_split = pygame.image.load(file_name).convert()

    def get_image(self, x0, y0, width, height):  # для того чтобы разделить изображение на спрайты
        black = (0, 0, 0)
        image = pygame.Surface([width, height]).convert()  # изменяет формат пикселей
        image.blit(self.sprite_split, (0, 0), (x0, y0, width, height))  # dcnfdkztn bpj,hfl
        image.set_colorkey(black)  # для того чтобы виден был только персонаж без фона вокруг него
        return image


sprites = pygame.image.load('sprites.png')

cat = pygame.image.load('cat.png')

sprinte_signs = SpriteSplit('signs.png')
signs_p_left = sprinte_signs.get_image(190, 146, 130, 100)
signs_p_right = sprinte_signs.get_image(40, 140, 118, 93)

signs_c_right = sprinte_signs.get_image(29, 10, 112, 100)
signs_c_left = sprinte_signs.get_image(193, 10, 109, 100)

signs_o_right = sprinte_signs.get_image(375, 140, 103, 109)
signs_o_left = sprinte_signs.get_image(370, 30, 100, 100)

sprite_split = SpriteSplit("player.png")
wleft = [sprite_split.get_image(0, 189, 53, 94), sprite_split.get_image(50, 189, 59, 94),
         sprite_split.get_image(107, 189, 55, 94), sprite_split.get_image(161, 189, 50, 94),
         sprite_split.get_image(211, 189, 55, 94),
         sprite_split.get_image(266, 189, 85, 94),
         sprite_split.get_image(320, 189, 50, 94)]  # спрайты, когда идёт вправо

im = Image.open("player.png")
im = im.transpose(Image.FLIP_LEFT_RIGHT)  # отзеркаливаю изображение
im.save("player_2.png")
sprite_split1 = SpriteSplit("player_2.png")

wright = [sprite_split1.get_image(0, 189, 50, 94), sprite_split1.get_image(50, 189, 54, 94),
          sprite_split1.get_image(106, 189, 53, 94), sprite_split1.get_image(160, 189, 50, 94),
          sprite_split1.get_image(211, 189, 55, 94),
          sprite_split1.get_image(266, 189, 55, 94),
          sprite_split1.get_image(320, 189, 50, 94)]  # спрайты,когда идёт влево
stand = [sprite_split.get_image(0, 0, 58, 95), sprite_split.get_image(54, 0, 52, 95)]  # спрайт, когда стоит

clock = pygame.time.Clock()

# x0,y0 начальное расположение объекта

hight = 250
width = 66
x0 = 50
y0 = window_hight - (hight + 20)
speed = 5
left = False
right = False
flPause = False
flMusic = False
light_count = 0
light = False
animCount = 0
volume = 1.0


def drawWindow():
    global animCount, speed
    speed=5
    pygame.display.update()
    window.blit(background, (0, 0))  # делаем фон
    window.blit(sprites, (0, 0))
    if light_count!=2:
        window.blit(cat,(814,23))

    if animCount + 1 >= 30:  # если превышает 30 фреймов, то обновляем
        animCount = 0

    if left:  # если персонаж идёт влево
        window.blit(pygame.transform.scale(wleft[animCount // 6],(150,250)), (x0, y0))
        # так как картинок влево всего 6,а фреймов 30
        animCount += 1

    elif right:  # если персонаж идёт вправо
        window.blit(pygame.transform.scale(wright[animCount // 6],(150,250)), (x0, y0))
        animCount += 1

    else:  # если стоит
        window.blit(pygame.transform.scale(stand[animCount//2],(150,250)), (x0, y0))

    if light is True:
        night = pygame.image.load('night.png')
        window.blit(night, (0, 0))
        speed=10
    pygame.display.update()


run = True
while run:  # самый простой цикл для выхода
    clock.tick(30)  # указывает кол-во фреймов

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # если пользователь нажимает quit- приложение закрывается
            run = False  # так как выходим из цикла
        if event.type == pygame.KEYDOWN:
            if event.key == ord('p') and 780 > x0 > 480:
                if flMusic is False:
                    pygame.mixer.music.load('old city theme.ogg')
                    pygame.mixer.music.play(-1)
                    flMusic = True
                elif flMusic is True:
                    pygame.mixer.music.load('I Never Came Home Again.ogg')
                    pygame.mixer.music.play(-1)
                    flMusic = False
            elif event.key == pygame.K_CAPSLOCK:
                flPause = not flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == ord('o') and 80 > x0 > 0:
                light = not light
                light_count += 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x0 -= speed  # при задержки левой кнопки объект перемещается на 5 пикс влево
        left = True
        right = False
        if 780 > x0 > 480:
            window.blit(pygame.transform.scale(signs_p_left, [50, 50]), (475, 180))
            pygame.display.update()
        elif 330 > x0 > 45:
            window.blit(pygame.transform.scale(signs_c_left, [50, 50]), (40, 180))
            pygame.display.update()
        elif 100 > x0 > 0:
            window.blit(pygame.transform.scale(signs_o_right, [50, 50]), (30, 200))
            pygame.display.update()
        if x0 < 0:
            x0 = window_width - width
            pygame.display.update()
    elif keys[pygame.K_RIGHT]:
        x0 += speed
        left = False
        right = True
        if 780 > x0 > 480:
            window.blit(pygame.transform.scale(signs_p_right, [50, 50]), (700, 180))
            pygame.display.update()
        elif 330 > x0 > 45:
            window.blit(pygame.transform.scale(signs_c_right, [50, 50]), (330, 180))
            pygame.display.update()
        elif 80 > x0 > 0:
            window.blit(pygame.transform.scale(signs_o_right, [50, 50]), (30, 200))
            pygame.display.update()

        if x0 > window_width:
            x0 = 0
            pygame.display.update()

    elif keys[pygame.K_EQUALS]:
        volume += 0.1
        pygame.mixer.music.set_volume(volume)

    elif keys[pygame.K_MINUS]:
        volume -= 0.1
        pygame.mixer.music.set_volume(volume)

    elif keys[pygame.K_c] and 330 > x0 > 45:
        snake()

    else:
        left = 0
        right = 0
        animCount = 0

    drawWindow()

pygame.quit()  # тоже выход
