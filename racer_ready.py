
import random
import pygame

pygame.init()
game_wight = 400
game_height = 600
persons_wight = 50
persons_height = 100
game_speed = 60
player_speed = 8
enemy_speed = 8
enemy_surface = pygame.Surface((persons_wight, persons_height))
enemy_image = pygame.image.load('Enemy.png')
player_surface = pygame.Surface((persons_wight, persons_height))
player_image = pygame.image.load('Player.png')
background_surface = pygame.Surface((game_wight, game_height))
background_image = pygame.image.load('AnimatedStreet.png')
screen = pygame.display.set_mode((game_wight, game_height))
stop_game = False
x = random.randint(0, game_wight - persons_wight)
x_enemy = random.randint(2, game_wight - persons_wight - 2)
y_enemy = 0
clock = pygame.time.Clock()
#    money mode
mon_mode = False
moment = random.randint(game_speed, game_speed * 2)
money_size = 50
cycle = 0
score = 0
y_money = 0 - money_size
x_money = 0
#    score time
score_time = 0
#     font set
font = pygame.font.SysFont('arial', 20)
while not stop_game:
    screen.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            stop_game = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and x < game_wight - persons_wight:
        x += player_speed
    if pressed[pygame.K_LEFT] and x > 0:
        x -= player_speed
    if x < 0:
        x = 0
    if x > game_wight - persons_wight:
        x = game_wight - persons_wight
    #    money mode cfg
    cycle += 1
    if moment < cycle and mon_mode == False:
        mon_mode = True
        x_money = random.randrange(0, game_wight, money_size)
        y_money = 0 - money_size
    if y_money < 600 and mon_mode:
        y_money += enemy_speed
    if y_money > 600 and mon_mode:
        mon_mode = False
        moment = random.randint(game_speed * 2, game_speed * 5)
        cycle = 0
        print("ooops")
    if x_money - money_size < x < x_money + money_size and game_height - (3 * money_size) < y_money < game_height and mon_mode == True:
        mon_mode = False
        moment = random.randint(game_speed, game_speed * 2)
        cycle = 0
        score += 1
    #     font set
    text = font.render(str(score), True, (255, 0, 0))
    screen.blit(text, (5, 5))
    screen.blit(enemy_image, (x_enemy, y_enemy))
    screen.blit(player_image, (x, game_height - persons_height))
    if mon_mode:
        pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(x_money, y_money, money_size, money_size))
    if y_enemy < game_height:
        y_enemy += enemy_speed
    else:
        x_enemy = random.randint(2, game_wight - persons_wight - 2)
        y_enemy = -1 * persons_height
        enemy_speed += 0.3
        score_time += 1
    text_score = font.render(str(score_time), True, (255, 0, 0))
    screen.blit(text_score, (game_wight - 50, 5))
    if x_enemy - persons_wight < x < x_enemy + persons_wight and game_height - (2 * persons_height) + 20 < y_enemy < game_height:
        stop_game = True
    pygame.display.flip()
    clock.tick(game_speed)
