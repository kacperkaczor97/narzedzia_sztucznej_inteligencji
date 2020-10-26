# Kacper Kaczor

# Power of Thor - Episode 1
# https://www.codingame.com/ide/puzzle/power-of-thor-episod

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    direction1 = ""
    direction2 = ""

    if initial_tx == light_x:
        if initial_ty > light_y:
            direction2 = "N"
            initial_ty -= 1
        elif initial_ty < light_y:
            direction1 = "S"
            initial_ty += 1

    elif initial_ty == light_y:
        if initial_tx > light_x:
            direction1 = "W"
            initial_tx -= 1
        elif initial_tx < light_x:
            direction2 = "E"
            initial_tx += 1

    elif initial_tx != light_x and initial_ty != light_y:
        if initial_ty > light_y and initial_tx > light_x:
            direction2 = "NW"
            initial_tx -= 1
            initial_ty -= 1
        elif initial_ty > light_y and initial_tx < light_x:
            direction2 = "NE"
            initial_tx += 1
            initial_ty -= 1
        elif initial_ty < light_y and initial_tx > light_x:
            direction1 = "SW"
            initial_tx -= 1
            initial_ty += 1
        elif initial_ty < light_y and initial_tx < light_x:
            direction1 = "SE"
            initial_tx += 1
            initial_ty += 1

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(direction2 + direction1)
