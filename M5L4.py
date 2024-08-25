from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        self.image = transform.scale(image.load(player_image), (80,80))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
        if keys[K_s]:
            self.rect.y += self.speed
        if keys[K_w]:
            self.rect.y -= self.speed


class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 100:
            self.direction = "up"
        if self.rect.x >= 650:
            self.direction = "down"
        if self.rect.y >= 450:
            self.direction = "left"
        if self.rect.y <= 100:
            self.direction = "right"



        if self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed
        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3

        self.width = wall_width
        self.height = wall_height

        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y  = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((700, 500))
display.set_caption("Tony best maze game")
background = transform.scale(image.load("background.png"), (700, 500))
wall_1 = Wall(158, 23, 27, 100, 20, 450, 10)
wall_2 = Wall(158, 23, 27, 100, 450, 450, 10)
wall_3 = Wall(158, 23, 27, 100, 20, 10, 350)
wall_4 = Wall(158, 23, 27, 100, 125, 100, 10)
wall_5 = Wall(158, 23, 27, 225, 250, 10, 200)
wall_6 = Wall(158, 23, 27, 350, 20, 10, 430)
#player = transform.scale(image.load('slime.png'), (100, 100))
player = Player("slime.png", 5, 5, 3)
#enemy = transform.scale(image.load('enemy.png'), (100, 100))
enemy = Enemy("enemy.png", 100, 100, 4)
enemy2 = Enemy("enemy2.png", 200, 300, 2)
#treasure = transform.scale(image.load('treasure.png'), (100, 100))
treasure = GameSprite("treasure.png", 600, 400, 0)


mixer.init()
mixer.music.load("jungles.ogg")
#mixer.music.play()

is_over = False
finish = False
clock = time.Clock()
FPS = 60
font.init()
font = font.Font(None, 70)


win_text = font.render("YOU WIN!", True, (34,246,90))
lost_text = font.render("YOU LOSE!", True, (136, 0, 164))
while not is_over:
    for e in event.get():
        if e.type == QUIT:
            is_over = True
    if finish != True:
        window.blit(background, (0,0))
        player.update()
        player.reset()
        enemy.update()
        enemy.reset()
        enemy2.update()
        enemy2.reset()
        treasure.reset()
        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        wall_4.draw_wall()
        wall_5.draw_wall()
        wall_6.draw_wall()

    if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, enemy2):
        finish = True
        window.blit(lost_text, (200,200))

    if sprite.collide_rect(player, treasure):
        finish = True
        window.blit(win_text, (200,200))

    display.update()
    clock.tick(FPS)