"""
Find an overlap coordinates from multi overlap record:

>> before-multi.txt
chrom   start   end     num     list    s_VEL1@Before_cold@VEL1-FLAG-NV-rep1    s_VEL1@Before_cold@VEL1-FLAG-NV-rep3    s_VEL1@Before_cold@VEL1-FLAG-NV-rep2
Chr1    2870    2969    1       s_VEL1@Before_cold@VEL1-FLAG-NV-rep3    0       1       0
Chr1    2969    2988    2       s_VEL1@Before_cold@VEL1-FLAG-NV-rep1,s_VEL1@Before_cold@VEL1-FLAG-NV-rep3       1       1       0
Chr1    2988    3278    3       s_VEL1@Before_cold@VEL1-FLAG-NV-rep1,s_VEL1@Before_cold@VEL1-FLAG-NV-rep3,s_VEL1@Before_cold@VEL1-FLAG-NV-rep2  1       1       1
Chr1    3278    3311    2       s_VEL1@Before_cold@VEL1-FLAG-NV-rep1,s_VEL1@Before_cold@VEL1-FLAG-NV-rep3       1       1       0
Chr1    3311    3317    1       s_VEL1@Before_cold@VEL1-FLAG-NV-rep1    1       0       0

>> before-multi.bed
Chr1    2969    2988
Chr1    2988    3278
Chr1    3278    3311

>> we overlap each sruvived and q15 filtered bed: [s_VEL1@Before_cold@VEL1-FLAG-NV-rep1.bed] with before-multi.bed
Chr1    2969    3317    VEL1-FLAG-NV-rep1_peak_1        208     .       2.73556 22.5402 20.8915 163
Chr1    13347   13917   VEL1-FLAG-NV-rep1_peak_2        439     .       4.19425 46.2327 43.9649 349
Chr1    16600   16904   VEL1-FLAG-NV-rep1_peak_3        300     .       3.30054 31.9306 30.0327 144
Chr1    20195   21544   VEL1-FLAG-NV-rep1_peak_4        564     .       3.97425 59.0151 56.4047 811
Chr1    37766   38359   VEL1-FLAG-NV-rep1_peak_8        430     .       3.22907 45.2874 43.0431 301
Chr1    46754   47023   VEL1-FLAG-NV-rep1_peak_10       230     .       2.98503 24.745  23.0363 124

>> to get segments [ h_s_VEL1@Before_cold@VEL1-FLAG-NV-rep1.bed ]
Chr1    2969    2988    VEL1-FLAG-NV-rep1_peak_1        208     .       2.73556 22.5402 20.8915 163     @s_VEL1@Before_cold@VEL1-FLAG-NV-rep1
Chr1    2988    3278    VEL1-FLAG-NV-rep1_peak_1        208     .       2.73556 22.5402 20.8915 163     @s_VEL1@Before_cold@VEL1-FLAG-NV-rep1
Chr1    3278    3311    VEL1-FLAG-NV-rep1_peak_1        208     .       2.73556 22.5402 20.8915 163     @s_VEL1@Before_cold@VEL1-FLAG-NV-rep1
Chr1    13408   13429   VEL1-FLAG-NV-rep1_peak_2        439     .       4.19425 46.2327 43.9649 349     @s_VEL1@Before_cold@VEL1-FLAG-NV-rep1
Chr1    13429   13871   VEL1-FLAG-NV-rep1_peak_2        439     .       4.19425 46.2327 43.9649 349     @s_VEL1@Before_cold@VEL1-FLAG-NV-rep1
Chr1    13871   13910   VEL1-FLAG-NV-rep1_peak_2        439     .       4.19425 46.2327 43.9649 349     @s_VEL1@Before_cold@VEL1-FLAG-NV-rep1
Chr1    16600   16904   VEL1-FLAG-NV-rep1_peak_3        300     .       3.30054 31.9306 30.0327 144     @s_VEL1@Before_cold@VEL1-FLAG-NV-rep1



step-wise\bwa_mapping\uniq-nopcr-dups\FINAL_BAM\macs3-narrow\PEAKS\SURVIVAL-PEAKS\discard-peak-more-than-one-control\VEL1\SURVIVED\Q15

"""
import subprocess
import os
import time

categ = 'before'

output_multi_bed = categ + '-multi.bed'
# write multibed
with open(categ +'-multi.txt') as inp, open(output_multi_bed, 'w') as outf:
  for i, line in enumerate(inp,1):
      A = line.strip().split('\t')    
      if i == 1:
         header = A[:]
         candi_beds = [ a + '.bed' for a in header[5:] ]
         continue

      d = dict(zip(header, A))   
      num = int(d['num'])
      if num >= 2: # in at least 2 samples
         pipe = [ d['chrom'], d['start'], d['end'] ]
         outf.write('\t'.join(pipe) + '\n')    

#
time.sleep(3)

for g in candi_beds:
  print(g)
  assert os.path.isfile(g) 
  with open('HITS/h_' + g ,'w') as outf:    
    cmd = ['bedtools',  'intersect', '-a', g , '-b',  output_multi_bed  ]
    print( cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)
    for line in p.stdout:
        pipe_out = line.strip() + '\t@' + g[:-4] #
        outf.write(pipe_out + '\n') 
