'''
Author: Ibrahima Barry
date:   04/18/2022

Description: 
Write a program to implement the Quine McCluskey Algorithm for boolean algebra
that generates the minimized 2-level sum of products (SOP) and product of sums
(POS) expressions for all single-output boolean functions of up to 10 literals. 

Sources:
'''
def ham_dist(s1, s2):
    try:
        dist = 0;
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                dist += 1
        return dist
    except IndexError:
        print("make sure the two strings are of the same size");

def to_binary(num):
    binary_num = bin(num).replace("0b", "")
    while len(binary_num) < 4:
        binary_num = "0" + binary_num
    return binary_num

def is_pow2(num):
    return (num and (not (num & (num - 1))))

def group_matching(G1, G2):
    # create pairs across adjacent groups if ham(G1_i, G2_j) is a power of 2
    match_arrays = [] 
    for i in range(len(G1)):
        for j in range(len(G2)):
            dist = ham_dist(str(G1[i]), str(G2[j]))
            if is_pow2(dist): # can match them
                # create array to hold data
                int1 = int(G1[i], 2)
                int2 = int(G2[j], 2)
                diff = abs(int1 - int2)
                match_arrays.append([int1, int2, diff])
    return match_arrays

def larger_group_matching(G1, G2):
    # idea: using the arrays from group_matching function
    # check if the last elements match
    match_arrays = []
    for i in range(len(G1)):
        for j in range(len(G2)):
            if G1[i][2] == G2[j][2]: # the last array element matches so can match them
                # idea just concatenate them first take the first two of each
                # and concatenate the min and max differences between the
                # numbers
                match_arrays.append([ G1[i][0:2] + G2[j][0:2] ])
    # remove redundancies from list (because im lazy)
    match_arrays_x = []
    # sort all arrays in match arrays
    for i in match_arrays:
        i[0] = sorted(i[0]);
        if i[0] not in match_arrays_x:
            match_arrays_x.append(i[0])
    return match_arrays_x

def list_to_binary(array):
    bin_array = [ ]
    for i in range(len(array)):
        binary = bin(array[i]).replace("0b", "")
        while len(binary) < 4:
            binary = "0" + binary
        bin_array.append(binary)
    return bin_array

def cubes(minterms, dont_cares):
    print("number of 1s", "||\t\t", "0 cubes")
    # decimal to binary conversion
    bin_minterms = list_to_binary(minterms);
    bin_dc = list_to_binary(dont_cares);

    zero_ones = [ ]
    one_ones = [ ]
    two_ones = [ ]
    three_ones = [ ]
    four_ones = [ ]

    print("0", "\t\t\t", end= " ")
    for i in range(len(bin_minterms)):
        if bin_minterms[i].count('1') == 0:
            zero_ones.append(minterms[i])
            print(minterms[i], end=" ");
    for i in range(len(bin_dc)):
        if bin_dc[i].count('1') == 0:
            zero_ones.append(dont_cares[i])
            print(dont_cares[i], end=" ");
    print("\n")
    print("1", "\t\t\t", end= " ")
    for i in range(len(bin_minterms)):
        if bin_minterms[i].count('1') == 1:
            one_ones.append(minterms[i])
            print(minterms[i], end=" ");
    for i in range(len(bin_dc)):
        if bin_dc[i].count('1') == 1:
            one_ones.append(dont_cares[i])
            print(dont_cares[i], end=" ");   
    print("\n")
    print("2", "\t\t\t", end= " ")
    for i in range(len(bin_minterms)):
        if bin_minterms[i].count('1') == 2:
            two_ones.append(minterms[i])
            print(minterms[i], end=" ");
    for i in range(len(bin_dc)):
        if bin_dc[i].count('1') == 2:
            two_ones.append(dont_cares[i])
            print(dont_cares[i], end=" ");   
    print("\n")
    print("3", "\t\t\t", end= " ")
    for i in range(len(bin_minterms)):
        if bin_minterms[i].count('1') == 3:
            three_ones.append(minterms[i])
            print(minterms[i], end=" ");
    for i in range(len(bin_dc)):
        if bin_dc[i].count('1') == 3:
            three_ones.append(dont_cares[i])
            print(dont_cares[i], end=" ");   
    print("\n")
    print("4", "\t\t\t", end= " ")
    for i in range(len(bin_minterms)):
        if bin_minterms[i].count('1') == 4:
            four_ones.append(minterms[i])
            print(minterms[i], end=" ");
    for i in range(len(bin_dc)):
        if bin_dc[i].count('1') == 4:
            four_ones.append(dont_cares[i])
            print(dont_cares[i], end=" ");
    #TODO checking which 0 cubes to cross out
    print("\n")
    print("----------------------------------------------------------------")
    print("1-cubes groups 0 and 1")
    print("----------------------------------------------------------------")
    match_arrays = group_matching(list_to_binary(zero_ones),
            list_to_binary(one_ones))
    print(match_arrays)
    print("----------------------------------------------------------------")
    print("1-cubes groups 1 and 2")
    print("----------------------------------------------------------------")
    match_arrays2 = group_matching(list_to_binary(one_ones),
            list_to_binary(two_ones))
    print(match_arrays2)
    print("----------------------------------------------------------------")
    print("1-cubes groups 2 and 3")
    print("----------------------------------------------------------------")
    match_arrays3 = group_matching(list_to_binary(two_ones),
            list_to_binary(three_ones))
    print(match_arrays3)
    print("----------------------------------------------------------------")
    print("1-cubes groups 3 and 4")
    print("----------------------------------------------------------------")
    print(three_ones, four_ones);
    match_arrays4 = group_matching(list_to_binary(three_ones),
            list_to_binary(four_ones))
    print(match_arrays4)
    #TODO checking which 1 cubes to cross out
    print("\n")
    print("----------------------------------------------------------------")
    print("2-cubes groups 0* and 1*")
    print("----------------------------------------------------------------")
    match_arrays5 = larger_group_matching(match_arrays, match_arrays2)
    print(match_arrays5)
    print("----------------------------------------------------------------")
    print("2-cubes groups 1* and 2*")
    print("----------------------------------------------------------------")
    match_arrays6 = larger_group_matching(match_arrays2, match_arrays3)
    print(match_arrays6)

if __name__ == "__main__":
    minterms = [1, 5, 7, 8, 9, 13, 15]
    dont_cares = [4, 12, 14] 

    cubes(minterms, dont_cares)






