#!/usr/bin/python3
import sys
import subprocess

def main():
    if len(sys.argv) != 2:
        print('This script use Python3\nUsage: ./%s <srr_ids.txt>' \
                                % os.path.basename(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1], 'r') as srr_id:
        srrs = srr_id.read().split("\n")

    for i in srrs:
        print("Downloading %s" % i)
        #subprocess.call('prefetch -a "/opt/aspera/bin/ascp|/opt/aspera/etc/asperaweb_id_dsa.openssh" %s' % i, shell=True)
        #print("Converting SRA > FASTQ")
        subprocess.call('fastq-dump -I --gzip --split-files %s' % i, shell=True)
        #subprocess.call('rm %s.sra' % i, shell=True)
        #subprocess.call('srst2 --input_se %s_1.fastq %s_2.fastq --log --gene_db gene.db --output %s' % (i, i, i), shell=True)

if __name__ == '__main__':
    main()
