# Defining calendar layout
layer_1 = [  # top, smallest
    ['', '', '', '', '', '', '', '', '', '', '', '', ],
    ['', '', '', '', '', '', '', '', '', '', '', '', ],
    ['', '', '', '', '', '', '', '', '', '', '', '', ],
    ['15', '', '8', '', '3', '', '6', '', '10', '', '7', '']
]

layer_2 = [
    ['', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '4', '', '7', '15', '', '', '14', '', '9', '', '12'],
    ['17', '7', '3', '', '6', '', '11', '11', '6', '11', '', '6']
]

layer_3 = [
    ['', '', '', '', '', '', '', '', '', '', '', ''],
    ['22', '', '16', '', '9', '', '5', '', '10', '', '8', ''],
    ['11', '26', '14', '1', '12', '', '21', '6', '15', '4', '9', '18'],
    ['17', '4', '5', '', '7', '8', '9', '13', '9', '7', '13', '21']
]

layer_4 = [ 
    ['12', '', '6', '', '10', '', '10', '', '1', '', '9', ''],
    ['2', '13', '9', '', '17', '19', '3', '12', '3', '26', '6', ''],
    ['6', '', '14', '12', '3', '8', '9', '', '9', '20', '12', '3'],
    ['7', '14', '11', '', '8', '', '16', '2', '7', '', '9', '']
]

layer_5 = [  # bottom, biggest
    ['16', '8', '7', '8', '8', '3', '4', '12', '2', '5', '10', '7'],
    ['21', '21', '9', '9', '4', '4', '6', '6', '3', '3', '14', '14'],
    ['12', '13', '14', '15', '4', '5', '6', '7', '8', '9', '10', '11'],
    ['11', '14', '11', '14', '11', '11', '14', '11', '14', '11', '14', '14']
]

# HELPER FUNCTIONS
# returns a top-down view of the calendar
def compile_calendar():
    rows = 4
    cols = 12
    calendar = [[''] * cols for _ in range(rows)]
    
    for row in range(rows):
        for col in range(cols):

            for layer in (layer_1, layer_2, layer_3, layer_4, layer_5):
                if layer[row][col] != '':
                    calendar[row][col] = layer[row][col]
                    break

    return calendar

# returns the specified layer, rotated once
def rotate_layer(layer):
    for i in range(len(layer)):
        layer[i] = layer[i][-1:] + layer[i][:-1]

# prints the calendar in a readable format
def display(cal):
    for row in cal:
        print("".join(f"{value:<{4}}" for value in row))
    print()

# evaluates the calendar to check if all columns add to 42
def evaluate(cal):
    # convert to integers:
    int_cal = [[int(value) for value in row] for row in cal]
    
    sums = []
    for col in range(len(int_cal[0])):
        sum = 0
        for row in int_cal:
            sum += row[col]
        sums.append(sum)
        
    return all(col_sum == 42 for col_sum in sums)

# brute force compute solution
def solve():
    solutions = []

    for _ in range(len(layer_5[0])):
        for _ in range(len(layer_4[0])):
            for _ in range(len(layer_3[0])):
                for _ in range(len(layer_2[0])):
                    for _ in range(len(layer_1[0])):

                        calendar = compile_calendar()
                        if evaluate(calendar):
                            solutions.append(calendar)

                        rotate_layer(layer_1)               
                    rotate_layer(layer_2)               
                rotate_layer(layer_3)
            rotate_layer(layer_4)
        rotate_layer(layer_5)

    print(f'Found {len(solutions)} solutions!')
    return solutions

# Main
if __name__ == "__main__":
    for sol in solve():
        display(sol)