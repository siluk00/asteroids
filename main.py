# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroidfield = AsteroidField()


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 return
            
        for thing in updatable:    
            thing.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game Over!")
                return
            for shot in shots:
                if asteroid.collide(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill((0,0,0))

        
        for thing in drawable:
            thing.draw(screen)
        

        pygame.display.flip()
        dt = clock.tick(60) /1000

        if player.timer <= 0:
            player.timer = 0
        else:
            player.timer -= dt

if __name__ == "__main__":
    main()