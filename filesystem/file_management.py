#!/usr/bin/env python3

from exceptions import FileNotFoundError

__header__ = """
                              -`
              ...            .o+`
           .+++s+   .h`.    `ooo/
          `+++%++  .h+++   `+oooo:
          +++o+++ .hhs++. `+oooooo:
          +s%%so%.hohhoo'  'oooooo+:
          `+ooohs+h+sh++`/:  ++oooo+:
           hh+o+hoso+h+`/++++.+++++++:
            `+h+++h.+ `/++++++++++++++:
                     `/+++ooooooooooooo/`
                    ./ooosssso++osssssso+`
                   .oossssso-````/osssss::`
                  -osssssso.      :ssss``to.
                 :osssssss/  Mike  osssl   +
                /ossssssss/   8a   +sssslb
              `/ossssso+/:-        -:/+ossss'.-
             `+sso+:-`                 `.-/+oso:
            `++:.                           `-/+/
            .`                                 `/
"""


def find_file(root, filename):
    """Find a file recursively in the parent directories

    :root: TODO
    :filename: TODO
    :returns: TODO

    """
    pass


def is_file(filename):
    """Tells whether or not the given string is a file in the current dir

    :filename: TODO
    :returns: TODO

    """
    pass


def is_dir(dirname):
    """Tells whether or not the given string is a dir inside the current dir

    :dirname: TODO
    :returns: TODO

    """
    pass


def is_empty(name):
    """Tells whether or not the given file/dir is empty

    :name: TODO
    :returns: TODO

    """
    pass


if __name__ == "__main__":
    raise Exception(
        "This module is not intended to run as a standalone scripts")
