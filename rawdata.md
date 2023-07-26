
- Raw reads were downloaded from the SRA archives paired ends fastq
- Fastp cleaned reads and renamed according to the following naming

```python
srr2sample_pe = {
##
  'SRR11095962' :  'VAL1-GFP-val1-Rep1',
  'SRR11095963' :  'VAL1-GFP-val1-Rep2', 
  'SRR11095964' :  'VAL1-GFP-val1-input-control',   
 
# gene list by our method  genes from peaks common2:
  'SRR8955899' : 'H3K27me3_NV_1',  # 32.5 reads duplicates     --> 
  'SRR8955908' : 'H3K27me3_NV_2',  # 57.4 reads duplicates

  'SRR8955896' : 'NV_input_control',

#  analysis gene list from from rep2 
  'SRR8955909' : '40V_H3K27_me3_rep2', 
  'SRR8955897' : '40V_input_control',

}
for srr, bio_name in srr2sample_pe.items():
    print 'cp ' +  srr + '_1.fastq.gz'  +  ' rename/' + bio_name + '_1.fq.gz'
    print 'cp ' +  srr + '_2.fastq.gz'  +  ' rename/' + bio_name + '_2.fq.gz'

[cheemaj@NBI-HPC interactive rename]$ pwd
/jic/scratch/groups/Caroline-Dean/jitender/mathias/swn-clf-val1-mapping/FQ/clean/rename
[cheemaj@NBI-HPC interactive rename]$ ls
40V_H3K27_me3_rep2_1.fq.gz  40V_input_control_2.fq.gz  H3K27me3_NV_2_1.fq.gz     NV_input_control_2.fq.gz             VAL1-GFP-val1-Rep1_1.fq.gz  VAL1-GFP-val1-Rep2_2.
40V_H3K27_me3_rep2_2.fq.gz  H3K27me3_NV_1_1.fq.gz      H3K27me3_NV_2_2.fq.gz     VAL1-GFP-val1-input-control_1.fq.gz  VAL1-GFP-val1-Rep1_2.fq.gz
40V_input_control_1.fq.gz   H3K27me3_NV_1_2.fq.gz      NV_input_control_1.fq.gz  VAL1-GFP-val1-input-control_2.fq.gz  VAL1-GFP-val1-Rep2_1.fq.gz
[cheemaj@NBI-HPC interactive rename]$ 
```
