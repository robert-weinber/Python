class MyClass:
    n_objects = 0

    def __new__(cls):
        if cls.n_objects < 5:
            instance = object.__new__(cls)
            cls.n_objects += 1
            return instance

    def __str__(self):
        return "An object of MyClass"
