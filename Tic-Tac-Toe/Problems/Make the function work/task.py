def closest_mod_5(x):
    if x % 5 == 0:
        return x
    while x % 5 != 0:
        x += 1
    return x
