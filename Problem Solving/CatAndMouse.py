#!/bin/python3

import os
import sys



def catAndMouse(x, y, z):
    distanceA = abs(x - z)
    distanceB = abs(y - z)

    if distanceA < distanceB:
        return "Cat A"
    elif distanceB < distanceA:
        return "Cat B"
    else:
        return "Mouse C"
   


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        f.write(result + '\n')

    f.close()
