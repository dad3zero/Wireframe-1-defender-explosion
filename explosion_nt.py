import random
import math
from collections import namedtuple

Particle = namedtuple("Particle", ("x", "y", "vx", "vy", "age"))

# the size of the screen
WIDTH = 800
HEIGHT = 600


DRAG = 0.8  # how much a particle slows down by each second

PARTICLE_COLOR = 255, 230, 178  # the colour of each particle in R, G, B values

MAX_AGE = 3  # the time in seconds for which a particle is displayed

particles = []  # an array to hold the details of the explosion particles on the screen


def explode(x:int, y:int, speed: int  = 300):
    """
    This function creates a new explosion at the specified screen co-ordinates
    """

    particles = []
    age = 0     
    
    # generate 100 particles per explosion
    for _ in range(100):
    
        # for each particle, generate a random angle and distance
        angle = random.uniform (0, 2 * math.pi)
        radius = random.uniform(0, 1) ** 0.5

        # convert angle and distance from the explosion point into x and y velocity for the particle
        vx = speed * radius * math.sin(angle)
        vy = speed * radius * math.cos(angle)
        
        # add the particle's position, velocity and age to the array
        particles.append(Particle(x, y, vx, vy, age))

    return particles


def draw():
    """
    This function redraws the screen by plotting each particle in the array
    """

    # clear the screen
    screen.clear()
    
    # loop through all the particles in the array
    for x, y, *_ in particles:
        
        # for each particle in the array, plot its position on the screen
        screen.surface.set_at((int(x), int(y)), PARTICLE_COLOR)


def update_particle_data(particle: Particle, delay):
    """
    This function updates the array of particles
    """


    drag = DRAG ** delay
    vx = particle.vx * drag
    vy = particle.vy * drag

    x = particle.x + vx * delay
    y = particle.y + vy * delay

    age = particle.age + delay

    return Particle(x, y, vx, vy, age)

def update(particles:list[Particle], dt):
    particles[:] = [update_particle_data(particle, dt)
                    for particle in particles
                    if particle.age + dt <= MAX_AGE]

def explode_random():
    """
    This function creates an explosion at a random location on the screen
    """

    # select a random position on the screen
    x = random.randrange(WIDTH)
    y = random.randrange(HEIGHT)
    
    # call the explosion function for that position
    return explode(x, y)
