import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else: 
            random_num = random.uniform(20, 50)
            asteroid_one = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid_two = Asteroid(self.position.x, self.position.y, self.radius)
            
            asteroid_one.velocity = self.velocity.rotate(random_num) * 1.2
            asteroid_two.velocity = self.velocity.rotate(-random_num) * 1.2
            
            asteroid_one.radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_two.radius = self.radius - ASTEROID_MIN_RADIUS