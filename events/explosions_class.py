import random
import math

DRAG = 0.8  # how much a particle slows down by each second

MAX_AGE = 3  # the time in seconds for which a particle is displayed


class Particle:
    __slots__ = ("x", "y", "vx", "vy", "age")

    def __init__(self, x: float, y: float, vx: float, vy: float, age: float = 0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.age = age

    def __str__(self):
        return f"Particle x={self.x} y={self.y} - vx={self.vx}, vy={self.vy} - age={self.age}"

    def __repr__(self):
        return f"Particle({self.x}, {self.y}, {self.vx}, {self.vy}, {self.age})"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.x, self.y, self.vx, self.vy, self.age) \
            == (other.x, other.y, other.vx, other.vy, other.age)

    def update_data(self, delay):
        drag = DRAG ** delay
        self.vx *= drag
        self.vy *= drag

        self.x += self.vx * delay
        self.y += self.vy * delay

        self.age += delay

    def is_alive(self):
        return self.age <= MAX_AGE


class Explosion:
    def __init__(self, x: float, y: float, speed: int = 300):
        self.x = x
        self.y = y
        self.speed = speed

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
