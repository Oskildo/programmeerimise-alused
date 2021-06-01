import pygame
import time
ekraan = pygame.display.set_mode((1920, 980))
pygame.init()
ekraan.fill((128, 255, 212))
dog_y = 200
dog_x = 100
dog_kiirus_x = 0.15
dog_kiirus_y = 0.06
pygame.draw.rect(ekraan, (255, 128, 171), (320, 240, 200, 100))
dog = pygame.image.load("dog.png")
kont =pygame.image.load("kont.png")
ekraan.blit(dog, (dog_x, dog_y))
ekraan.blit(kont, (1700, 800))
font = pygame.font.SysFont("Comic Sans MS", 24)
tekst = font.render("Kus mu kont on?", True, (0, 0, 0))
ekraan.blit(tekst, ((dog_x+100), (dog_y+30)))
pygame.display.flip()
time.sleep(2)
dog = pygame.transform.flip(dog, True, False)
ekraan.blit(dog, (dog_x, dog_y))
tekst = font.render("Ah seal see on.", True, (0, 0, 0))
ekraan.blit(tekst, ((dog_x+100), (dog_y+30)))
pygame.display.flip()
time.sleep(2)
kell = pygame.time.Clock()
print(dog_y)
while True:
    dt = kell.tick(60)
    sisend = pygame.event.poll()
    if sisend.type == pygame.QUIT:
        break
    ekraan.fill((128, 255, 212))
    ekraan.blit(dog, (dog_x, dog_y))
    ekraan.blit(kont, (1700, 800))
    pygame.display.flip()
    dog_x += dog_kiirus_x * dt
    dog_y += dog_kiirus_y * dt
    if dog_y >= 600:
        dog_kiirus_x = 0
        dog_kiirus_y = 0
        tekst = font.render("Yay. :)", True, (0, 0, 0))
        ekraan.blit(tekst, ((dog_x+100), (dog_y+30)))
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
<<<<<<< Updated upstream
pygame.quit()
=======
pygame.quit()
>>>>>>> Stashed changes
