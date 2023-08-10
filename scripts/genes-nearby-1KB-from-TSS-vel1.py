#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0103, W1514, C0301, C0413

"""

# 5kb annotated as genes
bedtools window -a h_s_VEL1@Before_cold@12_8_VEL1_NV.bed -b TAIR10_GFF3_unique_genes.gff  -w 5000

singularity exec ~/BUILD/VERN/idr_bwa.sif python3 genes-nearby-1KB-from-TSS.py

"""

import subprocess
import os
import time
import glob


def gen_submit_file(peak_file="test.narrowPeak", sumit_filer="submit-test.bed"):
    head = ['chrom', 'beg', 'end', 'peak', 'score', 'dot', 'p', 'fold', 'q', 'offset']
    sumit_head = ['chrom', 'beg', 'end', 'peak', 'q']
    with open(peak_file) as inp, open(sumit_filer, 'w') as outF:
        for line in inp:
            A = line.strip().split()
            d = dict(zip(head, A))
            d['end'] = int(d['beg']) + int(d['offset']) + 1
            d['beg'] = int(d['beg']) + int(d['offset'])
            pipe = [str(d[h]) for h in sumit_head]
            outF.write('\t'.join(pipe) + '\n')
    return sumit_filer


if __name__ == '__main__':

    trt_files = glob.glob('h_s_*.bed')
    for g in trt_files:
        print(g)
        assert os.path.isfile(g)
        sumit_file = gen_submit_file(peak_file=g, sumit_filer="submit-" + g[4:])
        time.sleep(10)
        with open('GENES/' + g[4:], 'w') as outf:
            cmd = ['bedtools', 'window', '-a', sumit_file, '-b', 'TSS-genes.bed', '-w', '1000']
            print(cmd)
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)
            for line in p.stdout:
                pipe_out = line.strip() + '\t@' + g[:-4]  #
                outf.write(pipe_out + '\n')

    print('DONE')
