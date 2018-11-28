import pygame
from ship import Ship
from projectile import Projectile, ProjectileList, ProjectileEnemiesList
from configs import gameConfigs

class Player(Ship):
    lifes = 10
    def __init__(self, screen):
        y = gameConfigs["height"] - self.height - 10
        x = gameConfigs["width"] // 2 - self.width // 2
        image = pygame.image.load("assets/images/player-ship.png")
        super().__init__(screen, (x, y), image)

    def check_dead(self):
        for projectile in ProjectileEnemiesList.projectiles:
            isInY = projectile.y > self.y and projectile.y < self.y + self.height - 5
            isInX = projectile.x > self.x and projectile.x < self.x + self.width
            if isInX and isInY:
                self.lifes -= 1


    def update(self):
        self.gunLastShot += 1

        image = pygame.image.load("assets/images/player-ship.png")
        imageMoveLeft = pygame.image.load("assets/images/player-ship-left.png")
        imageMoveRight = pygame.image.load("assets/images/player-ship-right.png")

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            super().__init__(self.screen, (self.x, self.y), imageMoveLeft)

        if keys[pygame.K_RIGHT]:
            self.x += self.speed
            super().__init__(self.screen, (self.x, self.y), imageMoveRight)

        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            super().__init__(self.screen, (self.x, self.y), image)

        if keys[pygame.K_SPACE] and self.gunLastShot > self.gunDelay:
            self.gunLastShot = 0
            projectile = Projectile(self.screen, (self.x + self.width // 2, self.y), Projectile.UP)
            ProjectileList.projectiles.append(projectile)

        self.check_dead()

        super().update()