from pygame import *
from random import randint

init()

# Game scene
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping Pong Pu")

# Game Sprite Class
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# Main Player Class
class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

# Ball
class Ball(GameSprite):
    direction_x = 1
    direction_y = 1

    def update(self):
        self.rect.x += (self.direction_x * self.speed)
        self.rect.y += (self.direction_y * self.speed)

        if self.rect.y < 5 or self.rect.y > win_height -50:
            self.direction_y *= -1

    def racket_check(self, player):
        if self.rect.colliderect(player.rect):
            self.direction_x *= -1

Player_1 = Player("racket.png", 50, 0, 30, 110, 5)
Player_2 = Player("racket.png", win_width -50,0, 30, 110, 5)

bounce_ball = Ball("we go band4band.webp", win_width / 2, win_height / 2, 50, 50, 2)

bg = transform.scale(image.load("TEST.jpg"), (win_width, win_height))

clock = time.Clock()
is_playing = True
FPS = 60
is_finished = False

# Main Game Loop
while is_playing:
    for e in event.get():
        if e.type == QUIT:
            is_playing = False

    if is_finished == False:
        window.blit(bg, (0, 0))
        Player_1.reset()
        Player_1.update_left()

        Player_2.reset()
        Player_2.update_right()

        bounce_ball.reset()
        bounce_ball.update()
        bounce_ball.racket_check(Player_1)
        bounce_ball.racket_check(Player_2)

    display.update()
    clock.tick(FPS)