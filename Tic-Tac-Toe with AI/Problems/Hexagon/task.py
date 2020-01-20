import math


class Hexagon:
    def __init__(self, t):
        self.t = t

    def get_area(self):
        return round((3 * math.sqrt(3) * pow(self.t, 2)) / 2, 3)
