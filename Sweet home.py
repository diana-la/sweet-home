import pygame, random
from random import randrange
from PIL import Image

pygame.init()

pygame.mixer.music.load('I Never Came Home Again.ogg')  # загрузка музыки
pygame.mixer.music.play(-1)  # воспроизведение
s = pygame.mixer.Sound('ticking_clock.wav')
catt = pygame.mixer.Sound('Meow.ogg')
window_width = 1000
window_hight = 500
size_window = [window_width, window_hight]
window = pygame.display.set_mode(size_window)  # размер окна

pygame.display.set_caption('Sweet home')  # заголовок окна

WITHE = (225, 225, 225)

background = pygame.image.load('Sprite_home.png')


# змейка
def snake():
    # шрифты
    go_font_scole = pygame.font.SysFont('Arial', 26)
    go_font = pygame.font.SysFont('Arial', 50)

    clock_tick = 3
    size = 50
    score = 0
    # цвета
    red = (255, 0, 0)
    green = (0, 225, 0)
    black = (0, 0, 0)

    down = True
    left = True
    right = True
    up = True
    runn = True

    # начальные коордитаны змейки
    x, y = randrange(0, window_hight, size), randrange(0, window_hight, size)
    # начальне координаты яблока
    apple = randrange(0, window_hight, size), randrange(0, window_hight, size)

    lenght = 1
    snake = [(x, y)]
    dx, dy = 0, 0

    while runn:  # самый простой цикл для выхода
        window.fill(pygame.Color(black))
        [(pygame.draw.rect(window, pygame.Color(green), (i, j, size, size))) for i, j in snake]
        pygame.draw.rect(window, pygame.Color(red), (*apple, size, size))

        # счётчик
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
            if clock_tick != 10:
                clock_tick += 1
            else:
                clock_tick = 9

        if x < 0 or x > window_width - size or y < 0 or \
                y > window_hight - size or len(snake) != len(set(snake)):
            go_end = go_font.render('Game over', 1, red)
            window.blit(go_end, (window_width // 3, window_hight // 3))
            pygame.display.flip()

        pygame.display.flip()
        clock.tick(clock_tick)  # указывает кол-во фреймов
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # если пользователь нажимает quit- приложение закрывается
                runn = False

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_RIGHT or event.key == ord('d') and right):
                    # если идёт вправо, то влево нет
                    dx, dy = 1, 0
                    down = True
                    left = False
                    right = True
                    up = True

                elif (event.key == pygame.K_LEFT or event.key == ord('a') and left):
                    # если идёт влево, то вправо нет
                    dx, dy = -1, 0
                    down = True
                    left = True
                    right = False
                    up = True

                elif (event.key == pygame.K_UP or event.key == ord('w') and up):
                    # если идёт вверх, то вниз нет
                    dx, dy = 0, -1
                    down = False
                    left = True
                    right = True
                    up = True

                elif (event.key == pygame.K_DOWN or event.key == ord('s') and down):
                    # если идёт вниз, то вверх нет
                    dx, dy = 0, 1
                    down = True
                    left = True
                    right = True
                    up = False

                    # escape - тоже выход
                elif event.key == pygame.K_ESCAPE:
                    runn = False


# слова из слов
def slova():
    # цвета
    COLOR_INACTIVE = pygame.Color('palegoldenrod')
    COLOR_ACTIVE = pygame.Color('burlywood')
    COLOR_NOTRIGHT = pygame.Color('coral')
    COLOR_RIGHT = pygame.Color('yellowgreen')
    # шрифты
    FONT = pygame.font.Font(None, 32)
    FONT_NOTRIGHT = pygame.font.Font(None, 27)
    FONT_RIGHT = pygame.font.Font(None, 50)

    bg = pygame.image.load('slova.jpg')
    used = []

    wordlist = ['почитатель', 'экспонат', 'эпиграмма', 'академия']

    first = ['пол', 'пот', 'тип', 'лечо', 'чело', 'почта', 'читать', 'читатель',
             'печать', 'пилот', 'лепта', 'плечо', 'атлет', 'плато', 'платье', 'печаль',
             'печь', 'лето', 'отчёт', 'теплота']

    second = ['акт', 'кот', 'сок', 'нос', 'сон', 'ток', 'тон', 'пот',
              'пано', 'коса', 'поэт', 'танк', 'нота', 'этнос', 'стопа', 'топка',
              'стопка', 'станок', 'эстонка']

    third = ['мир', 'маг', 'миг', 'мим', 'пир', 'грип', 'грим', 'пари',
             'рама', 'мама', 'ампир', 'гамма', 'грамм', 'магма', 'прима', 'рампа']

    fourth = ['ад', 'яд', 'еда', 'имя', 'мак', 'мид', 'яма', 'дама',
              'идея', 'маяк', 'ямка', 'дамка', 'камея', 'медиа', 'медик',
              'медяк']

    word = random.choice(wordlist)

    class InputBox:

        def __init__(self, x, y, w, h, text=''):
            self.rect = pygame.Rect(x, y, w, h)
            self.color = COLOR_INACTIVE
            self.text = text
            self.txt_surface = FONT.render(text, True, self.color)
            self.active = False

        def event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):  # проверяет нажал ли пользователь на поле
                    self.active = not self.active
                else:
                    self.active = False
                if self.active:  # изменение цвета если поле активно
                    self.color = COLOR_ACTIVE
                else:  # если неактивно
                    self.color = COLOR_INACTIVE
            if event.type == pygame.KEYDOWN:  # нажатие кнопок
                if self.active:
                    if event.key == pygame.K_RETURN:  # escape

                        if word == 'почитатель':
                            if (self.text in first) and (self.text not in used):
                                self.color = COLOR_RIGHT
                                used.append(self.text)
                            else:
                                self.color = COLOR_NOTRIGHT

                        elif word == 'экспонат':
                            if (self.text in second) and (self.text not in used):
                                self.color = COLOR_RIGHT
                                used.append(self.text)
                            else:
                                self.color = COLOR_NOTRIGHT

                        elif word == 'эпиграмма':
                            if (self.text in third) and (self.text not in used):
                                self.color = COLOR_RIGHT
                                used.append(self.text)
                            else:
                                self.color = COLOR_NOTRIGHT
                        else:
                            if (self.text in fourth) and (self.text not in used):
                                self.color = COLOR_RIGHT
                                used.append(self.text)
                            else:
                                self.color = COLOR_NOTRIGHT
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
                    self.txt_surface = FONT.render(self.text, True, self.color)

        def update(self):
            width = max(200, self.txt_surface.get_width() + 10)
            self.rect.w = width

        def draw(self, window):
            label = FONT.render('Составте 8 слов из слова: ', 1, COLOR_ACTIVE)
            slovo_label = FONT.render(word, 1, COLOR_INACTIVE)
            label_enter = FONT_NOTRIGHT.render('*После того как вписали'
                                               ' слово нажмите ENTER', 1, COLOR_NOTRIGHT)
            label_notright = FONT_NOTRIGHT.render('*Если  слово красное, то мы его'
                                                  ' не загадывали :)', 1, COLOR_NOTRIGHT)

            if len(used) == 8:
                label_end = FONT_RIGHT.render('Молодец, ты угадал все слова!!!', 1, COLOR_NOTRIGHT)
                window.blit(label_end, (50, 356))

            window.blit(label, (50, 30))
            window.blit(slovo_label, (335, 30))
            window.blit(label_enter, (450, 450))
            window.blit(label_notright, (450, 470))
            window.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

            pygame.draw.rect(window, self.color, self.rect, 2)

    input_box1 = InputBox(100, 100, 140, 32)
    input_box2 = InputBox(100, 164, 140, 32)
    input_box3 = InputBox(100, 228, 140, 32)
    input_box4 = InputBox(100, 292, 140, 32)
    input_box5 = InputBox(500, 100, 140, 32)
    input_box6 = InputBox(500, 164, 140, 32)
    input_box7 = InputBox(500, 228, 140, 32)
    input_box8 = InputBox(500, 292, 140, 32)
    input_boxes = [input_box1, input_box2, input_box3, input_box4, input_box5, input_box6, input_box7, input_box8]
    done = False

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                box.event(event)

        for box in input_boxes:
            box.update()

        window.blit(bg, (0, 0))
        for box in input_boxes:
            box.draw(window)

        pygame.display.flip()


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

signs_t_right = sprinte_signs.get_image(510, 10, 128, 110)
signs_t_left = sprinte_signs.get_image(666, 10, 123, 105)

signs_b_right = sprinte_signs.get_image(510, 140, 135, 105)
signs_b_left = sprinte_signs.get_image(662, 136, 128, 115)

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

# x0,y0 начальное расположение персонача
# hight, width - ширина и высота персонажа
hight = 250
width = 66
x0 = 50
y0 = window_hight - (hight + 20)
speed = 5  # скорость передвижения персонажа
flMusic = 0  # счётчик для музыки
light_count = 0  # счётчик для света
animCount = 0  # счётчик для фреймов
volume = 1.0  # громкость звука

left = False
right = False
flPause = False
light = False
tick = False


def drawWindow():
    global animCount, speed
    speed = 5
    pygame.display.update()
    window.blit(background, (0, 0))  # делаем фон
    window.blit(sprites, (0, 0))
    if light_count != 2:
        window.blit(cat, (814, 23))

    if animCount + 1 >= 30:  # если превышает 30 фреймов, то обновляем
        animCount = 0

    if left:  # если персонаж идёт влево
        window.blit(pygame.transform.scale(wleft[animCount // 6], (150, 250)), (x0, y0))
        # так как картинок влево всего 6,а фреймов 30
        animCount += 1

    elif right:  # если персонаж идёт вправо
        window.blit(pygame.transform.scale(wright[animCount // 6], (150, 250)), (x0, y0))
        animCount += 1

    else:  # если стоит
        window.blit(pygame.transform.scale(stand[animCount // 2], (150, 250)), (x0, y0))

    if light is True:
        night = pygame.image.load('night.png')
        window.blit(night, (0, 0))
        speed = 10
    pygame.display.update()


run = True
while run:  # самый простой цикл для выхода
    clock.tick(30)  # указывает кол-во фреймов

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # если пользователь нажимает quit- приложение закрывается
            run = False  # так как выходим из цикла
        if event.type == pygame.KEYDOWN:
            if event.key == ord('p') and 780 > x0 > 480:
                flMusic += 1

                if flMusic == 4:
                    flMusic = 0

                if flMusic == 1:
                    pygame.mixer.music.load('old city theme.ogg')
                    pygame.mixer.music.play(-1)

                elif flMusic == 2:
                    pygame.mixer.music.load('musiccc.ogg')
                    pygame.mixer.music.play(-1)

                elif flMusic == 3:
                    pygame.mixer.music.load('Snowfall.ogg')
                    pygame.mixer.music.play(-1)

                else:
                    pygame.mixer.music.load('I Never Came Home Again.ogg')
                    pygame.mixer.music.play(-1)

            elif event.key == pygame.K_CAPSLOCK:
                # при нажатии CAPSLOCK музыка включается/выключается
                flPause = not flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            elif event.key == ord('o') and 80 > x0 > 0:
                light = not light
                light_count += 1

            elif event.key == ord('t') and 400 > x0 > 300:
                tick = not tick
                if tick:
                    s.play()
                else:
                    s.stop()

            elif event.key == ord('c') and 975 > x0 > 793:
                catt.set_volume(0.7)
                catt.play()

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

        elif 975 > x0 > 793:
            window.blit(pygame.transform.scale(signs_c_left, [50, 50]), (770, 23))
            window.blit(pygame.transform.scale(signs_b_left, [50, 50]), (760, 180))
            pygame.display.update()

        elif 400 > x0 > 300:
            window.blit(pygame.transform.scale(signs_t_left, [50, 50]), (290, 120))
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

        elif 975 > x0 > 793:
            window.blit(pygame.transform.scale(signs_c_left, [50, 50]), (770, 23))
            window.blit(pygame.transform.scale(signs_b_left, [50, 50]), (760, 180))
            pygame.display.update()

        elif 400 > x0 > 300:
            window.blit(pygame.transform.scale(signs_t_right, [50, 50]), (440, 120))
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

    elif keys[pygame.K_b] and 975 > x0 > 793:
        slova()

    else:
        left = 0
        right = 0
        animCount = 0

    drawWindow()

pygame.quit()  # тоже выход
