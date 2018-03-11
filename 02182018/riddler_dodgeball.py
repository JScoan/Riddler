import math
import random
import pandas as pd

# Consider another truel one where the three combatants
# are equally fast but unequally accurate. Name them Abbott,
#  Bob and Costello. Each has an accuracy of a, b and c,
# respectively. That is, if Abbott aims at something, he hits
#  it with probability a, Bob with probability b and Costello
# with probability c. The abilities of each player are known
# by the others.
#
# Lets say Abbott is a perfect shot: a = 1. Again, suppose the
#  players follow an optimal strategy. Which player, for every
#  possible combination of Bob and Costellos abilities (b and c),
# is favored to survive this truel? (You are welcome to submit your
#  answer as a diagram, if youd like.)

class combatant:
    