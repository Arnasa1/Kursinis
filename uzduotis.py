import pygame
import sys
import random

WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 40
ENEMY_SIZE = 50
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0,128,0,0)
BLUE = (0, 0, 255)

pygame.init()

# Bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, owner):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 8
        self.direction = direction
        self.owner = owner

    def update(self):
        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]

        if self.rect.bottom < 0 or self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

# Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)  # Start at the center
        self.speed = 8
        self.lives = 3
        self.score = 0
        self.last_score_bullet_speed_increase = 0
        self.extra_life_given = False
        self.bullets = pygame.sprite.Group()
        self.last_direction = pygame.math.Vector2(0, -1)  # Default direction (up)

    def update(self, *args, **kwargs):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.last_direction = pygame.math.Vector2(-1, 0)
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.last_direction = pygame.math.Vector2(1, 0)
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.last_direction = pygame.math.Vector2(0, -1)
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.last_direction = pygame.math.Vector2(0, 1)
            
        self.update_score_logic()

        # Boundaries
        self.rect.x = max(0, min(self.rect.x, WIDTH - PLAYER_SIZE))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - PLAYER_SIZE))

        
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery, (self.last_direction.x, self.last_direction.y), "player")
        self.bullets.speed = 10
        self.bullets.add(bullet)
        all_sprites.add(bullet)
    def update_score_logic(self):
       
        if self.score % 200 == 0 and self.score > self.last_score_bullet_speed_increase:
            self.increase_enemy_bullet_speed()
            self.last_score_bullet_speed_increase = self.score

        if self.score >= 500 and not self.extra_life_given:
            self.give_extra_life()
            self.extra_life_given = True

    def increase_enemy_bullet_speed(self):
        for enemy_bullet in enemy_bullets:
            enemy_bullet.speed += 0.5

    def give_extra_life(self):
        self.lives += 1

# Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((ENEMY_SIZE, ENEMY_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - ENEMY_SIZE)
        self.rect.y = random.randint(0, HEIGHT - ENEMY_SIZE)
        self.speed = 2
        self.shoot_delay = random.randint(2400, 3000)  
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.shoot()
            self.last_shot = now
            self.shoot_delay = random.randint(1500, 1801)  

    def shoot(self):
        player_pos = player.rect.center
        enemy_pos = self.rect.center

        # Calculate direction vector towards the player
        direction = pygame.math.Vector2(player_pos[0] - enemy_pos[0], player_pos[1] - enemy_pos[1]).normalize()

        
        bullet = Bullet(self.rect.centerx, self.rect.centery, (direction.x, direction.y), "enemy")
        bullet.speed = 5
        enemy_bullets.add(bullet)
        all_sprites.add(bullet)

# SpecialEnemy
class SpecialEnemy(pygame.sprite.Sprite):
    def __init__(self, target):
        super().__init__()
        self.image = pygame.Surface((ENEMY_SIZE, ENEMY_SIZE))
        self.image.fill(BLUE) #Melyna 
        self.rect = self.image.get_rect()
        self.speed = 9
        self.target = target

    def update(self):
        direction = pygame.math.Vector2(self.target.rect.centerx - self.rect.centerx,
                                        self.target.rect.centery - self.rect.centery).normalize()
        self.rect.x += self.speed * direction.x
        self.rect.y += self.speed * direction.y


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Berzerk")
clock = pygame.time.Clock()

# Sprite Groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for _ in range(4):
    enemy = Enemy()
    enemies.add(enemy)
    all_sprites.add(enemy)

special_enemy = None
special_enemy_spawned = False  


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    all_sprites.update()

    if player.score % 300 == 0:
        RED = (random.randint(0, 255), random.randint(0, 128), random.randint(0, 255))\
        

    #collisions between player bullets and enemies
    hits = pygame.sprite.groupcollide(enemies, player.bullets, True, True)
    for enemy in hits:
        player.score += 20

    #collisions between enemies and player
    hits = pygame.sprite.spritecollide(player, enemy_bullets, True)
    if hits:
        player.lives -= 1
        if player.lives == 0:
            running = False  # Game over

    hits = pygame.sprite.spritecollide(player, enemies, True)
    if hits:
        player.lives -= 1
        if player.lives == 0:
            running = False  # Game over
    
    if not enemies and not special_enemy_spawned:
        # Spawn a special enemy
        special_enemy = SpecialEnemy(player)
        all_sprites.add(special_enemy)
        enemies.add(special_enemy)
        special_enemy_spawned = True

    elif not enemies and special_enemy_spawned:
        for _ in range(4):
                enemy = Enemy()
                enemies.add(enemy)
                all_sprites.add(enemy)
                special_enemy_spawned = False

    #collisions between special enemy and player bullets
    if special_enemy is not None:
        hits = pygame.sprite.spritecollide(special_enemy, player.bullets, True)
        if hits: 
            player.score += 20
            special_enemy.kill()
            special_enemy = None
            pygame.time.wait(60)

    if special_enemy is not None:
          if special_enemy.rect.colliderect(player.rect):
            player.lives -= 1
            special_enemy.kill()
            special_enemy = None
            pygame.time.wait(30)
            if player.lives <= 0:
                running = False  # Game over
        
    # Drawing
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    player.bullets.draw(screen)  # Draw player bullets

    font = pygame.font.Font(None, 24)
    score_text = font.render(f"Score: {player.score}", True, WHITE)
    lives_text = font.render(f"Lives: {player.lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Game over screen
font = pygame.font.Font(None, 74)
game_over_text = font.render("Game Over", True, WHITE)
score_text = font.render(f"Score: {player.score}", True, WHITE)
screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
screen.blit(score_text, (WIDTH // 2 - 100, HEIGHT // 2 + 50))
pygame.display.flip()

# Wait for a few seconds before quitting
pygame.time.wait(1000)
pygame.quit()
sys.exit()