# for each number, turn it into a list
# check each list against criteria

in_order = []

print(f"starting count: {len(range(156218,652527))}")

for number in range(156218, 652527):
    # print(number)
    res = [int(x) for x in str(number)]
    if len(res) == len(set(res)):
        continue
    if all(res[i] <= res[i+1] for i in range(len(res)-1)):
        # add to list of things that are in order
        in_order.append(res)
        # print(res)

print(f"ending count:{len(in_order)}")
