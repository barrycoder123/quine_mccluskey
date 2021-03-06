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

def min_dist(arr):
    arr = sorted(arr)
    diff = 10**20 # big number
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if abs(arr[i] - arr[j]) < diff:
                diff = abs(arr[i] - arr[j])
    return diff


def larger_group_matching(G1, G2):
    # idea: using the arrays from group_matching function
    # check if the last elements match
    match_arrays = []
    ans = []
    for i in range(len(G1)):
        for j in range(len(G2)):
            if G1[i][2] == G2[j][2]: # the last array element matches so can match them
                # idea just concatenate them first take the first two of each
                ans = [ G1[i][0:2] + G2[j][0:2] ]
                match_arrays.append(ans[0])
    # remove redundancies from list (because im lazy)
    # sort all arrays in match arrays
    for i in match_arrays:
        for j in match_arrays:
            if set(i) == set(j):
                match_arrays.remove(i);

    for i in match_arrays:
        i.append(min_dist(i))
        i.append(abs(i[0] - i[1]))

    return match_arrays

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

    print("\n")
    #TODO checking which 0 cubes to cross out
    #idea: put all the 0-cubes in a dictionary and check them off (true/false)
    zero_cubes_dict = {key: False for key in minterms + dont_cares}
    print(zero_cubes_dict);
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
    match_arrays4 = group_matching(list_to_binary(three_ones),
            list_to_binary(four_ones))
    print(match_arrays4)

    print("\n");
    print("----------------------------------------------------------------")
    print("these are the zero cubes that have been checked off")
    print("----------------------------------------------------------------")
    for i in zero_cubes_dict:
        if i in match_arrays or match_arrays2 or match_arrays3 or match_arrays4:
            zero_cubes_dict[i] = True;

    print(zero_cubes_dict)
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
    print("----------------------------------------------------------------")
    print("2-cubes groups 2* and 3*")
    print("----------------------------------------------------------------")
    match_arrays7 = larger_group_matching(match_arrays3, match_arrays4)
    print(match_arrays7)
    one_cubes_dict = {}
    for i in match_arrays, match_arrays2, match_arrays3, match_arrays4:
        one_cubes_dict = {tuple(i) : False for i in  match_arrays +
                match_arrays2 + match_arrays3 + match_arrays4}
    print("----------------------------------------------------------------")
    print("these are the one cubes that have been checked off")
    print("----------------------------------------------------------------")
    for i in one_cubes_dict:
        if i in match_arrays5 or match_arrays6 or match_arrays7:
            one_cubes_dict[i] = True;
    print(one_cubes_dict);

    # prime implicant list
    one_cube_counter = 0
    pi = []
    for i in zero_cubes_dict:
        if zero_cubes_dict[i] == False:
            pi.append(i)
    for i in one_cubes_dict:
        if one_cubes_dict[i] == False:
            pi.append(i)
            one_cube_counter +=1
    for i in match_arrays5, match_arrays6, match_arrays7:
        if i != []:
            pi.append(i)
    pi_dict = {}
    reshape = []
    for i in pi:
        for j in range(len(i)):
            reshape.append(i[j])

    for i in reshape:
        if len(i) == 3:
            del(i[-1])
        if len(i) == 6:
            del(i[-1])
            del(i[-1])
    for i in range(len(reshape)):
        pi_dict[i] = reshape[i]
    print("----------------------------------------------------------------")
    print("these are the prime implicants")
    print("----------------------------------------------------------------")
    # print(pi)
    print(pi_dict)
    print("----------------------------------------------------------------")
    print("creating the PI table initialize all values to False" , end=" ")
    print("size = (number of prime implicants) x (number of minterms)")
    print("create an array of final checks")
    print("----------------------------------------------------------------")
    rows = len(pi_dict)
    cols = len(set(minterms))
    pi_table = []
    for i in range(rows):
        pi_table.append([])
        for j in range(cols):
            pi_table[i].append(False)

    final_checks = [False] * cols
    # add the checks
    # for one-cubes the check is a bit different
    # wanna check until the last two arr elements
    for j in range(rows):
        check_arr = pi_dict[j]
        for i in range(len(minterms)):
            if minterms[i] in check_arr:
                pi_table[j][i] = True

    print("----------------------------------------------------------------")
    print("this is the PI table")
    print("----------------------------------------------------------------")
    print(pi_table)

    minterm_list = minterms.copy();
    unused = list(pi_dict.values()) # list of pis
    for i in range(cols):
        minterm_list[i] = [minterm_list[i], 0] # each minterm has been used 0 times
    for i in range(cols):
        for j in range(len(unused)):
            for k in range(len(unused[j])):
                if minterm_list[i][0] == unused[j][k]:
                    minterm_list[i][1] +=1; # update counter
                    minterm_list[i].append(j) # but which pi did use - this answers that
    for i in range(len(minterm_list)):
        # check if only used once add true flag
        if minterm_list[i][1] == 1:
            unused[minterm_list[i][2]].append(True)

    print("----------------------------------------------------------------")
    print("these are the essential prime implicants")
    print("----------------------------------------------------------------")
    essential_pi = []
    for j in unused:
        if True in j:
            del j[-1]
            essential_pi.append(j)
        
    # now write the binary of the essential PIs
    for i in essential_pi:
        for j in range(len(i)):
            i[j] = to_binary(i[j])
    
    # figure out the placements of the dont cares
    misses_dict = []
    for i in essential_pi:
        # compare to the first one"
        cmpr = i[0]
        idx_miss = []
        for j in range(1, len(i) - 1):
            for k in range(4):
                if i[j][k] != cmpr[k]:
                    idx_miss.append(k)
        misses_dict.append(idx_miss)
    binary = essential_pi.copy()
    sop =[]
    newsop = []
    for i in range(len(binary)):
        for j in range(len(binary[i])-1): 
            for k in range(4):
                sop.append('0')
                sop[k] = binary[i][0][k]
                if ((binary[i][0][k] != binary[i][j+1][k])):
                    sop[k] = 'X'
        del sop[4:]            
        newsop.append( ''.join([str(x) for x in sop]) )
        sop = []
    print("Turning into Sum Of Products with don't cares", newsop)
    


    alphabet = ["A", "B", "C", "D"]
    ans_list = [ ]
    for i in range(len(newsop)):
        if newsop[i] != "X":
            res = [ ]
            for j in range(4):
                if newsop[i][j] == "0":
                    res.append("~" + alphabet[j])
                if newsop[i][j] == "1":
                    res.append(alphabet[j])
            ans_list.append(res)
    
    answers = []
    for i in ans_list:
        answers.append(''.join(i))

    solution = ""
    for i in range(len(answers)):
        solution += answers[i] + " + "
    print("the sum of products answer is f = ", solution[:-2])
    #convert to pos
    pos_ans = []
    for i in ans_list:
        to_add1, to_add2 = "", ""
        lst = []
        for j in range(len(i)):
            if  "~" in i[j]:
                to_add1 = i[j][1:] + " + "
                lst.append(to_add1)
            else:
                to_add2 = " ~" + i[j] + " + "
                lst.append(to_add2)
            pos_ans.append(lst)

    for i in pos_ans:
        for j in pos_ans:
            if set(i) == set(j):
                pos_ans.remove(j)

    pos_answers = []
    for i in pos_ans:
        pos_answers.append(''.join(i))
    pos_solution = ""
    for i in range(len(pos_answers)):
        pos_solution += "(" + pos_answers[i][:-2] + ")"
    print("the product of sums answers is F = ", pos_solution)
    print("\n");

if __name__ == "__main__":
    minterms = [1, 5, 7, 8, 9, 13, 15]
    dont_cares = [4, 12, 14] 

    cubes(minterms, dont_cares)






