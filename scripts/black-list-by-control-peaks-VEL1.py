"""
singularity exec ~/BUILD/VERN/idr_bwa.sif black-list-by-control-peaks-VEL1.py

"""
import subprocess
import os


mega = cluster_by_protein =   {'VRN5@Cold': ['VRN5@Cold@VRN5-YFP-6WT0-rep2.bed', 'VRN5@Cold@VRN5-YFP-6WT0-rep1.bed', 'VRN5@Cold@VRN5-YFP-6WT0-rep3.bed'], 
                               'VEL1@Before_cold': ['VEL1@Before_cold@VEL1-FLAG-NV-rep1.bed', 'VEL1@Before_cold@VEL1-FLAG-NV-rep3.bed', 'VEL1@Before_cold@VEL1-FLAG-NV-rep2.bed'], 
                               'VIN3@Control': ['VIN3@Control@ColFRI-6WT0-For-GFP-ColFR-Rep1.bed', 'VIN3@Control@ColFRI-NV-IP-For-GFP-ColFR-Rep2.bed', 'VIN3@Control@ColFRI-6WT0-For-GFP-ColFR-Rep2.bed', 
                               'VIN3@Control@ColFRI-NV-IP-For-GFP-ColFR-Rep1.bed'], 
                               'VRN5@Before_cold': ['VRN5@Before_cold@VRN5-YFP-NV-rep1.bed', 'VRN5@Before_cold@VRN5-YFP-NV-rep2.bed', 'VRN5@Before_cold@VRN5-YFP-NV-rep3.bed'], 'VIN3@Cold': ['VIN3@Cold@VIN3-eGFP-6WT0-rep1.bed', 'VIN3@Cold@VIN3-eGFP-6WT0-rep2.bed', 'VIN3@Cold@VIN3-eGFP-6WT0-rep3.bed'], 'VRN5@Control': ['VRN5@Control@ColFRI-6WT0-For-GFP-ColFR-Rep1.bed', 'VRN5@Control@ColFRI-NV-IP-For-GFP-ColFR-Rep2.bed', 'VRN5@Control@ColFRI-6WT0-For-GFP-ColFR-Rep2.bed', 'VRN5@Control@ColFRI-NV-IP-For-GFP-ColFR-Rep1.bed'], 'VEL1@Control': ['VEL1@Control@ColFRI-NV-IP-for-ColFRI-FLAG-Rep1.bed', 'VEL1@Control@ColFRI-NV-IP-for-ColFRI-FLAG-Rep2.bed', 'VEL1@Control@ColFRI-6WT0-for-ColFRI-FLAG-Rep1.bed'], 'VIN3@Before_cold': ['VIN3@Before_cold@VIN3-eGFP-NV-rep1.bed', 'VIN3@Before_cold@VIN3-eGFP-NV-rep2.bed'], 'VEL1@Cold': ['VEL1@Cold@VEL1-FLAG-6WT0-rep2.bed', 'VEL1@Cold@VEL1-FLAG-6WT0-rep3.bed', 'VEL1@Cold@VEL1-FLAG-6WT0-rep1.bed']
}


prot = 'VEL1'
#----------------------

trt_files = mega[prot + '@' + 'Before_cold']  +  mega[prot + '@' + 'Cold'] #
control_files = mega[prot + '@Control']  # Note vin3 used vrn5 controls

for g in trt_files:
  print(g)
  assert os.path.isfile(g) 
  with open('BLACK-PEAKS/' + g ,'w') as outf:    
   for  cfile in  control_files:
     cmd = ['bedtools',  'intersect', '-a', g , '-b',  cfile]
     p = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)
     for line in p.stdout:
        pipe_out = line.strip() + '\t@' + cfile[:-4]
        outf.write(pipe_out + '\n') 

print ('trt_files = ', trt_files)
print ('ctr_files = ', control_files)
print ('DONE')

"""
singularity exec /hpc-home/cheemaj/BUILD/PYBEDTOOLS/pybed.simg bedtools intersect -a VIN3GFP_IP1.bed -b TAIR10_GFF3_genes_only_padded_1K.gff

"""

