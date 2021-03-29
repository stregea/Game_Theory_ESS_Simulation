from Animal import Animal


class Dove(Animal):
    def __init__(self, animal_id: int):
        super(Dove, self).__init__(animal_id)
        self.animal_type = "Dove"
