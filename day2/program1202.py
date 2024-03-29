# Day 2: 1202 Program Alarm

initial_program = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 6, 1,
                   19, 1, 19, 5, 23, 2, 10, 23, 27, 2, 27, 13, 31, 1, 10, 31,
                   35, 1, 35, 9, 39,
                   2, 39, 13, 43, 1, 43, 5, 47, 1, 47, 6, 51, 2, 6, 51, 55, 1,
                   5,
                   55, 59, 2, 9, 59, 63, 2, 6, 63, 67, 1, 13, 67, 71, 1, 9,
                   71, 75, 2, 13, 75, 79, 1, 79, 10, 83, 2, 83, 9, 87, 1, 5,
                   87, 91, 2, 91, 6, 95, 2, 13, 95, 99, 1, 99, 5, 103, 1, 103,
                   2, 107, 1, 107, 10, 0, 99, 2, 0, 14, 0]


def intcode(program: list, pointer=0):
    # print(f"current program is {program} ")
    if program[pointer] not in [1, 2, 99]:
        return("unknown Opcode")
    if program[pointer] == 99:
        return program[0]
    if program[pointer] == 1:
        # add next two indexes
        program[program[pointer+3]] = program[program[pointer+1]] + \
            program[program[pointer+2]]
        # move the pointer
        pointer = pointer + 4
        intcode(program, pointer)
        return program[0]
    if program[pointer] == 2:
        program[program[pointer+3]] = program[program[pointer+1]] * \
            program[program[pointer+2]]
        pointer = pointer + 4
        intcode(program, pointer)
        return program[0]


def seek(target):
    for noun in range(99):
        for verb in range(99):
            current_program = initial_program.copy()
            current_program[1] = noun
            current_program[2] = verb
            result = intcode(current_program)
            if result == target:
                print(f"noun: {noun} \nverb: {verb}\n\
solution: {100*noun + verb}")


if __name__ == "__main__":
    seek(19690720)
