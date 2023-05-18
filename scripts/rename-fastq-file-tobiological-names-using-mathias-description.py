#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0103, W1514, C0301, C0413

"""
Renaming files using the Descriptive names

"""

head = ['experiment', 'MD5', 'FASTQ', 'biological-name']
records = 0
with open('checksums_MLN.csv') as inp, open('checksums_MLN-renamed.csv', 'w') as outf:
    next(inp)
    outf.write(','.join(head) + '\n')
    for line in inp:
        A = line.strip().split(',')
        d = dict(zip(head, A))
        experi = d['experiment'].replace('(', '').replace(')', '')
        new_fq_name = '-'.join(experi.split()) + '.fq.gz'
        d['biological-name'] = new_fq_name
        outf.write(','.join([d[h] for h in head]) + '\n')
        records += 1
        print(' '.join(['cp', '../' + d['FASTQ'], new_fq_name]))

print('# records written: ', records)
print('# Done')
