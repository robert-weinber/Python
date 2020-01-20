class Sphere:
    pi = 3.14

    def __init__(self, r):
        self.r = r
        self.v = (4 / 3) * self.pi * pow(int(r), 3)


sp = Sphere(input())
print(round(sp.v, 2))
