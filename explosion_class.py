import random

import pgzrun

from events import explosions_dataclass as ev_explosions

# the size of the screen
WIDTH = 800
HEIGHT = 600

PARTICLE_COLOR = 255, 230, 128  # the colour of each particle in R, G, B values

explosions = []  # an array to hold the details of the explosion particles on the screen


def draw():
    """
    This function redraws the screen by plotting each particle in the array
    """

    # clear the screen
    screen.clear()
    
    # loop through all the particles in the array
    for explosion in explosions:
        for particle in explosion.particles:

            # for each particle in the array, plot its position on the screen
            screen.surface.set_at((int(particle.x), int(particle.y)), PARTICLE_COLOR)


def update(dt):
    for explosion in explosions:
        for particle in explosion.particles:
            particle.update_data(dt)

def explode_random():
    """
    This function creates an explosion at a random location on the screen
    """

    # select a random position on the screen
    x = random.randrange(WIDTH)
    y = random.randrange(HEIGHT)
    
    # call the explosion function for that position
    explosions.append(ev_explosions.Explosion(x, y))

# call the random explosion function every 1.5 seconds
clock.schedule_interval(explode_random, 1.5)

pgzrun.go()