class Animal:

    def __init__(self, animal_id: int):
        self.animal_id = animal_id
        self.animal_type = None
        self.resource_amount = 0

    def add_resource(self, resource):
        """
        Add a resource to the animals current resource count.
        :param resource: The number of resources to add.
        """
        self.resource_amount += resource

    def remove_resource(self, resource):
        """
        Remove a resource from an animals current resource count.
        :param resource: The number of resources to remove.
        """
        self.resource_amount -= resource

    def die(self):
        """
        'Kill' an animal.
        """
        self.animal_type = "DEAD"

    def is_dead(self):
        """
        Determine if the current animal is dead.
        :return: True if the recourses are less than 0 and if 'DEAD'. False otherwise.
        """
        return self.resource_amount < 0 and self.animal_type == "DEAD"

    def is_alive(self):
        """
        Determine if the current animal is alive.
        :return: True if the recourses are greater than 0 and if not 'DEAD'. False otherwise.
        """
        return self.resource_amount >= 0 and self.animal_type != "DEAD"

    def is_dove(self):
        """
        Determine if the current type of animal is a dove.
        :return: True if the type is 'Dove'. False otherwise.
        """
        return self.animal_type == "Dove"

    def is_hawk(self):
        """
        Determine if the current type of animal is a hawk.
        :return: True if the type is 'Hawk'. False otherwise.
        """
        return self.animal_type == "Hawk"

    def __str__(self):
        """
        Return the toString representation of the current animal.
        :return: The current animal type.
        """
        return self.animal_type

    def __eq__(self, other):
        """
        Determine if the two animals are equal.
        :param other: The other animal to compare to.
        :return: True if the animals share the same type. False otherwise.
        """
        return self.animal_type == other.animal_type
