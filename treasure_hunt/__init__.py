import argparse
import numpy
import os
from . import oop_implementation, fp_implementation

TREASURE_MAP_FILE_PATH = os.path.join(
    os.path.dirname(os.path.relpath(__file__)),
    'treasure_map.txt'
)
OOP = 'oop'
FP = 'fp'


def main():
    parser = argparse.ArgumentParser(description="Treasure Hunt")
    parser.add_argument(
        '--implementation',
        help='choose the implementation',
        choices=(OOP, FP),
        default=OOP,
        const=OOP,
        nargs='?'
    )
    implementation = parser.parse_args().implementation

    # Load treasure map from a file.
    treasure_map = numpy.loadtxt(TREASURE_MAP_FILE_PATH, dtype=int,
                                 delimiter=' ')

    print('Implementation:', '\n', implementation)
    print('Treasure Map:', '\n', treasure_map)

    lookup_table = {
        OOP: oop_implementation.find_treasure,
        FP: fp_implementation.find_treasure
    }

    try:
        treasure_path = lookup_table[implementation](treasure_map)
    except ValueError as err:
        print(err)
    else:
        print('Path To Treasure:', '\n', treasure_path)
