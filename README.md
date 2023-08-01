# VEL-ChIPseq
VRN5 and VIN3/VEL1 ChIP-seq study and the associated scripts.
Mathias (Dean lab)



# Raw reads data
The single end fastq files are deposited to the SRA archived as `BioProject: PRJNA973989`
titled `Functional specification of VEL accessory proteins in Arabidopsis Polycomb silencing`


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



CLF and SWN 
-----------

```
GSM2916533 	CLF-GFP Rep1
GSM2916534 	CLF-GFP Rep2
GSM2916535 	SWN-GFP Rep1
GSM2916536 	SWN-GFP Rep2
GSM2916537 	35S_GFP (input)
```

- Shu J, Chen C, Thapa RK, Bian S et al. Genome-wide occupancy of histone H3K27 methyltransferases CURLY LEAF and SWINGER in Arabidopsis seedlings. Plant Direct 2019 Jan;3(1):e00100. PMID: 31245749
-	Shu, J, Chen, C, Thapa, RK, et al. Genome-wide occupancy of histone H3K27 methyltransferases CURLY LEAF and SWINGER in Arabidopsis seedlings. Plant Direct. 2019; 3: 1-14.

```

# CLF and SWN 
GSM2916533      CLF-GFP Rep1               SRX3544214 (GSM2916533: CLF-GFP Rep1; Arabidopsis thaliana; ChIP-Seq)
GSM2916534      CLF-GFP Rep2               SRX3544215 

GSM2916535      SWN-GFP Rep1               SRX3544216 
GSM2916536      SWN-GFP Rep2               SRX3544217

GSM2916537      35S_GFP (input) [control]  SRX3544218


PRJNA429247     SAMN08332084    SRX3544214      SRR6453472      3702    Arabidopsis thaliana    ftp.sra.ebi.ac.uk/vol1/fastq/SRR645/002/SRR6453472/SRR6453472.fastq.gz          ftp.sra.ebi.ac.uk/vol1/srr/SRR645/002/SRR6453472
PRJNA429247     SAMN08332083    SRX3544215      SRR6453473      3702    Arabidopsis thaliana    ftp.sra.ebi.ac.uk/vol1/fastq/SRR645/003/SRR6453473/SRR6453473.fastq.gz          ftp.sra.ebi.ac.uk/vol1/srr/SRR645/003/SRR6453473
PRJNA429247     SAMN08332082    SRX3544216      SRR6453474      3702    Arabidopsis thaliana    ftp.sra.ebi.ac.uk/vol1/fastq/SRR645/004/SRR6453474/SRR6453474.fastq.gz          ftp.sra.ebi.ac.uk/vol1/srr/SRR645/004/SRR6453474
PRJNA429247     SAMN08332081    SRX3544217      SRR6453475      3702    Arabidopsis thaliana    ftp.sra.ebi.ac.uk/vol1/fastq/SRR645/005/SRR6453475/SRR6453475.fastq.gz          ftp.sra.ebi.ac.uk/vol1/srr/SRR645/005/SRR6453475
PRJNA429247     SAMN08332080    SRX3544218      SRR6453476      3702    Arabidopsis thaliana    ftp.sra.ebi.ac.uk/vol1/fastq/SRR645/006/SRR6453476/SRR6453476.fastq.gz          ftp.sra.ebi.ac.uk/vol1/srr/SRR645/006/SRR6453476

srr2sample = {
  'SRR6453472' : 'CLF-GFP-Rep1',
  'SRR6453473' : 'CLF-GFP-Rep2',    
  'SRR6453474' : 'SWN-GFP-Rep1',
  'SRR6453475' : 'SWN-GFP-Rep2',
  'SRR6453476' : '35S_GFP_input_control',
}

```




- Raw reads from the Yuan et al(2021), where the 14-day-old seedling of VAL1 and VAL2 ChIP-seq, and 14-day-old seedling of H3K27me3 ChIP-seq of WT and val1val2 tp evidence extensive genome-wide interaction between VAL1/2 and PRC2.
- Yuan L, Song X, Zhang L, Yu Y et al. The transcriptional repressors VAL1 and VAL2 recruit PRC2 for genome-wide Polycomb silencing in Arabidopsis. Nucleic Acids Res 2021 Jan 11;49(1):98-113. PMID: 33270882(https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE145387)

```python
	
GSM4317615 	VAL1-GFP-val1-1
GSM4317616 	VAL1-GFP-val1-2
GSM4317617 	VAL1-GFP-val1-input

GSM4317618 	VAL2-GFP-val2-1
GSM4317619 	VAL2-GFP-val2-2
GSM4317620 	VAL2-GFP-val2-input

GSM4317621 	Col-0-1-input
GSM4317622 	Col-0-H3K27me3-1
GSM4317623 	Col-0-H3K27me3-2

GSM4317624 	val1val2-1-input
GSM4317625 	val1val2-H3K27me3-1
GSM4317626 	val1val2-H3K27me3-2

Relations
BioProject 	PRJNA607059
SRA 	SRP249704

```

Methods 
---------

- Raw reads as fastq files can be downloaded from the SRA archive, file names and the samples named are under `metadata-13351040-submitted.tsv`
- Files are downloaded to a directory and also the raw reads from the published above.
- Fastqc-0.11.3 was run on each fastq file and the read were cleaned using `fastp`

```bash
# Download fastq files as under 
metadata-13351040-submitted.tsv (see column filename in this tab delimited file)

# others raw reads
[cheemaj@NBI-HPC interactive rename]$ pwd
/jic/scratch/groups/Caroline-Dean/jitender/mathias/swn-clf-val1-mapping/FQ/clean/rename
[cheemaj@NBI-HPC interactive rename]$ ls -1
40V_H3K27_me3_rep2_1.fq.gz
40V_H3K27_me3_rep2_2.fq.gz
40V_input_control_1.fq.gz
40V_input_control_2.fq.gz
H3K27me3_NV_1_1.fq.gz
H3K27me3_NV_1_2.fq.gz
H3K27me3_NV_2_1.fq.gz
H3K27me3_NV_2_2.fq.gz
NV_input_control_1.fq.gz
NV_input_control_2.fq.gz
VAL1-GFP-val1-input-control_1.fq.gz
VAL1-GFP-val1-input-control_2.fq.gz
VAL1-GFP-val1-Rep1_1.fq.gz
VAL1-GFP-val1-Rep1_2.fq.gz
VAL1-GFP-val1-Rep2_1.fq.gz
VAL1-GFP-val1-Rep2_2.fq.gz
[cheemaj@NBI-HPC interactive rename]$

# read trimming and cleaning for SE reads were done
singularity exec ~/BUILD/FASTP/fastp.simg fastp   --thread 8    --html=SRR6453474.html      -i SRR6453474.fastq.gz    -o   clean/SRR6453474.fastq.gz

# read cleaning for PE was  done using the following 
singularity exec /hpc-home/cheemaj/BUILD/FASTP/fastp.simg fastp   --thread 8  --detect_adapter_for_pe   --html=SRR8955909.html      -i SRR8955909_1.fastq.gz  -I  SRR8955909_2.fastq.gz -o   clean/SRR8955909_1.fastq.gz -O clean/SRR8955909_2.fastq.gz 

```
  



