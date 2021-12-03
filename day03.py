# Advent of Code, day 3

def mcb(l, bit, mlb, tiebreaker = "1"):
    """
       l = list of bits, e.g. ["00100", "11110", "10110"]
       bit = index of the bit to consider, integer
       mlb = most ("1") or least ("0") bit 
       tiebreaker = if there's an even split, default to this value.

       returns the most common occurrencs, subject to tiebreakers, 
       "0" or "1" as a string
    """
    s = 0
    exact_split = len(l) / 2
    for i in l:
        if i[bit] == "1":
            s += 1
    if s == exact_split:
        return tiebreaker
    elif s > exact_split:
        return mlb
    else:
        return str(1 - int(mlb))

def reduce_list(s,bit,value):
    #
    # s = list to consider
    # bit = bit in the field to consider
    # value to match
    # 
    # returns a list 
    c = list()
    for i in s:
        if i[bit] == value:
            c.append(i)
    return(c)

with open("day03.txt","r") as fp:
    d = fp.read()
l = d.split()
bitlength = len(l[0])

# Problem 1
gamma_rate = ""
epsilon_rate = ""

for bits in range(0, bitlength):
    r = mcb(l, bits, "1")
    if r == "1":
        gamma_rate = gamma_rate + "1"
        epsilon_rate = epsilon_rate + "0"
    else:
        gamma_rate = gamma_rate + "0"
        epsilon_rate = epsilon_rate + "1"

power_consumption = int(gamma_rate,2) * int(epsilon_rate,2)
print(power_consumption)

# Problem 2

co2 = list(l)
oxygen = list(l)

for bits in range(0, bitlength):
    if len(oxygen) == 1:
        break
    lookfor = mcb(oxygen,bits,"1")
    oxygen = list(reduce_list(oxygen,bits,lookfor))

for bits in range(0, bitlength):
    if len(co2) == 1:
        break
    lookfor = mcb(co2, bits, "0", tiebreaker = "0")
    co2 = list(reduce_list(co2,bits,lookfor))

oxygen_gen = int(oxygen[0],2)
co2_gen = int(co2[0],2)
print( oxygen_gen * co2_gen )
