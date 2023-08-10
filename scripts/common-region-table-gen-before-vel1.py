"""

Multi intersect we need an overlap of two or more bed files: 

step-wise\bwa_mapping\uniq-nopcr-dups\FINAL_BAM\macs3-narrow\PEAKS\SURVIVAL-PEAKS\discard-peak-more-than-one-control\VEL1\SURVIVED\Q15

"""

import subprocess
import os
import glob



categ = 'before'

trt_files = glob.glob('*@Before_cold@*')

for g in trt_files:
  assert os.path.isfile(g) 

names = [trt[:-4] for trt in  trt_files]
with open(categ + '-multi.txt','w') as outf:    
    cmd = ['bedtools',  'multiinter', '-header', '-names'] + names + ['-i'] +  trt_files
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)
    for line in p.stdout:
        pipe_out = line.strip() #+ '\t@' + 'VEL1-control' ##g[:-4]) #
        outf.write(pipe_out + '\n') 

print ('trt_files = ', trt_files)
print ('DONE')
