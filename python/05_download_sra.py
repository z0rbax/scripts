#!/usr/bin/env python3
import os
import sys
import subprocess


def main():
    if len(sys.argv) != 2:
        print(f"\nUsage: ./{os.path.basename(sys.argv[0])} <srr_ids.txt>\n",
              file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1], 'r') as srr_id:
        srrs = srr_id.read().split("\n")

    for i in srrs:
        print("Downloading %s" % i)
        subprocess.call('fastq-dump -F --gzip --split-3 %s' % i, shell=True)


if __name__ == '__main__':
    main()
