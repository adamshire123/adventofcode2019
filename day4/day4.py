# for each number, turn it into a list
# check each list against criteria

import re
from collections import Counter
passwords = []

print(f"starting count: {len(range(156218,652527))}")

for number in range(156218, 652527):
    # print(number)
    res = [int(x) for x in str(number)]
    # if there are no duplicates move on
    if len(res) == len(set(res)):
        continue
    # check to see if the list is in order
    if all(res[i] <= res[i+1] for i in range(len(res)-1)):
        # add it to the list of possible passwords 
        histo = dict((x, res.count(x)) for x in res)
        if 2 in histo.values():
            passwords.append(res)
            print(res)


print(f"ending count:{len(passwords)}")
