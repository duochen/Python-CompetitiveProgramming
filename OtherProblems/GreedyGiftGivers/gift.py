"""
ID: duochen2
LANG: PYTHON3
TASK: gift1
"""

import math
from collections import OrderedDict

friends = OrderedDict()
with open("gift1.in", "r") as fin:
    # Read how many people
    NP = int(fin.readline().strip())   
    # Read names and put them in friends dictionary, each person has $0 at the beginning
    for i in range(NP):                
        name = fin.readline().strip()
        friends[name] = 0

    # For each person
    for i in range(NP):
        # Read the name of the person
        name = fin.readline().strip()
        # Read money and the number of friends will receive the gifts
        money, people = map(lambda x: int(x), fin.readline().strip().split())
        # Deduct the money from this person
        friends[name] -= money

        # For each friend
        for j in range(people):
            # Read friend's name
            friend = fin.readline().strip()
            # Split the money to each friend            
            friends[friend] += money // people

        # The rest of money will go back to the owner
        if money != 0:
            friends[name] += money % people

with open("gift1.out", "w") as fout:
    for item in friends.items():
        fout.write("%s %d\n" % item)