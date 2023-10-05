def stage1():
    for i in range(1, 6):

        number_of_combs = 0
        filename = "Level1\level1_" + str(i) + ".in"
        f = open(filename, "r")
        for x in f:
            number_of_combs += x.count("O")

        file = open("Level1\level1_" + str(i) + ".out", "w")
        file.write(str(number_of_combs))
        file.close()


def stage2():
    for file_idx in range(1, 6):
        filename = "Level2\level2_" + str(file_idx) + ".in"
        file = open(filename, "r")

        file_out = open("Level2\level2_" + str(file_idx) + ".out", "w")

        amount_of_honeycombs = int(file.readline())
        file.readline()

        for x in range(0, amount_of_honeycombs):

            current_honeycomb = ""
            line = file.readline().strip()
            current_honeycomb += line
            row_length = len(line)
            column_length = 0
            while line != "\n" and line != "":
                line = file.readline()
                current_honeycomb += line.strip()
                column_length += 1

            amount_of_neighboring_cells = 0
            for i in range(0, len(current_honeycomb)):
                if current_honeycomb[i] == "W":

                    if i % row_length == 0:

                        if i < row_length:

                            if current_honeycomb[i + 2] == "O":
                                amount_of_neighboring_cells += 1
                            if current_honeycomb[i + row_length + 1] == "O":
                                amount_of_neighboring_cells += 1

                        elif i >= (column_length - 1) * row_length:

                            if current_honeycomb[i + 2] == "O":
                                amount_of_neighboring_cells += 1
                            if current_honeycomb[i - row_length + 1] == "O":
                                amount_of_neighboring_cells += 1
                        else:

                            if current_honeycomb[i + 2] == "O":
                                amount_of_neighboring_cells += 1
                            if current_honeycomb[i - row_length + 1] == "O":
                                amount_of_neighboring_cells += 1
                            if current_honeycomb[i + row_length + 1] == "O":
                                amount_of_neighboring_cells += 1

                    elif i % row_length == 19:

                        if i < row_length:

                            if current_honeycomb[i - 2] == "O":
                                amount_of_neighboring_cells += 1
                            if current_honeycomb[i + row_length - 1] == "O":
                                amount_of_neighboring_cells += 1

                        elif i >= (column_length - 1) * row_length:

                            if current_honeycomb[i - 2] == "O":
                                amount_of_neighboring_cells += 1
                            if current_honeycomb[i - row_length - 1] == "O":
                                amount_of_neighboring_cells += 1

                        else:

                            if current_honeycomb[i - 2] == "O":
                                amount_of_neighboring_cells += 1
                            if current_honeycomb[i - row_length - 1] == "O":
                                amount_of_neighboring_cells += 1
                            if current_honeycomb[i + row_length - 1] == "O":
                                amount_of_neighboring_cells += 1

                    else:

                        if i < row_length:

                            if current_honeycomb[i - 2] == "O":
                                amount_of_neighboring_cells += 1
                            if current_honeycomb[i + 2] == "O":
                                amount_of_neighboring_cells += 1
                            if current_honeycomb[i + row_length - 1] == "O":
                                amount_of_neighboring_cells += 1
                            if current_honeycomb[i + row_length + 1] == "O":
                                amount_of_neighboring_cells += 1

                        elif i >= (column_length - 1) * row_length:

                            if current_honeycomb[i - 2] == "O":
                                amount_of_neighboring_cells += 1
                            if current_honeycomb[i + 2] == "O":
                                amount_of_neighboring_cells += 1
                            if current_honeycomb[i - row_length - 1] == "O":
                                amount_of_neighboring_cells += 1
                            if current_honeycomb[i - row_length + 1] == "O":
                                amount_of_neighboring_cells += 1

                        else:

                            if current_honeycomb[i - 2] == "O":
                                amount_of_neighboring_cells += 1
                            if current_honeycomb[i + 2] == "O":
                                amount_of_neighboring_cells += 1
                            if current_honeycomb[i - row_length - 1] == "O":
                                amount_of_neighboring_cells += 1
                            if current_honeycomb[i - row_length + 1] == "O":
                                amount_of_neighboring_cells += 1
                            if current_honeycomb[i + row_length - 1] == "O":
                                amount_of_neighboring_cells += 1
                            if current_honeycomb[i + row_length + 1] == "O":
                                amount_of_neighboring_cells += 1

                    break

            file_out.writelines(str(amount_of_neighboring_cells) + "\n")
        file.close()
        file_out.close()


def stage3():
    for file_idx in range(1, 6):
        filename = "Level3\level3_" + str(file_idx) + ".in"
        file = open(filename, "r")

        file_out = open("Level3\level3_" + str(file_idx) + ".out", "w")

        amount_of_honeycombs = int(file.readline())
        file.readline()

        for x in range(0, amount_of_honeycombs):

            print("INDEX CURRENT HONEYCOMB: " + str(x))

            current_honeycomb = ""
            line = file.readline().strip()
            current_honeycomb += line
            row_length = len(line)
            column_length = 1
            while True:
                line = file.readline()
                if line == "\n" or line == "":
                    break
                current_honeycomb += line.strip()
                column_length += 1

            escape_left = True
            escape_right = True
            escape_up_left = True
            escape_up_right = True
            escape_down_left = True
            escape_down_right = True
            for i in range(0, len(current_honeycomb)):
                if current_honeycomb[i] == "W":
                    print("Wasp found at index " + str(i) + "\n")

                    # left
                    current_index = i
                    current_row_position = i % row_length
                    while current_row_position >= 0:
                        if current_honeycomb[current_index] == "X":
                            escape_left = False
                            break
                        current_row_position -= 2
                        current_index -= 2
                    print("Found left: " + str(escape_left) + "\n")

                    # right
                    current_index = i
                    current_row_position = i % row_length
                    while current_row_position <= row_length-1:
                        if current_honeycomb[current_index] == "X":
                            escape_right = False
                            break
                        current_row_position += 2
                        current_index += 2
                    print("Found right: " + str(escape_right) + "\n")

                    # up_left
                    current_index = i
                    current_row_position = i % row_length
                    current_column_position = i // row_length
                    while current_row_position >= 0 and current_column_position >= 0:
                        if current_honeycomb[current_index] == "X":
                            escape_up_left = False
                            break
                        current_row_position -= 1
                        current_column_position -= 1
                        current_index -= (row_length+1)
                    print("Found up_left: " + str(escape_up_left) + "\n")

                    # up_right
                    current_index = i
                    current_row_position = i % row_length
                    current_column_position = i // row_length
                    while current_row_position <= row_length-1 and current_column_position >= 0:
                        if current_honeycomb[current_index] == "X":
                            escape_up_right = False
                            break
                        current_row_position += 1
                        current_column_position -= 1
                        current_index -= (row_length-1)
                    print("Found up_right: " + str(escape_up_right) + "\n")

                    # down_left
                    current_index = i
                    current_row_position = i % row_length
                    current_column_position = i // row_length
                    while current_row_position >= 0 and current_column_position <= column_length-1:
                        if current_honeycomb[current_index] == "X":
                            escape_down_left = False
                            break
                        current_row_position -= 1
                        current_column_position += 1
                        current_index += (row_length-1)
                    print("Found down_left: " + str(escape_down_left) + "\n")

                    # down_right
                    current_index = i
                    current_row_position = i % row_length
                    current_column_position = i // row_length
                    while current_row_position <= row_length-1 and current_column_position <= column_length-1:
                        if current_honeycomb[current_index] == "X":
                            escape_down_right = False
                            break
                        current_row_position += 1
                        current_column_position += 1
                        current_index += (row_length+1)
                    print("Found down_right: " + str(escape_down_right) + "\n")

                    break

            escaped = ""
            if escape_left or escape_right or escape_up_left or escape_up_right or escape_down_left or escape_down_right:
                escaped = "FREE"
            else:
                escaped = "TRAPPED"
            file_out.writelines(escaped + "\n")
        file.close()
        file_out.close()


if __name__ == '__main__':
    stage3()
