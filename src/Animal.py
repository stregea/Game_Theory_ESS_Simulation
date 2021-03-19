class Animal:

    def __init__(self, animal_id: int):
        self.animal_id = animal_id
        self.animal_type = None
        self.resource_amount = 0

    def add_resource(self, resource):
        self.resource_amount += resource

    def remove_resource(self, resource):
        self.resource_amount -= resource

    def die(self):
        self.animal_type = "DEAD"

    def is_dead(self):
        return self.resource_amount < 0 and self.animal_type == "DEAD"

    def is_alive(self):
        return self.resource_amount >= 0 and self.animal_type != "DEAD"

    def is_dove(self):
        return self.animal_type == "Dove"

    def is_hawk(self):
        return self.animal_type == "Hawk"

    def __str__(self):
        return self.animal_type

    def __eq__(self, other):
        return self.animal_type == other.animal_type
