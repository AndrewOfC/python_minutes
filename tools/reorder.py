import re, glob, os, math
from operator import itemgetter
import argparse


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('prefix', nargs=1)
    parser.add_argument('--suffix', default=".py",)
    parser.add_argument("--increment", default=1)
    parser.add_argument("--command", default="mv ")

    options = parser.parse_args()

    # load filenames
    filenames = glob.glob(f"*{options.suffix}")
    print(f"Found filenames: {filenames}")

    escaped_suffix = re.escape(options.suffix)
    s = f"({options.prefix[0]})([0-9]+)({escaped_suffix})"
    r = re.compile(s)

    def entry(f):
        m = r.match(f)
        if m is None:
            return(None, f)
        return int(m.group(2)), f, m.group(1), m.group(3)
    sfilenames = sorted(map(entry, filenames), key=itemgetter(0))

    number = options.increment
    for place, f, prefix, suffix in sfilenames:
        if place is None:
            continue
        new_place = f"{prefix}{number}{suffix}"
        if( f == new_place ):
            continue
        cmd = f"{options.command} {f} {new_place} &&"
        print(cmd)
        number += options.increment

    return

if __name__ == '__main__':
    main()