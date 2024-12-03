#!/usr/bin/env python3

"""
Description of your project.
"""

import argparse


def main():
    parser = argparse.ArgumentParser(description="Description of your script.")
    # Add arguments here if needed
    # parser.add_argument('-f', '--file', help='File to process', required=True)
    args = parser.parse_args()

    # Your main logic here
    print("hello world")
    day01()

def day01():
    print("day 1 - attempt 1")

if __name__ == "__main__":
    main()