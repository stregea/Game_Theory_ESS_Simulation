import argparse
import math
from Hawk import Hawk
from Dove import Dove

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
                        default=20,)
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

    individuals = []
    for i in range(0, population_size):

        roll = (population_size - i) % 2

        # if hawks remaining and even roll create hawk
        if number_of_hawks > 0 and roll == 0:
            individuals.append(Hawk(i))
            number_of_hawks -= 1
        else:
            individuals.append(Dove(i))

    for animal in individuals:
        print(animal)


if __name__ == '__main__':
    main()
