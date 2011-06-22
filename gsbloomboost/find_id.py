import os, sys
from bloom import Bloom


def call_main(author_name):
    bf = Bloom()
    count = bf.search("/Users/vivekris/GS/code/gsbloomboost/input/filters/",author_name)


if __name__ == "__main__":
    if (len(sys.argv) != 2 ):
        print "Usage python find_id.py <author_name>\n"
        sys.exit(0)
    call_main(sys.argv[1])
