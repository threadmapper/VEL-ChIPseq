#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=C0103, W1514, C0301, C0413

"""
Renaming files using the Descriptive names

"""
from collections import defaultdict

head = ['experiment', 'MD5', 'FASTQ', 'biological-name']
records = 0
seen = defaultdict(list)
with open('checksums_MLN-suggested-fixed.csv') as inp, open('checksums_MLN-suggested-fixed-renamed.csv', 'w') as outf:
    next(inp)
    outf.write(','.join(head) + '\n')
    for line in inp:
        A = line.strip().split(',')
        d = dict(zip(head, A))
        experi = d['experiment'].replace('(', '').replace(')', '')
        new_fq_name = '-'.join(experi.split()) + '.fq.gz'
        d['biological-name'] = new_fq_name
        seen[new_fq_name].append(d)
        outf.write(','.join([d[h] for h in head]) + '\n')
        print(' '.join(['cp', '../' + d['FASTQ'].strip(), new_fq_name]))
        records += 1

# check for duplicates
for new_fq_name, rows in seen.items():
    if len(rows) > 1:
        print(rows)
        for a in rows:
            print(' '.join(a))
print('# records written: ', records)
print('# Done')
