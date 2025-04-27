import pygame

# Ініціалізація Pygame
pygame.init()

# Розміри вікна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Екран очікування")

# Завантаження фону
background_image = pygame.transform.scale(pygame.image.load("background.jpg"), (WIDTH, HEIGHT))

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)
HOVER_BLUE = (100, 160, 210)

# Шрифти
title_font = pygame.font.SysFont("Arial", 60)
desc_font = pygame.font.SysFont("Arial", 30)
button_font = pygame.font.SysFont("Arial", 36)

# Тексти
title_text = title_font.render("Назва гри", True, WHITE)
desc_text = desc_font.render("Уникай ворогів, збирай монети, виживай якомога довше.", True, WHITE)

# Кнопка
button_text = button_font.render("Почати гру", True, WHITE)
button_width, button_height = 250, 60
button_x = WIDTH // 2 - button_width // 2
button_y = 400
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# Початковий екран
first_screen = True
while first_screen:
    screen.blit(background_image, (0, 0))

    # Показуємо назву та опис
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 150))
    screen.blit(desc_text, (WIDTH // 2 - desc_text.get_width() // 2, 250))

    # Перевірка наведення миші
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, HOVER_BLUE, button_rect)
    else:
        pygame.draw.rect(screen, BLUE, button_rect)

    # Показуємо текст кнопки
    screen.blit(button_text, (
        button_x + (button_width - button_text.get_width()) // 2,
        button_y + (button_height - button_text.get_height()) // 2
    ))

    pygame.display.flip()

    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                first_screen = False

import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Налаштування екрану
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Збір монет та ухилення від зомбі")

# Колір
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Швидкість
player_speed = 5
zombie_speed = 3

# Створення об'єктів
player = pygame.Rect(WIDTH // 2, HEIGHT // 2, 40, 40)
coin = pygame.Rect(random.randint(0, WIDTH-20), random.randint(0, HEIGHT-20), 20, 20)
zombies = [pygame.Rect(random.randint(0, WIDTH-40), random.randint(0, HEIGHT-40), 40, 40) for _ in range(5)]

# Головний цикл гри
clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont("Arial", 24)

# Функція для відображення рахунку
def display_score():
    text = font.render("Рахунок: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))
