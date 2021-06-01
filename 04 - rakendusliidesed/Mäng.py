import pygame
import time
import random
ekraan = pygame.display.set_mode((1920, 980))
pygame.init()
ekraan.fill((128, 255, 212))
dog_y = 200
dog_x = 100
kiirus = 0.6
dog_kiirus_x = 0
dog_kiirus_y = 0
kont_x =1700
kont_y =800
punkt = 0
pygame.draw.rect(ekraan, (255, 128, 171), (320, 240, 200, 100))
dog = pygame.image.load("dog.png")
kont =pygame.image.load("kont.png")
ekraan.blit(dog, (dog_x, dog_y))
ekraan.blit(kont, (1700, 800))
font = pygame.font.SysFont("Comic Sans MS", 24)
tekst = font.render("Tahan konti?", True, (0, 0, 0))
ekraan.blit(tekst, ((dog_x+100), (dog_y+30)))
dog = pygame.transform.flip(dog, True, False)
pygame.display.flip()
kell = pygame.time.Clock()
mäng_käib= True
while mäng_käib:
    dt = kell.tick(60)
    sisend = pygame.event.poll()
    if sisend.type == pygame.QUIT:
        mäng_käib = False
    vajutatud = pygame.key.get_pressed()
    if vajutatud[pygame.K_UP]:
        dog_kiirus_y = -kiirus
    elif vajutatud[pygame.K_DOWN]:
        dog_kiirus_y = kiirus
    else:
        dog_kiirus_y = 0
    if vajutatud[pygame.K_UP] and vajutatud[pygame.K_DOWN]:
        dog_kiirus_y = 0

    if vajutatud[pygame.K_LEFT]:
        dog_kiirus_x = -kiirus
    elif vajutatud[pygame.K_RIGHT]:
        dog_kiirus_x = kiirus
    else:
        dog_kiirus_x = 0
    if vajutatud[pygame.K_RIGHT] and vajutatud[pygame.K_LEFT]:
        dog_kiirus_x = 0
    if dog_kiirus_x and dog_kiirus_y:
        dog_kiirus_x /= 2**0.5
        dog_kiirus_y /= 2**0.5

        
    ekraan.fill((128, 255, 212))
    ekraan.blit(dog, (dog_x, dog_y))
    ekraan.blit(kont, (kont_x, kont_y))
    tekst = font.render(str(punkt), True, (0, 0, 0))
    ekraan.blit(tekst, ((100), (30)))
    pygame.display.flip()
    dog_x += dog_kiirus_x * dt
    dog_y += dog_kiirus_y * dt
    dog_rect = ekraan.blit(dog, (dog_x, dog_y))
    kont_rect = ekraan.blit(kont,(kont_x, kont_y))
    
    if dog_rect.colliderect(kont_rect):
        punkt += 1
        kont_x = random.randint(0, 1920 - kont.get_width())
        kont_y = random.randint(0, 980 - kont.get_width())
        print(punkt)
        
    
pygame.quit()


