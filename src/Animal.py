class Animal:

    def __init__(self, animal_id: int):
        self.animal_id = animal_id
        self.animal_type = None
        self.resource_amount = 0

    def is_alive(self):
        return self.resource_amount >= 0

    def add_resource(self, resource):
        self.resource_amount += resource

    def remove_resource(self, resource):
        self.resource_amount -= resource

    def __str__(self):
        return self.animal_type
