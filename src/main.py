# -*- coding: utf-8 -*-
import argparse
import sys

from CalcRating import CalcRating
from CountStudent import CountStudent
from TextDataReaderYAML import TextDataReaderYAML


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = TextDataReaderYAML()
    students = reader.read(path)
    print("Students: ", students)

    rating = CountStudent(students).calc()
    print("StudentCount", rating.countStudent)


# точка вхождения
if __name__ == "__main__":
    main()
