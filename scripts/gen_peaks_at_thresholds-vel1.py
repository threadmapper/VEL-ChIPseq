"""

Filter by or keep qscore >= 15

step-wise\bwa_mapping\uniq-nopcr-dups\FINAL_BAM\macs3-narrow\PEAKS\SURVIVAL-PEAKS\discard-peak-more-than-one-control\VEL1\SURVIVED

"""

import math
import glob 


samples =  glob.glob('s_*.bed')



#q = 0.0000000001 # Q10
#q = 0.000000000000001 # Q_15
q = 1e-15

threshold = -math.log(q, 10)
print ('threshold = ', threshold) 
folder = 'Q'+ str(int(round(threshold)))
print ('folder = ', folder)
 

 
for s in samples:
    with open(s ) as inp, open(folder + '/' + s, 'w') as outf:
        for line in inp:
            A = line.strip().split()   
            qscore =  float(A[-2]) # narrow peak has q-values as the second last col
            #assert qscore > threshold , A
            if qscore > threshold:
               outf.write(line.strip() + '\n')
   

            