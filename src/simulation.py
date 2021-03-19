import argparse
import math
import random
from Animal import Animal
from Hawk import Hawk
from Dove import Dove
from sort import mergesort

def menu():
    return """
===============MENU=============
1 ) Starting Stats
2 ) Display Individuals and Points
3 ) Display Sorted - TODO
4 ) Have 1000 interactions
5 ) Have 10000 interactions
6 ) Have N interactions
7 ) Step through interactions "Stop" to return to menu - TODO
8 ) Quit
================================
"""


def display_starting_stats(population_size: int,
                           hawk_percentage: float,
                           resource_amount: int,
                           hawk_hawk_interaction: int):
    """
    Display the starting statistics for the simulation.
    :param population_size: The total population size.
    :param hawk_percentage: The percentage of Hawks in the population.
    :param resource_amount: The value of each resource that the individuals in the population will be competing for during each encounter.
    :param hawk_hawk_interaction: The loss of resources (or time) in the simulation that penalizes an excessive number of Hawk-Hawk encounters.
    """
    print(f"Population size: {population_size}")
    print(f"Percentage of Hawks: {hawk_percentage}%")
    print(f"Number of Hawks: {math.ceil(population_size * (hawk_percentage / 100))}\n")
    print(f"Percentage of Doves: {100 - hawk_percentage}%")
    print(f"Number of Doves: {population_size - math.ceil(population_size * (hawk_percentage / 100))}\n")
    print(f"Each resource is worth: {resource_amount}")
    print(f"Cost of Hawk-Hawk interaction: {hawk_hawk_interaction}")


def display_individuals_and_points(individuals: list[Animal]):
    """
    Display each of the individuals and their resources.
    :param individuals: The list of individuals.
    """
    living_count = 0
    for i in range(len(individuals)):
        print(f"Individual[{i}]={individuals[i]}:{individuals[i].resource_amount}")
        if individuals[i].is_alive():
            living_count += 1
    print(f"Living: {living_count}")


def display_sorted_individuals(individuals: list[Animal]):
    """
    Display a sorted list of individuals based on their resource amount.
    :param individuals: The list of individuals.
    """
    tmp = mergesort(orig_list=individuals, n=len(individuals))
    for animal in tmp:
        print(f"{animal}:{animal.resource_amount}")


def interaction(individuals: list[Animal], resource_amount: int, cost_of_hawk_hawk: int, number_of_encounters: int):
    """
    Perform an interation between two random individuals.
    :param individuals: The list of individuals.
    :param resource_amount: The value of each resource that the individuals in the population will be competing for during each encounter.
    :param cost_of_hawk_hawk: The loss of resources (or time) in the simulation that penalizes an excessive number of Hawk-Hawk encounters.
    :param number_of_encounters: The total number of encounters occurred.
    """
    animal1 = random.randrange(0, len(individuals))
    animal2 = random.randrange(0, len(individuals))

    # perform search for different index if both are equal
    while animal2 == animal1:
        animal2 = random.randrange(0, len(individuals))

    # if animal 1 is dead break?
    print(f"Encounter: {number_of_encounters}")
    print(f"Individual {animal1}: {individuals[animal1]}")
    print(f"Individual {animal2}: {individuals[animal2]}")

    # if both are doves, split the resource
    if individuals[animal1].is_dove() and individuals[animal2].is_dove():
        # split the resource
        individuals[animal1].add_resource(resource_amount // 2)
        individuals[animal2].add_resource(resource_amount // 2)
        print(f"{individuals[animal1]}/{individuals[animal2]}: {individuals[animal1]}: +{resource_amount // 2}\t{individuals[animal2]}: +{resource_amount // 2}") # this is printed below
        print(f"Individual {animal1}={individuals[animal1].resource_amount}\tIndividual {animal2}={individuals[animal2].resource_amount}")
    # if both are hawks, the first hawk takes the resource, and both bear the hawk-hawk encounter cost
    elif individuals[animal1].is_hawk() and individuals[animal2].is_hawk():
        # edge case for if either are dead?
        individuals[animal1].add_resource(resource_amount)

        # bear the hawk-hawk encounter price
        individuals[animal1].remove_resource(cost_of_hawk_hawk)
        individuals[animal2].remove_resource(cost_of_hawk_hawk)

        char = "+" if resource_amount - cost_of_hawk_hawk >= 0 else ""
        print(f"{individuals[animal1]}/{individuals[animal2]}: {individuals[animal1]}: {char}{resource_amount - cost_of_hawk_hawk}\t{individuals[animal2]}: -{cost_of_hawk_hawk}") # this is printed below
        print(f"Individual {animal1}={individuals[animal1].resource_amount}\tIndividual {animal2}={individuals[animal2].resource_amount}")

        # if recourses are depleted ( < 0 ), the hawk has died
        if individuals[animal1].resource_amount < 0:
            individuals[animal1].die()
            print(f"Hawk {individuals[animal1].animal_id} has died!")
        if individuals[animal2].resource_amount < 0:
            individuals[animal2].die()
            print(f"Hawk {individuals[animal2].animal_id} has died!")

    # if hawk or dove, the hawk takes the resource, and the dove remains unharmed
    elif (individuals[animal1].is_dove() and individuals[animal2].is_hawk()) or (individuals[animal1].is_hawk() and individuals[animal2].is_dove()):

        # if hawk dead, have dove take resource?
        if individuals[animal1].is_hawk() and individuals[animal1].is_alive():
            individuals[animal1].add_resource(resource_amount)
            print(f"{individuals[animal1]}/{individuals[animal2]}: {individuals[animal1]}: +{resource_amount}\t{individuals[animal2]}: +{0}")
            print(f"Individual {animal1}={individuals[animal1].resource_amount}\tIndividual {animal2}={individuals[animal2].resource_amount}")

        elif individuals[animal2].is_hawk() and individuals[animal2].is_alive():
            individuals[animal2].add_resource(resource_amount)
            print(f"{individuals[animal1]}/{individuals[animal2]}: {individuals[animal1]}: +{0}\t{individuals[animal2]}: +{resource_amount}")
            print(f"Individual {animal1}={individuals[animal1].resource_amount}\tIndividual {animal2}={individuals[animal2].resource_amount}")
    print("")


def main():
    # This will serve as the main program
    parser = argparse.ArgumentParser()
    parser.add_argument('popSize',
                        help="The population size of how many individuals you have total in your population.",
                        type=int)
    parser.add_argument('percentHawks',
                        help="The percentage of the population that is employing the Hawk strategy",
                        type=float,  # make a string to handle both int and float values?
                        nargs='?',
                        default=20, )
    parser.add_argument('resourceAmt',
                        help="The value of each resource that the individuals in the population will be competing for "
                             "during each encounter",
                        type=int,
                        nargs='?',
                        default=50)
    parser.add_argument('costHawk_Hawk',
                        help="This will be the loss of resources (or time) in the simulation that penalizes an "
                             "excessive number of Hawk-Hawk encounters",
                        type=int,
                        nargs='?',
                        default=100)
    args = parser.parse_args()

    # assign
    population_size = args.popSize

    # what if negative value?
    percent_hawks = args.percentHawks / 100
    resource_amount = args.resourceAmt
    cost_hawk_hawk = args.costHawk_Hawk

    number_of_hawks = math.ceil(population_size * percent_hawks)
    number_of_doves = population_size - number_of_hawks

    animals = []
    animal_counter = 0

    # while the array isn't fully populated
    # populate the list based on an even or odd roll
    # if the roll is even, create a hawk.
    # if the roll is odd, create a dove
    while animal_counter < population_size:
        roll = (population_size - random.randrange(0, population_size)) % 2
        if number_of_hawks > 0 and roll == 0:
            animals.append(Hawk(animal_counter))
            number_of_hawks -= 1
            animal_counter += 1
        elif number_of_doves > 0 and roll == 1:
            animals.append(Dove(animal_counter))
            number_of_doves -= 1
            animal_counter += 1

    running = True
    encounters = 0
    while running:
        print(menu())
        result = input("> ")
        if result == "1":
            display_starting_stats(args.popSize, args.percentHawks, args.resourceAmt, args.costHawk_Hawk)
        elif result == "2":
            display_individuals_and_points(animals)
        elif result == "3":
            display_sorted_individuals(animals)
        elif result == "4":
            count = 0
            while count < 1000:
                interaction(animals, args.resourceAmt, args.costHawk_Hawk, encounters)
                encounters += 1
                count += 1
        elif result == "5":
            count = 0
            while count < 10000:
                interaction(animals, args.resourceAmt, args.costHawk_Hawk, encounters)
                encounters += 1
                count += 1
        elif result == "6":
            interactions = int(input("Enter number of interactions > "))
            count = 0
            while count < interactions:
                interaction(animals, args.resourceAmt, args.costHawk_Hawk, encounters)
                encounters += 1
                count += 1
        elif result == "7":
            flag = True
            while flag:
                interaction(animals, args.resourceAmt, args.costHawk_Hawk, encounters)
                encounters += 1
                step = input()
                if step.lower() == "stop":
                    flag = False
        elif result == "8":
            running = False
        else:
            print("Invalid command")

    print(menu())


if __name__ == '__main__':
    main()
