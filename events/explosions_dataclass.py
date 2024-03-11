import random
import math
from dataclasses import dataclass, field

DRAG = 0.8  # how much a particle slows down by each second

MAX_AGE = 3  # the time in seconds for which a particle is displayed

@dataclass()
class Particle:
    x: float
    y: float
    vx: float
    vy: float
    age: int = 0

    def update_data(self, delay, drag=0.8):
        drag = drag ** delay
        self.vx *= drag
        self.vy *= drag

        self.x += self.vx * delay
        self.y += self.vy * delay

        self.age += delay

    def is_alive(self, max_age=3):
        self.age <= max_age

@dataclass
class Explosion:
    x: float
    y: float
    speed: int = 300
    particles: list[Particle] = field(init=False, repr=False, compare=False)

    def __post_init__(self):
        self.particles = []
        self._explode()

    def _explode(self):
        for _ in range(100):
            angle = random.uniform(0, 2 * math.pi)
            radius = random.uniform(0, 1) ** 0.5

            # convert angle and distance from the explosion point into x and y velocity for the particle
            vx = self.speed * radius * math.sin(angle)
            vy = self.speed * radius * math.cos(angle)

            # add the particle's position, velocity and age to the array
            self.particles.append(Particle(self.x, self.y, vx, vy))
