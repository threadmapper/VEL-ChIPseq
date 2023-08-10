#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0103, W1514, C0301, C0413

"""

Gather survived Q15 peaks from:
  s_VEL1@Before_cold@VEL1-FLAG-NV-rep1.bed
if the peak name apprears in 

singularity exec ~/BUILD/VERN/idr_bwa.sif python3 ggather_survival-1KB-vel1.py

>>VEL1-FLAG-NV-rep1_summits.bed
Chr1    3132    3133    VEL1-FLAG-NV-rep1_peak_1        20.8915
Chr1    13696   13697   VEL1-FLAG-NV-rep1_peak_2        43.9649

step-wise\bwa_mapping\uniq-nopcr-dups\FINAL_BAM\macs3-narrow\PEAKS\SURVIVAL-PEAKS\discard-peak-more-than-one-control\VEL1\SURVIVED\Q15\HITS\GATHER-ORIGINAL-PEAKS

"""

import subprocess
import os
import time
import glob
from collections import defaultdict


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


def get_peak_names(peak_file="test.narrowPeak"):
    head = ['chrom', 'beg', 'end', 'peak', 'score', 'dot', 'p', 'fold', 'q', 'offset']
    peak_names = set()
    with open(peak_file) as inp:
        for line in inp:
            A = line.strip().split()
            d = dict(zip(head, A))
            peak_names.add(d['peak'])
    return peak_names


if __name__ == '__main__':

    for trt_bed in ['VEL1@Before_cold@VEL1-FLAG-NV-rep1.bed', 'VEL1@Before_cold@VEL1-FLAG-NV-rep2.bed', 'VEL1@Before_cold@VEL1-FLAG-NV-rep3.bed', 'VEL1@Cold@VEL1-FLAG-6WT0-rep1.bed', 'VEL1@Cold@VEL1-FLAG-6WT0-rep2.bed', 'VEL1@Cold@VEL1-FLAG-6WT0-rep3.bed']:

        origin_bed =   '../../s_' + trt_bed
        common_segment_bed = '../h_s_' + trt_bed  # segments
        filtered_original_bed = 'f_s_' + trt_bed
        filtered_original_bed_summitfile = 'summit-f_s_' + trt_bed

        assert os.path.isfile(origin_bed)
        assert os.path.isfile(common_segment_bed)

        common_peaks_for_this_rep = get_peak_names(peak_file=common_segment_bed)
        head = ['chrom', 'beg', 'end', 'peak', 'score', 'dot', 'p', 'fold', 'q', 'offset']
        with open(origin_bed) as inp, open(filtered_original_bed, "w") as outf:
            for line in inp:
                A = line.strip().split()
                d = dict(zip(head, A))
                if d['peak'] in common_peaks_for_this_rep:
                    outf.write('\t'.join(A) + '\n')

        # --------------------
        gen_submit_file(peak_file=filtered_original_bed, sumit_filer=filtered_original_bed_summitfile)
        print('Written file:', filtered_original_bed)
        print('Written file:', filtered_original_bed_summitfile)

        with open('GENES/' + 'genes_' + filtered_original_bed_summitfile, 'w') as outf:
            cmd = ['bedtools', 'window', '-a', filtered_original_bed_summitfile, '-b', 'TSS-genes.bed', '-w', '1000']
            print(cmd)
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)
            for line in p.stdout:
                pipe_out = line.strip() + '\t@' + filtered_original_bed_summitfile[:-4]  #
                outf.write(pipe_out + '\n')

    print('Done')
