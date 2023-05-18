# VEL-ChIPseq
VRN5 and VIN3/VEL1 ChIP-seq study and the associated scripts.
Mathias (Dean lab)



# Raw reads data
The single end fastq files are deposited to the SRA archived


```python
[cheemaj@NBI-HPC interactive UPDATED]$ pwd
/jic/scratch/groups/Matthew-Hartley/cheemaj/scratch/scratch-work/jitender/mathias/RAW-READS/UPDATED
[cheemaj@NBI-HPC interactive UPDATED]$
## rename the biologial names 
[cheemaj@NBI-HPC interactive UPDATED]$ rankmycode rename-fastq-file-tobiological-names-using-mathias-description.py
-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.41/10, +0.59)
[cheemaj@NBI-HPC interactive UPDATED]$
# generate the renaming script, we are renaming using the copy to keep the original files
[cheemaj@NBI-HPC interactive UPDATED]$ python3  rename-fastq-file-tobiological-names-using-mathias-description.py  > copier.sh
[cheemaj@NBI-HPC interactive UPDATED]$ source copier.sh
```

SRA uploading
--------------

- We uploaded reads to the SRA 
- The source directory was

```python
#
[cheemaj@NBI-HPC interactive FIXED-UPDATED]$ pwd
/jic/scratch/groups/Matthew-Hartley/cheemaj/scratch/scratch-work/jitender/mathias/RAW-READS/FIXED-UPDATED
[cheemaj@NBI-HPC interactive FIXED-UPDATED]$ ls -1 *.py
file-exists-checks.py
rename-fastq-file-tobiological-names-using-mathias-description.py
[cheemaj@NBI-HPC interactive FIXED-UPDATED]$

[cheemaj@NBI-HPC interactive MATHIAS-META-DATA]$ pwd
/jic/scratch/groups/Matthew-Hartley/cheemaj/scratch/scratch-work/jitender/mathias/RAW-READS/FIXED-UPDATED/MATHIAS-META-DATA
[cheemaj@NBI-HPC interactive MATHIAS-META-DATA]$ ls -1
checksums_MLN-suggested-fixed-renamed.csv
checksums_MLN-suggested-fixed-renamed-Formatted.csv
checksums_MLN-suggested-fixed-renamed-Formatted.xlsx  [approved]
ChIP-seq-metadata-only-sheet-upload.xlsx
ChIP-seq-metadata-sheet-upload.xlsx
ChIP-seq metadata sheet.xlsx
generate-meta-data-table
README.md
sample-attributes-Plant.1.0_MLN-added-description.xlsx  [we uploaded this ]
[cheemaj@NBI-HPC interactive MATHIAS-META-DATA]$
```

Mapping read to the genome refernce
-----------------------------------

- We mapped the reads to TAIR10 reference genome
- Indexing and mapping was done using `bwa-0.5.7` and the samtools version(1.6)

```bash
Typical run: 
# mappign output to sai files 
bwa  aln -t 8  -l 25  -k 2  -n 5    tair10-genome.fasta  15_9ColFRINVinp_1.fq.gz    > 15_9ColFRINVinp.sai
# converting to sam 
bwa  samse   tair10-genome.fasta   15_9ColFRINVinp.sai   15_9ColFRINVinp_1.fq.gz    > 15_9ColFRINVinp.sam
# sam to sorted bam   
samtools view -bt tair10-genome.fasta  -o 15_9ColFRINVinp.bam  15_9ColFRINVinp.sam
samtools sort -o sorted-15_9ColFRINVinp.bam  15_9ColFRINVinp.bam
samtools index sorted-15_9ColFRINVinp.bam 

# Mapping stats wer found using  
samtools flagstat sorted-15_9ColFRINVinp.bam 
samtools view -F 0x04 -c sorted-15_9ColFRINVinp.bam 

# Peak calling using macs3 
# ATH tair 10 genome size Genome size tair10-genome.fasta:  119146348
singularity exec macs3_a7.simg macs3  callpeak -t TRT_BAM_FILE  -c  CNTRL_BAM_FILE  -f BAM -g 119146348  -q 0.05  --bdg --outdir BASE  -n BASE  --nomodel  --extsize 180 

# bed graphs summary was generated using deeptools  
singularity exec ~/BUILD/DEEPTOOLS/deeptools.sif   multiBigwigSummary bins --binSize 10  \
 --bwfiles 10_8FRI6WOinput.bw 10_8_FRI_6W0_IP.bw 11_2_VRN5_IP.bw 11_2_VRN5_Input.bw 12_8VEL1NVinput.bw 12_8_VEL1_NV_IP.bw 13_4VIN3GFPinp.bw 13_4_VIN3GFP_IP.bw 15_9ColFRINVinp.bw 15_9_ColFRINVIP.bw 16_9VEL16W0inpu.bw 16_9_VEL16W0_IP.bw 18_6VIN3NVInput.bw 18_6_VIN3_NV_IP.bw 21_4_VRN5_IP.bw 21_4_VRN5_Input.bw 21_8FRINVinput.bw 21_8FRI_NV_IP.bw 21_9FRI6W0input.bw 21_9_FRI_6W0_IP.bw 22_7VIN3NVInput.bw 22_7_VIN3_NV_IP.bw 23_9VEL1NVinput.bw 23_9_VEL1_NV_IP.bw 25_8FRI6W0input.bw 25_8_FRI_6W0_IP.bw 26_7VEL16WOinput.bw 26_7_VEL1_6W0IP.bw 29_5VIN3NVInput.bw 31_7COIFRINVinput.bw 31_7_COIFRI_NV_IP.bw 31_8VEL1NVinput.bw 31_8_VEL1_NV_IP.bw 6_5VRN5NVInput.bw 6_5_VRN5_NV_IP.bw 7_4VRN56W0IP.bw 7_4VRN56W0input.bw 7_4_VRN5_IP.bw 7_4_VRN5_input.bw 7_9VEL16W0input.bw 7_9_VEL1_6W0_IP.bw 8_6VRN5NVInput.bw 8_6_VRN5_NV_IP.bw 9_7VRN5NVInput.bw 9_7_VRN5_NV_IP.bw 9_9FRINVinput.bw 9_9_FRI_NV_IP.bw VIN3GFP_IP_1.bw VIN3GFP_IP_2.bw VIN3GFP_input_1.bw VIN3GFP_input_2.bw \
 --labels 10_8FRI6WOinput 10_8_FRI_6W0_IP 11_2_VRN5_IP 11_2_VRN5_Input 12_8VEL1NVinput 12_8_VEL1_NV_IP 13_4VIN3GFPinp 13_4_VIN3GFP_IP 15_9ColFRINVinp 15_9_ColFRINVIP 16_9VEL16W0inpu 16_9_VEL16W0_IP 18_6VIN3NVInput 18_6_VIN3_NV_IP 21_4_VRN5_IP 21_4_VRN5_Input 21_8FRINVinput 21_8FRI_NV_IP 21_9FRI6W0input 21_9_FRI_6W0_IP 22_7VIN3NVInput 22_7_VIN3_NV_IP 23_9VEL1NVinput 23_9_VEL1_NV_IP 25_8FRI6W0input 25_8_FRI_6W0_IP 26_7VEL16WOinput 26_7_VEL1_6W0IP 29_5VIN3NVInput 31_7COIFRINVinput 31_7_COIFRI_NV_IP 31_8VEL1NVinput 31_8_VEL1_NV_IP 6_5VRN5NVInput 6_5_VRN5_NV_IP 7_4VRN56W0IP 7_4VRN56W0input 7_4_VRN5_IP 7_4_VRN5_input 7_9VEL16W0input 7_9_VEL1_6W0_IP 8_6VRN5NVInput 8_6_VRN5_NV_IP 9_7VRN5NVInput 9_7_VRN5_NV_IP 9_9FRINVinput 9_9_FRI_NV_IP VIN3GFP_IP_1 VIN3GFP_IP_2 VIN3GFP_input_1 VIN3GFP_input_2   \
 --outFileName bin_scoreL.npz --outRawCounts bin_scoreL.txt --numberOfProcessors 16 


```





