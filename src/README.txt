Note: This was written in python 3.9

To run: python3 simulation.py popSize [percentHawks] [resourceAmt] [costHawk_Hawk]

This project was written in python, and the reason I chose python was mostly due to preference over Java.

From what I can observe from the simulations, if there are more doves in the total population than hawks, more hawks
will end up surviving the simulation, otherwise the simulation will come to an end with all hawks dying, or one remains.
This shows that in order for an ecosystem to survive and thrive, we need to have multiple species, rather than one massive population
of one type of animal.
In this particular simulation, an ESS occurs during which two animals are selected. The simulation then checks to see if the matching is
Dove/Dove, Dove/Hawk, or Hawk/Hawk and handles the distribution of the resources dependent upon the match up.

What I've learned in relation to ESS is that it allows for the simulating of survival of the fittest. How this relates to Game Theory/Intelligent Systems
is largely due to it being a subset of the Nash Equilibrium. So, depending upon the situation, an intelligent system will have to make a decision upon the Nash Equilibrium,
or in this case an ESS that will simulate which individual survives and which doesn't.