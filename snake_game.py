import pygame
import time
import random
pygame.init()
pygame.font.init()
dis_width = 600
dis_height = 600
display = pygame.display.set_mode((dis_width, dis_height))
little = pygame.display.set_caption('snake game','snake')
x1 = dis_width / 2
x2 = dis_height/2

y1 = 0
y2 = 0
font_style = pygame.font.SysFont("Segoe UI", 50)
print(font_style)

snake_block = 10
snake_speed = 20
snake_length = 1


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    print(type(mesg))
    display.blit(mesg, [dis_width / 2, dis_height / 2])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display,'black',[x[0],x[1], snake_block, snake_block])

snake_list = []
game_over = False

clock = pygame.time.Clock()

foodx = random.randrange(0, dis_width - snake_block,10)
foody = random.randrange(0, dis_height - snake_block,10)

while not game_over:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y1 = 0
                y2 = -10
            elif event.key == pygame.K_d:
                y1 = 10
                y2 = 0
            elif event.key == pygame.K_a:
                y1 = -10
                y2 = 0
            elif event.key == pygame.K_s:
                y1 = 0
                y2 = 10
    if x1 >= dis_width or x1 <0 or x2 >=dis_height or x2 <0:
        game_over = True

    x1 += y1
    x2 += y2

    display.fill('blue')
    pygame.draw.rect(display, 'red', [foodx, foody, snake_block, snake_block])
    snake_head = []
    snake_head.append(x1)
    snake_head.append(x2)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    our_snake(snake_block, snake_list)

    pygame.display.update()
    if x1 == foodx and x2 == foody:
        foodx = random.randrange(0, dis_width - snake_block,10)
        foody = random.randrange(0, dis_height - snake_block,10)
        snake_length += 1


    pygame.draw.rect(display, 'black', [x1 , x2, snake_block, snake_block])

    our_snake(snake_block, snake_list)
    pygame.display.update()

    clock.tick(snake_block)
message('You lost','red')
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()
