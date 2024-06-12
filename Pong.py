import pygame
import sys

# Initialisieren von Pygame
pygame.init()

# Einstellungen für das Spiel
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Einfaches Pong-Spiel")
clock = pygame.time.Clock()

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball Einstellungen
initial_ball_speed = [3, 3]
ball_speed = initial_ball_speed[:]
ball = pygame.Rect(width // 2 - 15, height // 2 - 15, 30, 30)

# Schläger Einstellungen
paddle_speed = 6
paddle1 = pygame.Rect(50, height // 2 - 60, 10, 120)
paddle2 = pygame.Rect(width - 60, height // 2 - 60, 10, 120)

# Punkte
score1 = 0
score2 = 0
font = pygame.font.Font(None, 74)

def move_paddles(keys):
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= paddle_speed
    if keys[pygame.K_s] and paddle1.bottom < height:
        paddle1.y += paddle_speed
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2.bottom < height:
        paddle2.y += paddle_speed

def move_ball():
    global ball_speed, score1, score2
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed[1] = -ball_speed[1]
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed[0] = -ball_speed[0]
        ball_speed[0] *= 1.1
        ball_speed[1] *= 1.1

    if ball.left <= 0:
        score2 += 1
        reset_ball()
    elif ball.right >= width:
        score1 += 1
        reset_ball()

def reset_ball():
    global ball_speed
    ball.center = (width // 2, height // 2)
    ball_speed = initial_ball_speed[:]

def draw_score():
    text = font.render(str(score1), True, WHITE)
    screen.blit(text, (width // 4, 10))
    text = font.render(str(score2), True, WHITE)
    screen.blit(text, (3 * width // 4, 10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    move_paddles(keys)
    move_ball()

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (width // 2, 0), (width // 2, height))
    draw_score()

    pygame.display.flip()
    clock.tick(60)
