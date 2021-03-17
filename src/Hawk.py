from Animal import Animal


class Hawk(Animal):
    hawk_counter = 0

    def __init__(self, animal_id: int):
        # super(Dove, self).__init__(animal_id, animal_type)
        super(Hawk, self).__init__(animal_id)
        self.animal_type = "Hawk"
        self.hawk_counter += 1

