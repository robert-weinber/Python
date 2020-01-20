class Puppy:
    n_puppies = 0

    def __new__(cls):
        if cls.n_puppies < 10:
            instance = object.__new__(cls)
            cls.n_puppies += 1
            return instance
