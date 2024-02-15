with open('day1.txt', 'r') as file:
    instructions = file.read()
def final_floor(instructions):
    floor = 0
    for char in instructions:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
    return floor
print(final_floor(instructions))
