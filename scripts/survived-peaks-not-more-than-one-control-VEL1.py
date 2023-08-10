import sys
from collections import defaultdict

def load_peaks_from_black_bed(filer):
    """
    Chr1   2972    3327    12_8_VEL1_NV_peak_1     259     .       3.13636 27.7337 25.9826 154
    """
    black_peaks = defaultdict(set)
    peak_header = ['chrom', 'beg', 'end', 'peak_name', 'score', 'strand', 'enrichment_signal', 'pval', 'qval', 'offset', 'CTRL']
    with open(filer) as inp:
      for line in inp:
        if line: 
           A = line.strip().split()
           assert len(A) == len(peak_header)
           d = dict(zip(peak_header, A))
           black_peaks[d['peak_name']].add(d['CTRL']) # can hit in the same sample mutiple ovelapping control peaks 

    return black_peaks


def survival_peaks_from_black_bed(black_peaks, candi_filer, outfiler = ''):
    """
    Chr1   2972    3327    12_8_VEL1_NV_peak_1     259     .       3.13636 27.7337 25.9826 154
    """
    peak_header = ['chrom', 'beg', 'end', 'peak_name', 'score', 'strand', 'enrichment_signal', 'pval', 'qval', 'offset']
    
    with open(candi_filer) as inp, open(outfiler, 'w') as outf:
      for line in inp:
        if line: 
           A = line.strip().split()
           assert len(A) == len(peak_header)
           d = dict(zip(peak_header, A))
           this_peak = d['peak_name']
           if this_peak not in black_peaks or not len(black_peaks[this_peak]) > 1: # control free or not be in more than 1 controls region
              outf.write(line.strip() + '\n') # should control free
 

if __name__ == '__main__':

   #conditions =  ['Control', 'Before_cold', 'Cold']
   mega = cluster_by_protein =   {'VRN5@Cold': ['VRN5@Cold@VRN5-YFP-6WT0-rep2.bed', 'VRN5@Cold@VRN5-YFP-6WT0-rep1.bed', 'VRN5@Cold@VRN5-YFP-6WT0-rep3.bed'], 
                               'VEL1@Before_cold': ['VEL1@Before_cold@VEL1-FLAG-NV-rep1.bed', 'VEL1@Before_cold@VEL1-FLAG-NV-rep3.bed', 'VEL1@Before_cold@VEL1-FLAG-NV-rep2.bed'], 
                               'VIN3@Control': ['VIN3@Control@ColFRI-6WT0-For-GFP-ColFR-Rep1.bed', 'VIN3@Control@ColFRI-NV-IP-For-GFP-ColFR-Rep2.bed', 'VIN3@Control@ColFRI-6WT0-For-GFP-ColFR-Rep2.bed', 
                              'VIN3@Control@ColFRI-NV-IP-For-GFP-ColFR-Rep1.bed'], 'VRN5@Before_cold': ['VRN5@Before_cold@VRN5-YFP-NV-rep1.bed', 'VRN5@Before_cold@VRN5-YFP-NV-rep2.bed', 'VRN5@Before_cold@VRN5-YFP-NV-rep3.bed'], 'VIN3@Cold': ['VIN3@Cold@VIN3-eGFP-6WT0-rep1.bed', 'VIN3@Cold@VIN3-eGFP-6WT0-rep2.bed', 'VIN3@Cold@VIN3-eGFP-6WT0-rep3.bed'], 'VRN5@Control': ['VRN5@Control@ColFRI-6WT0-For-GFP-ColFR-Rep1.bed', 'VRN5@Control@ColFRI-NV-IP-For-GFP-ColFR-Rep2.bed', 'VRN5@Control@ColFRI-6WT0-For-GFP-ColFR-Rep2.bed', 'VRN5@Control@ColFRI-NV-IP-For-GFP-ColFR-Rep1.bed'], 'VEL1@Control': ['VEL1@Control@ColFRI-NV-IP-for-ColFRI-FLAG-Rep1.bed', 'VEL1@Control@ColFRI-NV-IP-for-ColFRI-FLAG-Rep2.bed', 'VEL1@Control@ColFRI-6WT0-for-ColFRI-FLAG-Rep1.bed'], 'VIN3@Before_cold': ['VIN3@Before_cold@VIN3-eGFP-NV-rep1.bed', 'VIN3@Before_cold@VIN3-eGFP-NV-rep2.bed'], 'VEL1@Cold': ['VEL1@Cold@VEL1-FLAG-6WT0-rep2.bed', 'VEL1@Cold@VEL1-FLAG-6WT0-rep3.bed', 'VEL1@Cold@VEL1-FLAG-6WT0-rep1.bed']
   }

   prot = 'VEL1'
   #----------------------

   trt_files = mega[prot + '@' + 'Before_cold']  +  mega[prot + '@' + 'Cold'] #
   control_files = mega[prot + '@Control']  # Note vin3 used vrn5 controls

    
   for filer in trt_files:
       print ('loading ..', filer)   
       black_peaks = load_peaks_from_black_bed('BLACK-PEAKS/' + filer) 
       print  ('black_peaks = ',  len(black_peaks))
       ####
       # load candidates and write the survival
       survival_peaks_from_black_bed(black_peaks, filer, outfiler = 'SURVIVED/s_' + filer) 
       print (' ')  

"""
[cheemaj@NBI-HPC interactive VEL1]$ pwd
/jic/scratch/groups/Caroline-Dean/jitender/mathias/all-experiments-comparison/FDR-001/DISCARD-PEAKS-MORE-THAN-ONE-CONTROL/VEL1
[cheemaj@NBI-HPC interactive VEL1]$

[cheemaj@NBI-HPC interactive VEL1]$ python3 -u black-list-by-control-peaks-VEL1.py
VEL1@Before_cold@12_8_VEL1_NV.bed
VEL1@Before_cold@23_9_VEL1_NV.bed
VEL1@Before_cold@31_8_VEL1_NV.bed
VEL1@Cold@16_9_VEL16W0.bed
VEL1@Cold@26_7_VEL1_6W0.bed
VEL1@Cold@7_9_VEL1_6W0.bed
trt_files =  ['VEL1@Before_cold@12_8_VEL1_NV.bed', 'VEL1@Before_cold@23_9_VEL1_NV.bed', 'VEL1@Before_cold@31_8_VEL1_NV.bed', 'VEL1@Cold@16_9_VEL16W0.bed', 'VEL1@Cold@26_7_VEL1_6W0.bed', 'VEL1@Cold@7_9_VEL1_6W0.bed']
ctr_files =  ['VEL1@Control@15_9_ColFRINV.bed', 'VEL1@Control@21_9_FRI.bed', 'VEL1@Control@9_9_FRI_NV.bed']
DONE
[cheemaj@NBI-HPC interactive VEL1]$ 
##
[cheemaj@NBI-HPC interactive CONTROL-MATCH-PEAKS]$ wc -l *.bed
   8582 VEL1@Before_cold@12_8_VEL1_NV.bed
   9343 VEL1@Before_cold@23_9_VEL1_NV.bed
   8611 VEL1@Before_cold@31_8_VEL1_NV.bed
   9424 VEL1@Cold@16_9_VEL16W0.bed
   6641 VEL1@Cold@26_7_VEL1_6W0.bed
   9073 VEL1@Cold@7_9_VEL1_6W0.bed
  51674 total
[cheemaj@NBI-HPC interactive CONTROL-MATCH-PEAKS]$



"""
