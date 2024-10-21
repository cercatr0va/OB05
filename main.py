import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Пинг-понг: Игрок против Компьютера")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Настройки ракеток и мяча
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SIZE = 20
PLAYER_SPEED = 7
COMPUTER_SPEED = 6
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Шрифт для счета
font = pygame.font.SysFont(None, 55)

# Начальные координаты
player_paddle = pygame.Rect(50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
computer_paddle = pygame.Rect(SCREEN_WIDTH - 60, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Счет
player_score = 0
computer_score = 0

# Основной игровой цикл
running = True
clock = pygame.time.Clock()

def display_score():
    player_text = font.render(str(player_score), True, WHITE)
    computer_text = font.render(str(computer_score), True, WHITE)
    screen.blit(player_text, (SCREEN_WIDTH // 4, 20))
    screen.blit(computer_text, (SCREEN_WIDTH - SCREEN_WIDTH // 4, 20))

while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.top > 0:
        player_paddle.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN] and player_paddle.bottom < SCREEN_HEIGHT:
        player_paddle.y += PLAYER_SPEED

    # Движение компьютера
    if ball.y > computer_paddle.centery:
        computer_paddle.y += COMPUTER_SPEED
    elif ball.y < computer_paddle.centery:
        computer_paddle.y -= COMPUTER_SPEED

    # Движение мяча
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    # Отскок от стен
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        BALL_SPEED_Y = -BALL_SPEED_Y

    # Отскок от ракеток
    if ball.colliderect(player_paddle) or ball.colliderect(computer_paddle):
        BALL_SPEED_X = -BALL_SPEED_X

    # Проверка на голы
    if ball.left <= 0:
        computer_score += 1
        ball.x, ball.y = SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        BALL_SPEED_X = -BALL_SPEED_X
        BALL_SPEED_Y = random.choice([5, -5])
    if ball.right >= SCREEN_WIDTH:
        player_score += 1
        ball.x, ball.y = SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        BALL_SPEED_X = -BALL_SPEED_X
        BALL_SPEED_Y = random.choice([5, -5])

    # Очистка экрана
    screen.fill(BLACK)

    # Отображение объектов на экране
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, computer_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    # Отображение счета
    display_score()

    # Обновление экрана
    pygame.display.flip()

    # Контроль FPS
    clock.tick(60)

# Завершение Pygame
pygame.quit()
