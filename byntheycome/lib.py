# by-n-they-come Copyright © 2021 Aaron Seilis. See LICENSE for details.

import argparse
import os
import shutil
import sys

from typing import Iterator, List, Tuple

def eprint(*args, **kwargs):
    """Error print

    Prints an error to stderr by passing through the correct arguments to
    ``print``.
    """
    print(*args, file=sys.stderr, **kwargs)

def split_iter_by_n(files, n: int) -> Iterator[Tuple[int, List[str]]]:
    """Split a list of files into N evenly-sized groups

    :param files: The files to be split into groups
    :param n: The size of the groups
    :return: An iterator of (group_number, group) pairs
    """
    for grp_number, i in enumerate(range(0, len(files), n)):
        yield grp_number, files[i:i+n]

def main():
    """Entry point for the CLI tool"""
    parser = argparse.ArgumentParser()
    parser.add_argument('N', type=int, help="How many in each bin")
    parser.add_argument('FILES', nargs='+', help="The files to group")
    args = parser.parse_args()

    if len(args.FILES) % args.N > 0:
        eprint(f"the number of input files ({len(args.FILES)}) doesn't evenly divide by {args.N}")

    for number, group in split_iter_by_n(args.FILES, args.N):
        print(number, group)
        dir_name = f"{number:02}"
        os.mkdir(dir_name)
        for f in group:
            shutil.move(f, os.path.join(dir_name, f))


