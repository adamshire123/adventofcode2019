# Day 2: 1202 Program Alarm
import re
initial_program = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,61,45,225,102,94,66,224,101,-3854,224,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1101,31,30,225,1102,39,44,224,1001,224,-1716,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1101,92,41,225,101,90,40,224,1001,224,-120,224,4,224,102,8,223,223,1001,224,1,224,1,223,224,223,1101,51,78,224,101,-129,224,224,4,224,1002,223,8,223,1001,224,6,224,1,224,223,223,1,170,13,224,101,-140,224,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1101,14,58,225,1102,58,29,225,1102,68,70,225,1002,217,87,224,101,-783,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1101,19,79,225,1001,135,42,224,1001,224,-56,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,2,139,144,224,1001,224,-4060,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,1102,9,51,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,226,224,102,2,223,223,1006,224,329,101,1,223,223,108,677,677,224,102,2,223,223,1005,224,344,101,1,223,223,107,677,677,224,1002,223,2,223,1005,224,359,101,1,223,223,1107,226,677,224,1002,223,2,223,1005,224,374,1001,223,1,223,1008,677,677,224,102,2,223,223,1006,224,389,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,8,677,226,224,102,2,223,223,1005,224,419,1001,223,1,223,8,226,226,224,102,2,223,223,1006,224,434,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,449,101,1,223,223,1107,677,226,224,102,2,223,223,1005,224,464,101,1,223,223,1108,226,226,224,102,2,223,223,1006,224,479,1001,223,1,223,7,677,677,224,1002,223,2,223,1006,224,494,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,509,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,524,101,1,223,223,8,226,677,224,1002,223,2,223,1005,224,539,101,1,223,223,1007,226,226,224,102,2,223,223,1006,224,554,1001,223,1,223,108,226,226,224,1002,223,2,223,1006,224,569,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,584,101,1,223,223,108,226,677,224,102,2,223,223,1005,224,599,101,1,223,223,1007,226,677,224,102,2,223,223,1006,224,614,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,629,1001,223,1,223,107,226,226,224,1002,223,2,223,1006,224,644,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,659,1001,223,1,223,107,677,226,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226]

def intcode(program: list, input_instruction: int, pointer=0):
    # if program[pointer] not in [1, 2, 3, 4, 99]:
    # return("unknown operator")

    while not re.match(r"\d{0,3}99$", str(program[pointer])):

        # parse parameter mode
        # param mode 0 = position (get value from position given by param)
        # param mode 1 = immediate (get value from param)

        # parse instruction
        # instruction = re.match(r"(\d)??(\d)??(\d)??(\d{0,2})$", \
        # str(program[pointer]))
        # put match groups in a dict, use 0 as default if group is empty

        # initialize params list

        opcode = program[pointer] // 10**0 % 100
        param_modes = [program[pointer] // 10**i % 10 for i in range(2, 5)]

        if opcode == 1:
            # operator 1: add
            params = get_params(3, param_modes, program, pointer)
            program[params[2]] = program[params[0]] + program[params[1]]
            pointer = pointer + 4
            continue

        if opcode == 2:
            # operator 2: multiply
            params = get_params(3, param_modes, program, pointer)
            program[params[2]] = program[params[0]] * \
                program[params[1]]
            # move the pointer ahead 4 places
            pointer = pointer + 4
            continue

        if opcode == 3:
            # operator 3: assign input
            params = get_params(1, param_modes, program, pointer)
            program[params[0]] = input_instruction
            pointer = pointer + 2
            continue

        if opcode == 4:
            # operator 4: return output
            params = get_params(1, param_modes, program, pointer)
            output = program[params[0]]
            pointer = pointer + 2
            continue

        if opcode == 5:
            # operator 5: if param 1 is non-zero set pointer to param 2
            params = get_params(2, param_modes, program, pointer)
            if program[params[0]] != 0:
                pointer = program[params[1]]
            else:
                pointer = pointer + 3
            continue

        if opcode == 6:
            # opereator 6: if param 1 is 0 set pointer to param 2
            params = get_params(2, param_modes, program, pointer)
            if program[params[0]] == 0:
                pointer = program[params[1]]
            else:
                pointer = pointer + 3
            continue

        if opcode == 7:
            # operator 7: if param 1 is less than param 2 store '1' in param 3
            params = get_params(3, param_modes, program, pointer)
            if program[params[0]] < program[params[1]]:
                program[params[2]] = 1
            else:
                program[params[2]] = 0
            pointer = pointer + 4
            continue

        if opcode == 8:
            # operator 8: if param 1 is equal to param 2 store '1' in param 3
            params = get_params(3, param_modes, program, pointer)
            if program[params[0]] == program[params[1]]:
                program[params[2]] = 1
            else:
                program[params[2]] = 0
            pointer = pointer + 4
            continue

    print(output)


def get_params(numberOfParams, param_modes, program, pointer):
    params = []
    for i in range(1, numberOfParams+1):
        param = pointer + i if param_modes[i-1] == 1 \
            else program[pointer + i]
        params.append(param)
    return params


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
    intcode(initial_program, 5, 0)
