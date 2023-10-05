def stage1(input: str):
    list_of_permutations = list(map(int, input.split()))
    amount_of_permutations = list_of_permutations[0]
    list_of_permutations.pop(0)

    list_of_oriented_pairs = list()
    amount_of_oriented_pairs = 0

    for idx, elem1 in enumerate(list_of_permutations):
        for elem2 in list_of_permutations[idx:]:

            if (elem1 < 0 <= elem2 or elem2 < 0 <= elem1) and (abs(elem1) - abs(elem2) == 1 or abs(elem1) - abs(elem2) == -1):


                list_of_oriented_pairs.append((elem1, elem2))
                amount_of_oriented_pairs += 1

    list_of_oriented_pairs.sort(key=lambda x: x[0])
    list_of_oriented_pairs = list(sum(list_of_oriented_pairs, ()))
    list_of_oriented_pairs.insert(0, amount_of_oriented_pairs)

    ret_str = ""
    for elem in list_of_oriented_pairs:
        ret_str += str(elem)
        ret_str += " "
    return ret_str.strip()


def stage2(input: str):
    list_of_permutations = list(map(int, input.split()))
    amount_of_permutations = list_of_permutations[0]
    inversion_pair_with_index = list_of_permutations[-4:]
    list_of_permutations.pop(0)
    list_of_permutations = list_of_permutations[:len(list_of_permutations)-4]
    i, j = inversion_pair_with_index[1], inversion_pair_with_index[3]

    if inversion_pair_with_index[0] + inversion_pair_with_index[2] == 1:

        list_of_permutations[i:j] = list_of_permutations[i:j][::-1]
        list_of_permutations[i:j] = [-x for x in list_of_permutations[i:j]]
    else:
        list_of_permutations[i+1:j+1] = list_of_permutations[i+1:j+1][::-1]
        list_of_permutations[i+1:j+1] = [-x for x in list_of_permutations[i+1:j+1]]

    ret_str = ""
    for elem in list_of_permutations:
        ret_str += str(elem)
        ret_str += " "
    return ret_str.strip()


def stage3(input: str):
    inverted_permutation = stage2(input)
    inverted_permutation_in_list = list(map(int, inverted_permutation.split()))
    inverted_permutation_in_list.insert(0, len(inverted_permutation_in_list))

    ret_str = ""
    for elem in inverted_permutation_in_list:
        ret_str += str(elem)
        ret_str += " "
    ret_str = ret_str.strip()
    oriented_pairs = stage1(ret_str)
    oriented_pairs_in_list = list(map(int, oriented_pairs.split()))
    return oriented_pairs_in_list[0]


def stage4(input: str):

    current_permutation = input
    number_of_inversions = 0
    while True:

        # calculate amount of remaining oriented pairs
        tmp = stage1(current_permutation)
        tmp = list(map(int, tmp.split()))
        amount_of_remaining_oriented_pairs = tmp[0]
        if amount_of_remaining_oriented_pairs == 0:
            break
        else:
            number_of_inversions += 1

        # calculate maximum score for best inversion
        current_permutation_list = list(map(int, current_permutation.split()))
        current_permutation_list.pop(0)
        max_pair = str(tmp[1]) + " " + str(current_permutation_list.index(tmp[1])) + " " + str(tmp[2]) + " " + str(current_permutation_list.index(tmp[2]))
        max_score = stage3(current_permutation + " " + max_pair)

        for i in range(3, len(tmp), 2):
            current_pair = str(tmp[i]) + " " + str(current_permutation_list.index(tmp[i])) + " " + str(tmp[i+1]) + " " + str(current_permutation_list.index(tmp[i+1]))
            new_score = stage3(current_permutation + " " + current_pair)
            if new_score > max_score:
                max_score = new_score
                max_pair = current_pair


        # select pair and invert
        new_permutation = stage2(current_permutation + " " + max_pair)
        new_permutation = list(map(int, new_permutation.split()))
        new_permutation.insert(0, len(new_permutation))
        ret_str = ""
        for elem in new_permutation:
            ret_str += str(elem)
            ret_str += " "
        ret_str = ret_str.strip()
        current_permutation = ret_str

    return number_of_inversions


if __name__ == '__main__':
    print(stage4("193 125 133 134 135 136 -52 -51 -50 -49 -48 -47 -46 -45 66 67 68 69 70 71 -38 -37 -36 -35 -34 -33 -32 -31 -30 -29 -132 -131 -130 -193 -192 -191 -190 -189 -188 -187 -186 -185 -184 -183 -182 -181 -180 -179 -178 -177 -176 -175 -174 -173 -172 -171 -170 -169 -77 -76 -75 -74 -73 -72 18 19 20 21 22 23 24 25 26 27 28 -164 -163 -65 -64 -63 -62 -61 -60 -59 -58 -57 -56 -55 -54 -53 39 40 41 42 43 44 159 160 161 162 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -168 -167 -166 -165 126 127 128 129 86 87 88 89 90 91 92 93 94 95 96 -124 -123 -122 -121 -120 -119 -118 -117 -116 -115 -114 -113 -112 -111 -110 -109 -108 -107 -106 -105 -104 -103 -102 -101 -100 -99 -98 -97 153 154 155 156 157 158 -148 -147 -146 -145 -144 -143 -142 -141 -140 -139 -138 -137 -85 -84 -83 -82 -81 -80 -79 -78 -152 -151 -150 -149"))