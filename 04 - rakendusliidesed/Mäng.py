import pygame
import time
import random
display_x = 980
ekraan = pygame.display.set_mode((display_x, 980))
pygame.init()
ekraan.fill((128, 255, 212))
spaceship_y =800
spaceship_x = 400
Enspaceship_y =100
Enspaceship_x = 590
kiirus = 0.6
Enspaceship_kiirus = kiirus
spaceship_kiirus_x = 0
spaceship_kiirus_y = 0
Efire_x =1700
Efire_y =0
health = 3
spaceship = pygame.image.load("spaceship.png")
Enspaceship = pygame.image.load("Enemy_spaceship.png")
SPFire =pygame.image.load("fire_friendly.png")
Efire =pygame.image.load("Fire_unfriendly.png")
EHealth =pygame.image.load("Fire_unfriendly.png")
Efire = pygame.transform.scale(Efire, (12,46))
EHealth = pygame.transform.scale(EHealth,(200,100))
SPFire = pygame.transform.scale(SPFire, (36,980))
ekraan.blit(spaceship, (spaceship_x, spaceship_y+10))
ekraan.blit(Efire,(0,0))
spaceship = pygame.transform.scale(spaceship, (22*2,69*2))
ekraan.blit(Efire, (1700, 800))
font = pygame.font.SysFont("Comic Sans MS", 24)
tekst = font.render(" ", True, (255, 255, 255))
attack = font.render(" ", True, (255,255,255))
spaceship = pygame.transform.flip(spaceship, True, False)
pygame.display.flip()
kell = pygame.time.Clock()
mäng_käib= True
ticks = 0
firing = False
cooldown = 240
oh_no = 200
SPFire_rect = ekraan.blit(SPFire, (0,0))
while mäng_käib:
    dt = kell.tick(60)
    sisend = pygame.event.poll()
    if sisend.type == pygame.QUIT:
        mäng_käib = False
    vajutatud = pygame.key.get_pressed()
    if vajutatud[pygame.K_UP]:
        spaceship_kiirus_y = -kiirus
    elif vajutatud[pygame.K_DOWN]:
        spaceship_kiirus_y = kiirus
    else:
        spaceship_kiirus_y = 0
    if vajutatud[pygame.K_UP] and vajutatud[pygame.K_DOWN]:
        spaceship_kiirus_y = 0

    if vajutatud[pygame.K_LEFT]:
        spaceship_kiirus_x = -kiirus
    elif vajutatud[pygame.K_RIGHT]:
        spaceship_kiirus_x = kiirus
    else:
        spaceship_kiirus_x = 0
    if vajutatud[pygame.K_RIGHT] and vajutatud[pygame.K_LEFT]:
        spaceship_kiirus_x = 0
    if spaceship_kiirus_x and spaceship_kiirus_y:
        spaceship_kiirus_x /= 2**0.5
        spaceship_kiirus_y /= 2**0.5
    if vajutatud[pygame.K_SPACE] and cooldown >= 240:
        cooldown = 0
        ticks = 0
        firing = True
     
    ekraan.fill((128, 255, 212))
    pygame.draw.rect(ekraan, (0, 0, 0), (0, 0, 280, 980))
    ekraan.blit(Enspaceship, (Enspaceship_x, Enspaceship_y))
    ekraan.blit(spaceship, (spaceship_x, spaceship_y))
    ekraan.blit(Efire, (Efire_x, Efire_y))
    ekraan.blit(EHealth, (25, 100))
    tekst = font.render(("Health: "+ str(health)), True, (255, 255, 255))
    attack = font.render(("Attack cooldown: "+ str(240-cooldown)), True, (255, 255, 255))
    if cooldown >= 240:
        attack = font.render("Attack ready", True, (255, 255, 255))
    ekraan.blit(tekst, ((25), (30)))
    ekraan.blit(attack, (25, 60))
    pygame.display.flip()
    spaceship_rect = ekraan.blit(spaceship, (spaceship_x, spaceship_y))
    Enspaceship_rect = ekraan.blit(Enspaceship, (Enspaceship_x, Enspaceship_y))
    Efire_rect = ekraan.blit(Efire,(Efire_x, Efire_y))
    spaceship_x += spaceship_kiirus_x * dt
    spaceship_y += spaceship_kiirus_y * dt
    Efire_y += 1*dt
    Enspaceship_x += Enspaceship_kiirus *dt
    if (random.randint(0,1000))% 59== 0:
        Enspaceship_kiirus =-Enspaceship_kiirus
        print(Enspaceship_kiirus)
    if (980-Efire_y)<0:
        Efire_y = Enspaceship_y+Enspaceship.get_height()
        Efire_x = Enspaceship_x+round(Enspaceship.get_width()/2)
    if Enspaceship_rect.colliderect(SPFire_rect):
        oh_no -=1
        if oh_no == 0:
            tekst = font.render("you win!", True, (0, 0, 0))
            ekraan.blit(tekst, ((spaceship_x +100), (spaceship_y +30)))
            pygame.display.flip()
            time.sleep(4)
            pygame.quit()
        print(100-round(oh_no/100))
        EHealth = pygame.transform.scale(EHealth, (oh_no, 100))
        pygame.display.flip()
    if spaceship_rect.colliderect(Efire_rect):
        health -= 1
        Efire_x = random.randint(280, display_x - Efire.get_width())
        Efire_y = 0 - Efire.get_width()
    if health <=0:
        tekst = font.render(("Health: "+ str(health)), True, (0, 0, 0))
        ekraan.blit(tekst, ((100), (30)))
        pygame.display.flip()
        tekst = font.render("you lose!", True, (0, 0, 0))
        ekraan.blit(tekst, ((spaceship_x +100), (spaceship_y +30)))
        pygame.display.flip()
        time.sleep(4)
        pygame.quit()
    if ticks <= 60 and firing == True:
        ekraan.blit(SPFire, (spaceship_x+12, spaceship_y-980))
        pygame.display.flip()
        SPFire_rect = ekraan.blit(SPFire, (spaceship_x+12, spaceship_y-980))
    else:
        SPFire_rect = ekraan.blit(SPFire, (0,0))
    if spaceship_y <=800-spaceship.get_height():
        spaceship_y = 801-spaceship.get_height()
    elif spaceship_y >=980-spaceship.get_height():
        spaceship_y = 980 -spaceship.get_height()
    if spaceship_x >= display_x - spaceship.get_width():
        spaceship_x = display_x - spaceship.get_width()
    elif spaceship_x <= 280:
        spaceship_x = 280
    if Enspaceship_x >= display_x - Enspaceship.get_width():
        Enspaceship_x = display_x - Enspaceship.get_width()
    elif Enspaceship_x <= 280:
        Enspaceship_x = 280
    print(Efire_y)
    ticks +=1
    cooldown +=1

        
    
pygame.quit()
 

