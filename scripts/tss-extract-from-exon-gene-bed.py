"""

Select the TSS sites:

step-wise\bwa_mapping\uniq-nopcr-dups\FINAL_BAM\macs3-narrow\PEAKS\SURVIVAL-PEAKS\discard-peak-more-than-one-control\VEL1\SURVIVED\Q15\HITS

Could be off by  +/- one due to bed/gff3 

see; screenshot: ends-TSS.JPG checked in the IGV seems OK 

also: common-peak-segement-replicates.JPG

"""

import glob


def gen_submit_file(peak_file = "test.narrowPeak", sumit_file = "submit-test.bed"):

    head = ['chrom', 'beg', 'end', 'peak', 'score', 'dot', 'p', 'fold', 'q', 'offset']
    sumit_head = ['chrom', 'beg', 'end', 'peak', 'q']
    with open(peak_file) as inp, open(sumit_file, 'w') as outf:
      for line in inp:
        A = line.strip().split()
        d = dict( zip(head, A))
        d['end'] = int(d['beg']) + int(d['offset']) + 1 
        d['beg'] = int(d['beg']) + int(d['offset']) 
        pipe =  [ str(d[h]) for h in sumit_head]
        outf.write('\t'.join(pipe) + '\n')
    return sumit_file


if __name__ == '__main__':

    with open('tss-test-from-exons-gene.bed') as inp, open('TSS-genes.bed', 'w') as outf:

      head = ['chrom', 'beg', 'end', 'gene', 'dot', 'strand']
      for line in inp:
        A = line.strip().split()
        d = dict(zip(head, A))

        if d['strand'] == '+':
           d['beg'] = int(d['beg']) 
           d['end'] = int(d['beg']) + 1
        elif d['strand'] == '-':
           d['beg'] = int(d['end']) - 1
           d['end'] = int(d['end']) 
        pipe =  [ str(d[h]) for h in head]
        outf.write('\t'.join(pipe) + '\n')

 
       

