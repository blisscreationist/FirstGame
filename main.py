import pygame
import random
import time


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/marianeuro8_Picture_for_the_shooting_gallery_game_application_dcc5b952-14e1-41e3-a589-51e7e852eb47.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

font = pygame.font.Font(None, 36)

score = 0
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))


game_time = 30
start_time = time.time()


target_speed_x = random.choice([0, 0])
target_speed_y = random.choice([0, 0])

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                score += 1


    target_x += target_speed_x
    target_y += target_speed_y

    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    screen.blit(target_img, (target_x, target_y))


    score_text = font.render(f"Ваши очки: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


    elapsed_time = time.time() - start_time
    remaining_time = max(0, game_time - int(elapsed_time))
    timer_text = font.render(f"Время: {remaining_time}", True, (255, 255, 255))
    screen.blit(timer_text, (SCREEN_WIDTH - 150, 10))

    if remaining_time == 0:
        running = False

    pygame.display.update()

print(f"Ваш счет: {score}")

pygame.quit()



