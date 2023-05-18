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

```





