from Animal import Animal


class Hawk(Animal):
    def __init__(self, animal_id: int):
        super(Hawk, self).__init__(animal_id)
        self.animal_type = "Hawk"

