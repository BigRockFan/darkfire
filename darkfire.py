#Pygame
#Ultimate Bridge Task Year 2
import pygame
import random
import time
import math

WIDTH = 1170
HEIGHT = 685
FPS = 60# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (95,95,95)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Darkfire")
clock = pygame.time.Clock()
darkImg1 = pygame.image.load('darkfire.png')
darkImg2 = pygame.image.load('iced_darkfire.png')
darkImg3 = pygame.image.load('shook_darkfire.png')
darkImg4 = pygame.image.load('darkfireMelee.png')
darkImg5 = pygame.image.load('darkfireRed.png')
darkImg6 = pygame.image.load('darkfireWhite.png')
ballice = pygame.image.load('iceball.png')
meleeImg = pygame.image.load('mage.png')
ballfire = pygame.image.load('balls.png')
power = pygame.image.load('speed.png')
power2 = pygame.image.load('heal.png')
power3 = pygame.image.load('damage.png')
rock = pygame.image.load("fire1.png")
grass = pygame.image.load("grass.png")
icemage = pygame.image.load('icemage.png')
bolt = pygame.image.load('bolt.png')
electric = pygame.image.load('electric.png')
music = pygame.mixer.music.load("music.ogg")
#pygame.mixer.music.play(-1)
#pygame.mixer.music.set_volume(0.25)
fireController = 2
iceController = 3
darkfireController = 0
electricController = 1
font = pygame.font.SysFont(None,100)
scoreFont = pygame.font.SysFont(None,50)
wait = font.render("3",True,(WHITE))
wait2 = font.render("2",True,(WHITE))
wait3 = font.render("1",True,(WHITE))
go = font.render("GO!!!",True,(WHITE))

intor=pygame.image.load("introPic.png")

font = pygame.font.SysFont('comicsans', 60, True)                                             

#screen = pygame.display.set_mode((WIDTH, HEIGHT))

def ice():
    
    xF=10
    yF=320
    xI=90
    yI=320
    xE=170
    yE=320
    imageFire=meleeImg
    imageIce=icemage
    imageEle=electric
    positionFire=imageFire.get_rect()
    positionIce=imageIce.get_rect()
    positionEle=imageEle.get_rect()
    screen.blit(imageFire,(xF,yF))
    screen.blit(imageIce,(xI,yI))
    screen.blit(imageEle,(xE,yE))
    pygame.display.update()
    
    running=True
    while running:
        screen.blit(intor,(0,0))
        textStart=font.render("Press space to start",1,RED)

        screen.blit(textStart,(450,200))
        textName=font.render("Dark Fire: Uprising",1,YELLOW)

        screen.blit(textName,(450,150))
        xF=xF+2
        xI=xI+2
        xE=xE+2
        screen.blit(imageFire,(xF,yF))
        screen.blit(imageIce,(xI,yI))
        screen.blit(imageEle,(xE,yE))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()                    
            
             
        #if xF>WIDTH:
               # xF=0
        #if xI>WIDTH:
               # xI=0
        #if xE>WIDTH:
         #       xE=0        
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
        
            gameLoop()
        pygame.display.update()
            
def introLoop():
    music = pygame.mixer.music.load("halo.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.25)
    ice()
def gameLoop():
    music = pygame.mixer.music.load("music.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.25)
    class DarkFire(pygame.sprite.Sprite):
        def __init__(self):
            self.x = (WIDTH * 0.598)
            self.y = (HEIGHT * 0.52)
            pygame.sprite.Sprite.__init__(self)
            self.image = darkImg1
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.radius = 25
            #enable to see hit radius
            #pygame.draw.rect(self.image,RED,self.rect,0)
            #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
            self.rect.centerx = self.x
            self.rect.bottom = self.y
            self.cd = 0
            self.cd2 = 0
            self.cd3 = 0
            self.cd4 = 0
            self.cd5 = 0
            self.cd6 = -2000
            self.heal_cooldown = 0
            self.melee_cooldown = 0
            self.immune_cooldown = 0
            self.rage_cooldown = 0
            self.rage_time = 2000
            self.immune_time = 2000
            self.controllernum = darkfireController
            self.controller = -1
            self.checkInput()
            self.totalHP = 2500 #constant hp
            self.hp = 2500 #variable hp
            self.heal = 750 #heal amount
            self.alive = True 
            self.shock = False
            self.freeze = False
            self.speed = 9
            self.constspeed = 9
            self.meleeSkinOn = False
            self.immune = False
            self.meleedamage = 200
            self.discount = False
            self.regular = True

        def checkControllerButton(self):
            pygame.joystick.init()
            joystick = pygame.joystick.Joystick(self.controllernum)
            joystick.init()
            button = joystick.get_button(self.controllernum)
            button2 = joystick.get_button(1)
            button3 = joystick.get_button(2)
            button4 = joystick.get_button(3)
            buttons = [button,button2,button3,button4]
            return buttons
        def checkInput(self):
            try:
                a = self.checkController()
                self.controller = 0
                print("Controller "+str(self.controllernum)+" connected")
            except:
                self.controller = 1
                print("Controller "+str(self.controllernum)+" not plugged in. Use arrow keys.")
          
        def update(self):
            if time > speedP.destruct + speedP.cooldown and self.regular == True:
                self.speed = 9
            if time > damageP.destruct + damageP.cooldown and self.regular == True:
                self.meleedamage = 200
            if self.controller == 0:
                b = self.checkControllerButton()
                if b[0] == 1:
                    self.immunity()
                if b[1] == 1:
                    self.melee()
                if b[2] == 1:
                    self.healing()
                if b[3] == 1:
                    self.rage()
                        
            if self.discount == False:
                self.immune_cooldown = 10000
                self.heal_cooldown = 20000
            if self.immune:
                if time > self.cd + self.immune_time:
                    self.image = darkImg1
                    self.immune = False
                else:
                    self.image = darkImg6
                    if self.controller == 0:
                        a = self.checkController()
                        self.rect.x += self.speed*a[0]
                        self.rect.y += self.speed*a[1]
                    
            elif (self.shock and time <= shock.electricTime + shock.electricCooldown):
                self.shock = True
                self.image = darkImg3
            elif (self.shock and time > shock.electricTime + shock.electricCooldown):
                self.shock = False
                self.image = darkImg1
                shock.electricTime = 0
            else:
                if (self.freeze and time <= slow.iceTime + slow.iceCooldown):
                    self.speed = self.speed * slow.slowdownpercent
                    self.image = darkImg2
                elif (self.freeze and time > slow.iceTime + slow.iceCooldown):
                    self.freeze = False
                    slow.iceTime = 0
                    self.speed = self.constspeed
                    self.image = darkImg1
                if self.meleeSkinOn and time >= self.cd5 + 1500:
                    self.image = darkImg1
                    self.meleeSkinOn = False
                    pos = self.rect.center
                    self.rect = self.image.get_rect(center = pos)
                        
                if self.regular and time < self.cd6 + self.rage_time:
                    self.image = darkImg5
                    self.regular = False
                if self.regular == False and time > self.cd6 + self.rage_time:
                    self.meleedamage /= 1.5
                    self.speed /= 1.5
                    self.regular = True
                    self.image = darkImg1
                if self.controller == 0:
                    a = self.checkController()
                    
                    self.rect.x += self.speed*a[0]
                    self.rect.y += self.speed*a[1]
                    
                else:
                    keystate = pygame.key.get_pressed()
                    if keystate[pygame.K_LEFT]:
                        self.rect.x -= self.speed
                    if keystate[pygame.K_UP]:
                        self.rect.y -= self.speed
                    if keystate[pygame.K_DOWN]:
                        self.rect.y += self.speed
                    if keystate[pygame.K_RIGHT]:
                        self.rect.x += self.speed

                if self.rect.right > WIDTH:
                    self.rect.right = WIDTH
                if self.rect.left < 0:
                    self.rect.left = 0
                if self.rect.top < 0:
                    self.rect.top = 0
                if self.rect.bottom > HEIGHT:
                    self.rect.bottom = HEIGHT

            # TEXT HP NEEDS TO BE FIGURED OUT
            #text = font.render(str(player.hp), 1, (0,0,0))
            #screen.blit(text, (player.rect.x+25, player.rect.y+80))
            pygame.draw.rect(screen, RED,
                             pygame.Rect(self.rect.x+10, self.rect.y+75,
                             50, 10))
            pygame.draw.rect(screen, GREEN, pygame.Rect(self.rect.x+10,
                            self.rect.y+75, 50*(self.hp/self.totalHP), 10))
            if self.alive == False:
                # PLAY DEATH ANIMATION OR CUTSCENES HERE
                self.kill()

            
            ##boundaries
        def checkController(self):
            pygame.joystick.init()
            joystick = pygame.joystick.Joystick(self.controllernum)
            joystick.init()
            return [joystick.get_axis(0), joystick.get_axis(1)]
        def rage(self):
            if time > self.cd6 + self.rage_cooldown:
                self.immune_cooldown *= 0.6
                self.heal_cooldown *= 0.6
                self.meleedamage *= 1.5
                self.speed *= 1.5
                self.cd6 = pygame.time.get_ticks()
                self.rage_cooldown = 20000
                self.raged = True
                self.discount = True
        def immunity(self):
            if time > self.cd + self.immune_cooldown:
                self.immune = True
                self.shock = False
                self.freeze = False
                self.cd = pygame.time.get_ticks()
                self.immune_cooldown = 15000
                self.discount = False
        def melee(self):
            if time > self.cd5 + self.melee_cooldown:
                self.image = darkImg4
                pos = self.rect.center
                self.rect = self.image.get_rect(center = pos)
                self.cd5 = pygame.time.get_ticks()
                self.melee_cooldown = 5000
                self.meleeSkinOn = True
                hitFire = pygame.sprite.collide_rect(self, damage)
                hitShock = pygame.sprite.collide_rect(self, shock)
                hitIce = pygame.sprite.collide_rect(self, slow)
                
                if hitFire:
                    damage.hp = damage.hp - self.meleedamage
                    if damage.hp <= 0:
                        damage.hp = 0
                        damage.alive = False
                if hitShock:
                    shock.hp -= self.meleedamage
                    if shock.hp <= 0:
                        shock.hp = 0
                        shock.alive = False
                if hitIce:
                    slow.hp -= self.meleedamage
                    if slow.hp <= 0:
                        slow.hp = 0
                        slow.alive = False
                
        def healing(self):
            if time > self.cd2 + self.heal_cooldown:
                self.hp += self.heal
                if self.hp > 2500:
                    self.hp = 2500
                self.cd2 = pygame.time.get_ticks()
                self.heal_cooldown = 10000
                self.discount = False
            
            
            
            
            

    class Ice(pygame.sprite.Sprite):
        def __init__(self):
            self.x = (WIDTH * 0.59)
            self.y = (HEIGHT * 0.95)
            pygame.sprite.Sprite.__init__(self)
            self.image = icemage
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.radius = 25
            #enable to see hit radius
            #pygame.draw.rect(self.image,RED,self.rect,0)
            #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
            self.rect.centerx = self.x
            self.rect.bottom = self.y
            self.time = pygame.time.get_ticks()
            self.cooldown = 3000
            self.controllernum = iceController
            self.controller = -1
            self.checkInput()
            self.reload = 1000 #SUBJECT TO CHANGE
            self.destruct = -1 * self.reload
            self.attack = 80
            self.iceTime = 0
            self.iceCooldown = 1000
            self.slowdownpercent = 0.5 # freeze slows darkfire down to 50% speed
            self.speed = 8
            self.hp = 800
            self.heal = 200
            self.totalHP = 800
            self.alive = True
            
        def checkControllerButton(self):
            pygame.joystick.init()
            joystick = pygame.joystick.Joystick(self.controllernum)
            button = joystick.get_button(self.controllernum)
            button2 = joystick.get_button(1)
            button3 = joystick.get_button(2)
            button4 = joystick.get_button(3)
            buttons = [button,button2,button3,button4]
            return buttons
        def checkController(self):
            pygame.joystick.init()
            joystick = pygame.joystick.Joystick(self.controllernum)
            joystick.init()
            return [joystick.get_axis(0), joystick.get_axis(1)]
        def checkInput(self):
            try:
                a = self.checkController()
                self.controller = 0
                print("Controller "+str(self.controllernum)+" connected")
            except:
                self.controller = 1
                print("Controller "+str(self.controllernum)+" not plugged in. Use T F G H.")        
        def update(self):
            if time > speedP.destruct + speedP.cooldown:
                self.speed = 8
            if time > damageP.destruct + damageP.cooldown:
                self.attack = 80

            if self.controller == 0:
                a = self.checkController()
                b = self.checkControllerButton()
                if b[0] == 1:
                    self.fire1()
                self.rect.x += self.speed*a[0]
                self.rect.y += self.speed*a[1]

            else:
                keystate = pygame.key.get_pressed()
                if keystate[pygame.K_f]:
                    self.rect.x -= self.speed
                if keystate[pygame.K_t]:
                    self.rect.y -= self.speed
                if keystate[pygame.K_g]:
                    self.rect.y += self.speed
                if keystate[pygame.K_h]:
                    self.rect.x += self.speed

            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            elif self.rect.left < 0:
                self.rect.left = 0
            if self.rect.top < 0:
                self.rect.top = 0
            elif self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT

            pygame.draw.rect(screen, RED,
                             pygame.Rect(self.rect.x+10, self.rect.y+75,
                             50, 10))
            pygame.draw.rect(screen, GREEN, pygame.Rect(self.rect.x+10,
                            self.rect.y+75, 50*(self.hp/self.totalHP), 10))
            if self.alive == False:
                # PLAY DEATH ANIMATION OR CUTSCENES HERE
                self.kill()        
        def fire1(self):
            if time > self.destruct + self.reload:
                fire = RangedFireball(self.rect.centerx, self.rect.centery,
                                      ballice, self.controllernum, self.attack)
                all_sprites.add(fire)
                fires.add(fire)
                self.destruct = pygame.time.get_ticks()
            

        

    class Fire(pygame.sprite.Sprite):
        def __init__(self):
            self.x = (WIDTH * 0.31)
            self.y = (HEIGHT * 0.62)
            pygame.sprite.Sprite.__init__(self)
            self.image = meleeImg
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.radius = 25
            #enable to see hit radius
            #pygame.draw.rect(self.image,RED,self.rect,0)
            #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
            self.rect.centerx = self.x
            self.rect.bottom = self.y
            self.time = pygame.time.get_ticks()
            self.cooldown = 3000
            self.controllernum = fireController
            self.controller = -1
            self.checkInput()
            self.reload = 600 #SUBJECT TO CHANGE
            self.destruct = -1 * self.reload
            self.attack = 120
            self.speed = 8
            self.heal = 200
            self.hp = 800
            self.totalHP = 800
            self.alive = True
            
        def checkControllerButton(self):
            clock = pygame.time.Clock()
            pygame.joystick.init()
            joystick = pygame.joystick.Joystick(self.controllernum)
            button = joystick.get_button(self.controllernum)
            button2 = joystick.get_button(1)
            button3 = joystick.get_button(2)
            button4 = joystick.get_button(3)
            buttons = [button,button2,button3,button4]
            return buttons

        def checkController(self):
            pygame.joystick.init()
            joystick = pygame.joystick.Joystick(self.controllernum)
            joystick.init()
            return [joystick.get_axis(0), joystick.get_axis(1)]
            
        def checkInput(self):
            try:
                a = self.checkController()
                self.controller = 0
                print("Controller "+str(self.controllernum)+" connected")
            except:
                self.controller = 1
                print("Controller "+str(self.controllernum)+" not plugged in. Use W A S D.")
        def update(self):
            if time > speedP.destruct + speedP.cooldown:
                self.speed = 8
            if time > damageP.destruct + damageP.cooldown:
                self.attack = 120
            if self.controller == 0:
                a = self.checkController()
                b = self.checkControllerButton()
                if b[0] == 1:
                    self.fire1()
                self.rect.x += self.speed*a[0]
                self.rect.y += self.speed*a[1]

            else:
                keystate = pygame.key.get_pressed()
                if keystate[pygame.K_a]:
                    self.rect.x -= self.speed
                if keystate[pygame.K_w]:
                    self.rect.y -= self.speed
                if keystate[pygame.K_s]:
                    self.rect.y += self.speed
                if keystate[pygame.K_d]:
                    self.rect.x += self.speed
                    
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            elif self.rect.left < 0:
                self.rect.left = 0
            if self.rect.top < 0:
                self.rect.top = 0
            elif self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT

            pygame.draw.rect(screen, RED,
                             pygame.Rect(self.rect.x+10, self.rect.y+75,
                             50, 10))
            pygame.draw.rect(screen, GREEN, pygame.Rect(self.rect.x+10,
                            self.rect.y+75, 50*(self.hp/self.totalHP), 10))

            if self.alive == False:
                # PLAY DEATH ANIMATION OR CUTSCENES HERE
                self.kill()
            
        def fire1(self):
            
            if time > self.destruct + self.reload:
                fire = RangedFireball(self.rect.centerx, self.rect.centery,
                                      ballfire, self.controllernum, self.attack)
                all_sprites.add(fire)
                fires.add(fire)
                self.destruct = pygame.time.get_ticks()
            #else:
            #   print("reloading..")
    class Electric(pygame.sprite.Sprite):
        def __init__(self):
            self.x = (WIDTH * 0.89)
            self.y = (HEIGHT * 0.61)
            pygame.sprite.Sprite.__init__(self)
            self.image = electric
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.radius = 25
            #enable to see hit radius
            #pygame.draw.rect(self.image,RED,self.rect,0)
            #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
            self.rect.centerx = self.x
            self.rect.bottom = self.y
            self.time = pygame.time.get_ticks()
            self.cooldown = 3000
            self.controllernum = electricController
            self.controller = -1
            self.checkInput()
            self.reload = 4000 #SUBJECT TO CHANGE
            self.destruct = -1 * self.reload
            self.attack = 180
            self.electricTime = 0
            self.electricCooldown = 2000
            self.speed = 8
            self.heal = 200
            self.hp = 800
            self.totalHP = 800
            self.alive = True
            
        def checkControllerButton(self):
            pygame.joystick.init()
            joystick = pygame.joystick.Joystick(self.controllernum)
            button = joystick.get_button(self.controllernum)
            button2 = joystick.get_button(1)
            button3 = joystick.get_button(2)
            button4 = joystick.get_button(3)
            buttons = [button,button2,button3,button4]
            return buttons

        def checkController(self):
            pygame.joystick.init()
            joystick = pygame.joystick.Joystick(self.controllernum)
            joystick.init()
            return [joystick.get_axis(0), joystick.get_axis(1)]

        def checkInput(self):
            try:
                a = self.checkController()
                self.controller = 0
                print("Controller "+str(self.controllernum)+" connected")
            except:
                self.controller = 1
                print("Controller "+str(self.controllernum)+" not plugged in. Use I J K L.")
        def update(self):
            if time > speedP.destruct + speedP.cooldown:
                self.speed = 8
            if time > damageP.destruct + damageP.cooldown:
                self.attack = 180
            if time > speedP.destruct + speedP.respawn:
                speedPowerup.add(speedP)
                all_sprites.add(speedP)
            if time > damageP.destruct + damageP.respawn and damageP.alive() == False:
                damagePowerup.add(damageP)
                all_sprites.add(damageP)
            if time > healP.destruct + healP.respawn and healP.alive() == False:
                healPowerup.add(healP)
                all_sprites.add(healP)
            if time > damageP.destruct + damageP.cooldown:
                self.attack = 180
            if self.controller == 0:
                a = self.checkController()
                b = self.checkControllerButton()
                if b[0] == 1:
                    self.fire1()
                self.rect.x += self.speed*a[0]
                self.rect.y += self.speed*a[1]
            else:
                keystate = pygame.key.get_pressed()
                if keystate[pygame.K_j]:
                    self.rect.x -= self.speed
                if keystate[pygame.K_i]:
                    self.rect.y -= self.speed
                if keystate[pygame.K_k]:
                    self.rect.y += self.speed
                if keystate[pygame.K_l]:
                    self.rect.x += self.speed
                    
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            elif self.rect.left < 0:
                self.rect.left = 0
            if self.rect.top < 0:
                self.rect.top = 0
            elif self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT

            pygame.draw.rect(screen, RED,
                             pygame.Rect(self.rect.x+10, self.rect.y+75,
                             50, 10))
            pygame.draw.rect(screen, GREEN, pygame.Rect(self.rect.x+10,
                            self.rect.y+75, 50*(self.hp/self.totalHP), 10))
            if self.alive == False:
                # PLAY DEATH ANIMATION OR CUTSCENES HERE
                self.kill()
            
        def fire1(self):
            
            if time > self.destruct + self.reload:
                fire = RangedFireball(self.rect.centerx, self.rect.centery,
                                      bolt, self.controllernum, self.attack)
                all_sprites.add(fire)
                fires.add(fire)
                self.destruct = pygame.time.get_ticks()

    class SpeedPowerup(pygame.sprite.Sprite):
        def __init__(self):
            self.cooldown = 2000
            self.destruct = 0
            pygame.sprite.Sprite.__init__(self)
            self.image = power
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(HEIGHT - self.rect.width)
            self.respawn = 60000
        def update(self):
            collide = pygame.sprite.spritecollide(shock,speedPowerup,True)
            collide2 = pygame.sprite.spritecollide(slow,speedPowerup,True)
            collide3 = pygame.sprite.spritecollide(damage,speedPowerup,True)
            collide4 = pygame.sprite.spritecollide(player,speedPowerup,True)
            if collide:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(HEIGHT - self.rect.height)
                self.destruct = pygame.time.get_ticks()
                self.respawn *= 0.80
                shock.speed *= 2
            if collide2:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(HEIGHT - self.rect.height)
                self.destruct = pygame.time.get_ticks()
                self.respawn *= 0.80
                slow.speed *= 2
            if collide3:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(HEIGHT - self.rect.height)
                self.destruct = pygame.time.get_ticks()
                self.respawn *= 0.80
                damage.speed *= 2
            if collide4:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(HEIGHT - self.rect.height)
                self.destruct = pygame.time.get_ticks()
                self.respawn *= 0.80
                player.speed *= 1.5
                
    class HealPowerup(pygame.sprite.Sprite):
        def __init__(self):
            self.cooldown = 3000
            self.destruct = 0
            pygame.sprite.Sprite.__init__(self)
            self.image = power2
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(HEIGHT - self.rect.width)
            self.respawn = 55000
        def update(self):
            collide = pygame.sprite.spritecollide(shock,healPowerup,True)
            collide2 = pygame.sprite.spritecollide(slow,healPowerup,True)
            collide3 = pygame.sprite.spritecollide(damage,healPowerup,True)
            collide4 = pygame.sprite.spritecollide(player,healPowerup,True)
            if collide:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(HEIGHT - self.rect.height)
                self.destruct = pygame.time.get_ticks()
                self.respawn *= 0.90
                shock.hp += shock.heal
                if shock.hp > 2500:
                    shock.hp = 2500
            if collide2:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(HEIGHT - self.rect.height)
                self.destruct = pygame.time.get_ticks()
                self.respawn *= 0.90
                slow.hp += slow.heal
                if slow.hp > 2500:
                    shock.hp = 2500
            if collide3:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(HEIGHT - self.rect.height)
                self.destruct = pygame.time.get_ticks()
                self.respawn *= 0.90
                damage.hp += damage.heal
                if damage.hp > 2500:
                    damage.hp = 2500
            if collide4:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(HEIGHT - self.rect.height)
                self.destruct = pygame.time.get_ticks()
                self.respawn *= 0.90
                player.hp += player.heal
                if player.hp > 2500:
                    player.hp = 2500
    class DamagePowerup(pygame.sprite.Sprite):
        def __init__(self):
            self.cooldown = 3000
            self.destruct = 0
            pygame.sprite.Sprite.__init__(self)
            self.image = power3
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(HEIGHT - self.rect.width)
            self.respawn = 40000
        def update(self):
            collide = pygame.sprite.spritecollide(shock,damagePowerup,True)
            collide2 = pygame.sprite.spritecollide(slow,damagePowerup,True)
            collide3 = pygame.sprite.spritecollide(damage,damagePowerup,True)
            collide4 = pygame.sprite.spritecollide(player,damagePowerup,True)
            if collide:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(HEIGHT - self.rect.height)
                self.destruct = pygame.time.get_ticks()
                self.respawn *= 0.85
                shock.attack *= 2
            if collide2:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(HEIGHT - self.rect.height)
                self.destruct = pygame.time.get_ticks()
                self.respawn *= 0.85
                slow.attack *= 1.5
            if collide3:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(HEIGHT - self.rect.height)
                self.destruct = pygame.time.get_ticks()
                self.respawn *= 0.85
                damage.attack *= 1.2
            if collide4:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(HEIGHT - self.rect.height)
                self.destruct = pygame.time.get_ticks()
                self.respawn *= 0.80
                player.meleedamage *= 1.6
            
           
    class RangedFireball(pygame.sprite.Sprite):
        def __init__(self, x, y, ballpic, controllernum, damage):
            self.destruct =  pygame.time.get_ticks()
            self.cooldown = 2000 #SUBJECT TO CHANGE (maybe electric has more range)
            pygame.sprite.Sprite.__init__(self)
            self.image = ballpic
            self.rect = self.image.get_rect()
            #pygame.draw.rect(self.image,RED,self.rect,0)
            self.rect.centery = y
            self.rect.centerx = x
            self.speed = 20
            self.shockspeed = 30
            if damage == 180:
                self.speed = self.shockspeed
            self.damage = damage
            

            #controller
            pygame.joystick.init()
            for j in range(3):
                joystick = pygame.joystick.Joystick(controllernum)
                joystick.init()
                axes = joystick.get_numaxes()
                listaxes = []
                for i in range(axes):
                    axis = joystick.get_axis(i)
                    if (j == 2):
                        listaxes.append(axis)
                
            self.leftStick= []
            self.leftStick.append(listaxes[0])
            self.leftStick.append(listaxes[1])
            
        def update(self):
            collide = pygame.sprite.groupcollide(fires,ballDestroy,True,False)
            hitDark = pygame.sprite.collide_rect(self, player)
            if time > self.destruct + self.cooldown:
                self.kill()
            if hitDark:
                player.hp -= self.damage
                if player.hp < 0:
                    player.hp = 0
                    player.alive = False
                if self.damage == 180:
                    player.shock = True
                    shock.electricTime =  pygame.time.get_ticks()
                if self.damage == 80:
                    player.freeze = True
                    slow.iceTime = pygame.time.get_ticks()
                    
            
            else:
                #change triangle leg ratios (x and y) so that the hypotenuse is
                #self.

                instX = self.leftStick[0]*self.speed
                instY = self.leftStick[1]*self.speed
                hypotenuse = math.sqrt(math.pow(instX, 2) + math.pow(instY, 2))
                if hypotenuse != 0:
                    multiplyFactor = self.speed/hypotenuse
                    self.rect.y += instY * multiplyFactor
                    self.rect.x += instX * multiplyFactor

        
    class Wall(pygame.sprite.Sprite):
        def __init__(self, x, y):
            #This calls parent (Sprite) Constructor
            pygame.sprite.Sprite.__init__(self)
        
            #Here we create image of wall, fill it with color
            #You can also import an image
            self.image = rock
            self.rect = self.image.get_rect()
            #pygame.draw.rect(self.image,RED,self.rect,0)
            self.rect.x = x
            self.rect.y = y

    running = True
    all_sprites = pygame.sprite.Group()
    all_walls = pygame.sprite.Group()
    fires = pygame.sprite.Group()
    speedPowerup = pygame.sprite.Group()
    damagePowerup = pygame.sprite.Group()
    healPowerup = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    ballDestroy = pygame.sprite.Group()
    damage = Fire()
    slow = Ice()
    shock = Electric()
    player = DarkFire()
    speedP = SpeedPowerup()
    damageP = DamagePowerup()
    healP = HealPowerup()
    wall = (Wall(338,201))
    wall2 = (Wall(160,323))
    wall3 = (Wall(210,537))
    wall4 = (Wall(663,107))
    wall5 = (Wall(867,623))
    wall6 = (Wall(874,340))
    wall7 = (Wall(1058,205))
    walls.add(wall)
    walls.add(wall2)
    walls.add(wall3)
    walls.add(wall4)
    walls.add(wall5)
    walls.add(wall6)
    walls.add(wall7)
    speedPowerup.add(speedP)
    damagePowerup.add(damageP)
    healPowerup.add(healP)
    all_sprites.add(wall)
    all_sprites.add(wall2)
    all_sprites.add(wall3)
    all_sprites.add(wall4)
    all_sprites.add(wall5)
    all_sprites.add(wall6)
    all_sprites.add(wall7)
    all_sprites.add(player)
    all_sprites.add(slow)
    all_sprites.add(damage)
    all_sprites.add(shock)
    all_sprites.add(speedP)
    all_sprites.add(damageP)
    all_sprites.add(healP)
    ballDestroy.add(wall)
    ballDestroy.add(wall2)
    ballDestroy.add(wall3)
    ballDestroy.add(wall4)
    ballDestroy.add(wall5)
    ballDestroy.add(wall6)
    ballDestroy.add(wall7)
    ballDestroy.add(player)
    font = pygame.font.SysFont('comicsans', 30, True)                                             

    while running:
        time = pygame.time.get_ticks()
        clock.tick(FPS)
        screen.blit(grass,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        hits = pygame.sprite.spritecollide(player,walls, False)
        hits2 = pygame.sprite.spritecollide(slow, walls, False)
        hits3 = pygame.sprite.spritecollide(damage, walls, False)
        hits4 = pygame.sprite.spritecollide(shock, walls, False)
        if hits:
            for wall in walls:
                wall_collide = pygame.sprite.collide_rect(player,wall)
                if wall_collide:
                    player.rect.x = darkfirePos[0]
                    player.rect.y = darkfirePos[1]
                    
        if hits2:
            for wall in walls:
                wall_collide = pygame.sprite.collide_rect(slow,wall)
                if wall_collide:
                    slow.rect.x = icePos[0]
                    slow.rect.y = icePos[1]
        if hits3:
            for wall in walls:
                wall_collide = pygame.sprite.collide_rect(damage,wall)
                if wall_collide:
                    damage.rect.x = firePos[0]
                    damage.rect.y = firePos[1]
        if hits4:
            for wall in walls:
                wall_collide = pygame.sprite.collide_rect(shock,wall)
                if wall_collide:
                    shock.rect.x = electricPos[0]
                    shock.rect.y = electricPos[1]
        darkfirePos = [player.rect.x, player.rect.y]
        icePos = [slow.rect.x, slow.rect.y]
        firePos = [damage.rect.x, damage.rect.y]
        electricPos = [shock.rect.x, shock.rect.y]
        all_sprites.update()
        all_sprites.draw(screen)
        if time > 0 and time < 1000:
            import time
            screen.blit(wait,(WIDTH/2,HEIGHT/2))
            pygame.display.update()
            time.sleep(1)
        elif time > 1000 and time < 2000:
            import time
            screen.blit(wait2,(WIDTH/2,HEIGHT/2))
            pygame.display.update()
            time.sleep(1)
        elif time > 2000 and time < 3000:
                import time
                screen.blit(wait3,(WIDTH/2,HEIGHT/2))
                pygame.display.update()
                time.sleep(1)
        elif time > 3000 and time < 4500:
                import time
                screen.blit(go,(WIDTH/2,HEIGHT/2))
                pygame.display.update()

        

        pygame.display.update()
introLoop()
