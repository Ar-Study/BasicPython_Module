import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
screen = pygame.display.set_mode((800, 600))

# Judul dan ikon
pygame.display.set_caption("Game Sederhana")
icon = pygame.image.load('icon.png')  # Pastikan Anda memiliki file icon.png
pygame.display.set_icon(icon)

# Warna
white = (255, 255, 255)
black = (0, 0, 0)

# Pemain
playerImg = pygame.image.load('player.png')  # Pastikan Anda memiliki file player.png
playerX = 370
playerY = 480
playerX_change = 0

# Peluru
bulletImg = pygame.image.load('bullet.png')  # Pastikan Anda memiliki file bullet.png
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"

# Fungsi untuk menggambar pemain
def player(x, y):
    screen.blit(playerImg, (x, y))

# Fungsi untuk menembakkan peluru
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

# Loop utama game
running = True
while running:
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Kontrol pemain
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    playerX += playerX_change
    playerX = max(0, min(playerX, 736))  # Batas layar
    
    # Gerakkan peluru
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    
    player(playerX, playerY)
    pygame.display.update()

