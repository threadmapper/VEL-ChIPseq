# VEL-ChIPseq
VRN5 and VIN3/VEL1 ChIP-seq study and the associated scripts.
Mathias (Dean lab)



# Raw reads data
The single end fastq files are deposited to the SRA archived as `BioProject: PRJNA973989`
titled `Functional specification of VEL accessory proteins in Arabidopsis Polycomb silencing`


```python
[cheemaj@NBI-HPC interactive UPDATED]$ pwd
cheemaj/scratch/scratch-work/jitender/mathias/RAW-READS/UPDATED
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
cheemaj/scratch/scratch-work/jitender/mathias/RAW-READS/FIXED-UPDATED
[cheemaj@NBI-HPC interactive FIXED-UPDATED]$ ls -1 *.py
file-exists-checks.py
rename-fastq-file-tobiological-names-using-mathias-description.py
[cheemaj@NBI-HPC interactive FIXED-UPDATED]$

[cheemaj@NBI-HPC interactive MATHIAS-META-DATA]$ pwd
cheemaj/scratch/scratch-work/jitender/mathias/RAW-READS/FIXED-UPDATED/MATHIAS-META-DATA
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
- FastQC v0.11.9 were used to check the stats before and after read cleaning
- We run on each fastq file and the read were cleaned using `fastp`(fastp 0.20.1; singularity definition file under the containers subdirectory)
- Both fastqc and fastp were ran through singularity container(definition files are available under the containers subdirectory)

```bash
# Download fastq files as under 
metadata-13351040-submitted.tsv (see column filename in this tab delimited file)

# others raw reads
[cheemaj@NBI-HPC interactive rename]$ pwd
CD/jitender/mathias/swn-clf-val1-mapping/FQ/clean/rename
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

Mapping clean to TAIR10 reference 
---------------------------------

- We mapped to the tair10 genome (chromsomal) using `bwa-0.5.7` with slightly relaxed or the parameters `bwa aln -t 8  -l 25  -k 2  -n 5`
- the resulting sam were converted to BAM via samtools-1.6 
- BAM files were further processed at various stages with a combination of sambamba-1.0.0 and the samtools for further visualisation 


```bash
singularity exec ~/BUILD/VERN/idr_bwa.sif samtools flagstat ../BASE.bam > BASE.bam.stat 

# Filtering and sorting the reads
singularity exec ~/BUILD/VERN/idr_bwa.sif samtools view -@ 8  -F 772  -b ../BASE.bam  Chr1 Chr2 Chr3 Chr4 Chr5 -o FILTER/BASE.filter_unsorted.bam
singularity exec ~/BUILD/VERN/idr_bwa.sif samtools sort -o FILTER/BASE.filter.bam  FILTER/BASE.filter_unsorted.bam
# Index filtered reads
singularity exec ~/BUILD/VERN/idr_bwa.sif samtools  index    FILTER/BASE.filter.bam
# keep the stats
singularity exec ~/BUILD/VERN/idr_bwa.sif samtools  flagstat FILTER/BASE.filter.bam  > FILTER/BASE.filter.bam.stat

# mark duplicates with picard
singularity exec ~/BUILD/VERN/idr_bwa.sif picard MarkDuplicates I=FILTER/BASE.filter.bam O=FILTER/BASE.dupmark_unsorted.bam  M=FILTER/BASE.dup.qc  VALIDATION_STRINGENCY=LENIENT  REMOVE_DUPLICATES=false ASSUME_SORTED=true

# sort reads after marking the duplicates
singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools sort -o FILTER/BASE.dupmark.bam  FILTER/BASE.dupmark_unsorted.bam
# index the sorted reads
singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools index    FILTER/BASE.dupmark.bam
singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools flagstat FILTER/BASE.dupmark.bam > FILTER/BASE.dupmark.bam.stat

# remove duplicates
singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools view -@ 8  -F 1796  -b FILTER/BASE.dupmark.bam -o  FILTER/BASE.dupmark.nodup_unsorted.bam
singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools sort -o FINAL_BAM/BASE.bam  FILTER/BASE.dupmark.nodup_unsorted.bam
# index unique reads
singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools  index     FINAL_BAM/BASE.bam
singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools  flagstat  FINAL_BAM/BASE.bam >  FINAL_BAM/BASE.bam.stat

# for visualisation of read mapping distribution across TSS and TES flanks

(a) replication were merged with bamtools-2.5.2,  BASE.txt;containing the files names from the corresponding replicates
 singularity exec ~/BUILD/VERN/idr_bwa.sif  bamtools merge -list BASE.txt  -out MERGED/BASE.bam
 singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools index    MERGED/BASE.bam
 singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools flagstat  MERGED/BASE.bam > MERGED/BASE.bam.stat

(b) Bigwig file normalised for RPGC metric was generated using bamCoverage-3.5.1; 
 mkdir -p BW100
 singularity exec ~/BUILD/DEEPTOOLS/deeptools.sif  bamCoverage --bam BASE.bam  -o BW100/BASE.bw  --binSize 100   --normalizeUsing RPGC    --effectiveGenomeSize 119146348  --filterRNAstrand forward  --numberOfProcessors 8

# all the resulting  bw were scaled using the scalregions command:
singularity exec ~/BUILD/DEEPTOOLS/deeptools.sif   computeMatrix scale-regions   --scoreFileName VEL1-FLAG-6WT0.bw VEL1-FLAG-6WT0-input.bw VEL1-FLAG-NV.bw VEL1-FLAG-NV-input.bw VIN3-eGFP-6WT0.bw VIN3-eGFP-6WT0-input.bw VIN3-eGFP-NV.bw VIN3-eGFP-NV-input.bw VRN5-YFP-6WT0.bw VRN5-YFP-6WT0-input.bw VRN5-YFP-NV.bw VRN5-YFP-NV-input.bw CLF-GFP.bw SWN-GFP.bw  --samplesLabel vel1_cold-IP vel1_cold-Input vel1_nv-IP vel1_nv-Input vin3_cold-IP vin3_cold-Input vin3_nv-IP vin3_nv-Input vrn5_cold-IP vrn5_cold-Input vrn5_nv-IP vrn5_nv-Input CLF-GFP SWN-GFP  -R tss-test-from-exons-gene.bed  --beforeRegionStartLength 3000     --regionBodyLength 5000  --afterRegionStartLength 3000   --skipZeros -o mega100_clf_swn.mat.gz   --numberOfProcessors 16 

# using the shades of following colours pallete
singularity exec ~/BUILD/DEEPTOOLS/deeptools.sif     plotProfile  --plotHeight 14 --plotWidth 12 --yAxisLabel "RPGC" -m mega100_clf_swn.mat.gz  --plotFileFormat pdf  -out bwa-nodup-mega-per-group-rgb-100-profile.pdf    --numPlotsPerRow 1  --plotTitle "100bp resolution" --outFileNameData MATRIX100P/myProfile100bin.tab   --perGroup   --colors "#9f6867" "#c39d9b" "#e6d4d3" "#eee2e2" "#949418" "#c8c385" "#d2cd99" "#eeebd5" "#007f9b" "#8db7c8" "#c6dbe3" "#d9e7ec" "#FFF200FF" "#A2FF00FF" 


```


Effective Genome size
----------------------

- We find the effective genome size using epic
- We find kmers size to 50 

Mapping and Peak calling
-------------------------


We downloaded the raw reads from SRA archive and after cleaning the read with fastp we mapped to TAIR10 genome using bwa (version 0.5.7) with the parameters ‘bwa aln -q 5 -l 32 -k 2’ as recommended by Encode guidelines. The mapping result were sorted, filtered and merged using samtools(version 1.17), sambamba (v1.0.0) and bamtools (v2.5.2). Duplicate reads were marked using picard (v3.0.0).   The normalized coverage was extracted using bamCoverage  and computeMatrix from deepTools (v3.5.1). The uniquely and without PCR reads were further used for the peak calling with macs3 (v3.0.0a7) using the parameters ‘callpeak -f BAM -g 113582948  -q 0.05  --bdg  --nomodel’. The resulting peaks were further filtered by different cutoffs. Effective genome size was found using the epic-effective utility from epic (v0.2.12).


Mapping 
---------

- BWA aln was used
- Using 8 cpu cores

````
step 1: Mapping was done

#aln -t using 8 threads
# -l 32        seed length
# -k 2         mismatches allowed in seed
# -q 5
# these parameters are from Encode recommendation

mkdir -p BAM

singularity exec ~/BUILD/VERN/idr_bwa.sif bwa aln -q 5 -l 32 -k 2 -t 8 ../ref/TAIR10Genome.fasta  ../sra/VEL1-FLAG-NV-input-rep2.fq.gz  > VEL1-FLAG-NV-input-rep2.sai
 
sleep 2s

#for bwa samse: we are building sam
singularity exec ~/BUILD/VERN/idr_bwa.sif bwa samse ../ref/TAIR10Genome.fasta  VEL1-FLAG-NV-input-rep2.sai ../sra/VEL1-FLAG-NV-input-rep2.fq.gz  > VEL1-FLAG-NV-input-rep2.sam

singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools view -bt ../ref/TAIR10Genome.fasta  -o VEL1-FLAG-NV-input-rep2_unsorted.bam  VEL1-FLAG-NV-input-rep2.sam

singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools sort -@ 8  -o  BAM/VEL1-FLAG-NV-input-rep2.bam  VEL1-FLAG-NV-input-rep2_unsorted.bam
 
singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools index    BAM/VEL1-FLAG-NV-input-rep2.bam 

singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools flagstat BAM/VEL1-FLAG-NV-input-rep2.bam  >  VEL1-FLAG-NV-input-rep2.stat

# BAM Filtering 


mkdir -p FINAL_BAM 


singularity exec ~/BUILD/VERN/idr_bwa.sif sambamba view -t 8 -h -f bam -F "mapping_quality >= 1 and not (unmapped or secondary_alignment) and not ([XA] != null or [SA] != null)" ../BAM/VEL1-FLAG-NV-input-rep2.bam -o VEL1-FLAG-NV-input-rep2_uniq.bam
singularity exec ~/BUILD/VERN/idr_bwa.sif samtools index VEL1-FLAG-NV-input-rep2_uniq.bam 
singularity exec ~/BUILD/VERN/idr_bwa.sif samtools flagstat VEL1-FLAG-NV-input-rep2_uniq.bam  > VEL1-FLAG-NV-input-rep2_uniq.stat


# remove reads without MAPQ>=30
singularity exec ~/BUILD/VERN/idr_bwa.sif samtools view -@ 8  -F 772  -b VEL1-FLAG-NV-input-rep2_uniq.bam  Chr1 Chr2 Chr3 Chr4 Chr5 -o FILTER/VEL1-FLAG-NV-input-rep2.filter_unsorted.bam
singularity exec ~/BUILD/VERN/idr_bwa.sif samtools sort -@ 8  -o FILTER/VEL1-FLAG-NV-input-rep2.filter.bam  FILTER/VEL1-FLAG-NV-input-rep2.filter_unsorted.bam

# Index filtered reads
singularity exec ~/BUILD/VERN/idr_bwa.sif samtools  index    FILTER/VEL1-FLAG-NV-input-rep2.filter.bam
singularity exec ~/BUILD/VERN/idr_bwa.sif samtools  flagstat FILTER/VEL1-FLAG-NV-input-rep2.filter.bam  > FILTER/VEL1-FLAG-NV-input-rep2.filter.bam.stat



sleep 5s

# mark duplicates with picard
singularity exec ~/BUILD/VERN/idr_bwa.sif picard MarkDuplicates I=FILTER/VEL1-FLAG-NV-input-rep2.filter.bam O=FILTER/VEL1-FLAG-NV-input-rep2.dupmark_unsorted.bam  M=FILTER/VEL1-FLAG-NV-input-rep2.dup.qc  VALIDATION_STRINGENCY=LENIENT  REMOVE_DUPLICATES=false ASSUME_SORTED=true

sleep 5s

# sort reads after marking the duplicates
singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools sort -@ 8 -o FILTER/VEL1-FLAG-NV-input-rep2.dupmark.bam  FILTER/VEL1-FLAG-NV-input-rep2.dupmark_unsorted.bam

# index the sorted reads
singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools index    FILTER/VEL1-FLAG-NV-input-rep2.dupmark.bam
singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools flagstat FILTER/VEL1-FLAG-NV-input-rep2.dupmark.bam > FILTER/VEL1-FLAG-NV-input-rep2.dupmark.bam.stat


# remove duplicates
singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools view -@ 8  -F 1796  -b FILTER/VEL1-FLAG-NV-input-rep2.dupmark.bam -o  FILTER/VEL1-FLAG-NV-input-rep2.dupmark.nodup_unsorted.bam

singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools sort -@ 8  -o FINAL_BAM/VEL1-FLAG-NV-input-rep2.bam  FILTER/VEL1-FLAG-NV-input-rep2.dupmark.nodup_unsorted.bam

# index unique reads
singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools  index     FINAL_BAM/VEL1-FLAG-NV-input-rep2.bam
singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools  flagstat  FINAL_BAM/VEL1-FLAG-NV-input-rep2.bam >  FINAL_BAM/VEL1-FLAG-NV-input-rep2.bam.stat


# Following lines were used  to cehck the output

"""
Check the unique named reads
samtools view  35S_GFP_input_control.bam | cut -f 1  > read_names.txt
"""
from collections import Counter

red = Counter()
with open('read_names.txt') as inp:
    for line in inp:
        red[line.strip()] += 1

print(red.most_common(10))
```

Metaplot with merged BAMs
-------------------------

- BAM files were merged with `bamtools`
- The corresponding replicates were species in a flat txt file
- Merged files were normalise for RPGC with respect to effective genome size
- The binsize was fixed to 100

```
mkdir -p MERGED
singularity exec ~/BUILD/VERN/idr_bwa.sif  bamtools merge -list VIN3-eGFP-6WT0-input.txt  -out MERGED/VIN3-eGFP-6WT0-input.bam
singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools index  MERGED/VIN3-eGFP-6WT0-input.bam

# geneerated bedgraph files for each replicate
mkdir -p BW100
# TAIR10Genome.fasta Chroms + ChrC + ChrM = 119668634 --> 113582948  
singularity exec ~/BUILD/DEEPTOOLS/deeptools.sif  bamCoverage --bam BASE.bam  -o BW100/BASE.bw  --binSize 100   --normalizeUsing RPGC    --effectiveGenomeSize 113582948  --filterRNAstrand forward  --numberOfProcessors 8

singularity exec ~/BUILD/DEEPTOOLS/deeptools.sif   computeMatrix scale-regions   --scoreFileName VEL1-FLAG-6WT0.bw VEL1-FLAG-6WT0-input.bw VEL1-FLAG-NV.bw VEL1-FLAG-NV-input.bw VIN3-eGFP-6WT0.bw VIN3-eGFP-6WT0-input.bw VIN3-eGFP-NV.bw VIN3-eGFP-NV-input.bw VRN5-YFP-6WT0.bw VRN5-YFP-6WT0-input.bw VRN5-YFP-NV.bw VRN5-YFP-NV-input.bw CLF-GFP.bw SWN-GFP.bw  --samplesLabel vel1_cold-IP vel1_cold-Input vel1_nv-IP vel1_nv-Input vin3_cold-IP vin3_cold-Input vin3_nv-IP vin3_nv-Input vrn5_cold-IP vrn5_cold-Input vrn5_nv-IP vrn5_nv-Input CLF-GFP SWN-GFP  -R tss-test-from-exons-gene.bed  --beforeRegionStartLength 3000     --regionBodyLength 5000  --afterRegionStartLength 3000   --skipZeros -o mega100_clf_swn.mat.gz   --numberOfProcessors 16
# profile was plotted
singularity exec ~/BUILD/DEEPTOOLS/deeptools.sif     plotProfile  --plotHeight 14 --plotWidth 12 --yAxisLabel "RPGC" -m mega100_clf_swn.mat.gz  --plotFileFormat pdf  -out bwa-nodup-mega-per-group-rgb-100-profile.pdf   --numPlotsPerRow 1  --plotTitle "100bp resolution" --outFileNameData bwa-nodup-mega-profile-100bin.tab   --perGroup   --colors "#9f6867" "#c39d9b" "#e6d4d3" "#eee2e2" "#949418" "#c8c385" "#d2cd99" "#eeebd5" "#007f9b" "#8db7c8" "#c6dbe3" "#d9e7ec" "#FFF200FF" "#A2FF00FF"

# to generate "bwa-nodup-mega-per-group-rgb-100-profile-all-reads.pdf"

```

Coverage sampling
------------------

- BAM files were randomly sampled(downsampled) in order for an easy comparison
- This as done as QC step and also to check the robustness of profile 

```python

# see: https://www.biostars.org/p/9485840/
reads=5000000
bam=../ColFRI-NV-IP-For-GFP-ColFR.bam
fraction=$(singularity exec ~/BUILD/VERN/idr_bwa.sif samtools idxstats $bam | cut -f3 | awk -v ct=$reads 'BEGIN {total=0} {total += $1} END {print ct/total}')
echo $fraction

singularity exec ~/BUILD/VERN/idr_bwa.sif samtools  view -b -s ${fraction} ${bam} > ColFRI-NV-IP-For-GFP-ColFR_unsorted.bam

singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools  sort -o ColFRI-NV-IP-For-GFP-ColFR-sampled.bam  ColFRI-NV-IP-For-GFP-ColFR_unsorted.bam
singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools  index      ColFRI-NV-IP-For-GFP-ColFR-sampled.bam
singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools  flagstat   ColFRI-NV-IP-For-GFP-ColFR-sampled.bam >   ColFRI-NV-IP-For-GFP-ColFR-sampled.bam.stat

```

PEAK calling
-------------

- We called peak on each pair of bam files
- The default parameters were used

```
Typical run:

mkdir -p CLF-GFP-Rep1
singularity exec /hpc-home/cheemaj/BUILD/MACS3/macs3_a7.simg macs3  callpeak -t ../CLF-GFP-Rep1.bam  -c  ../35S_GFP_input_control.bam  -f BAM -g 113582948  -q 0.05  --bdg --outdir CLF-GFP-Rep1  -n CLF-GFP-Rep1  --nomodel   

The resulting narrow peak files were renamed to the biological simpler names using the naming "protein-conditions-treatment-input-reps.tab"

```

PEAK filtering
---------------

- We drop a peak it appears in more than one control samples using see for ex. `black-list-by-control-peaks-VEL1.py` and `survived-peaks-not-more-than-one-control-VEL1.py`
- The filtered peak were further filtered at various Q score cut off, `gen_peaks_at_thresholds-vel1.py`
- At each cutoff the peaks consensus common regions( or peak segments) were extacted using `bedtools multiinter`

```

```


Peak calling: Histone markers
-----------------------------

- The broad peaks were called for markers and the data was paired end reads
- The rest of processing and  BAM filtering was similar to the narrowpeaks


```
#singularity exec ~/BUILD/VERN/idr_bwa.sif bwa aln -q 5 -l 32 -k 2 -t 8 ../ref/TAIR10Genome.fasta  FASTQ_FWD    > BASE_1.sai
#singularity exec ~/BUILD/VERN/idr_bwa.sif bwa aln -q 5 -l 32 -k 2 -t 8 ../ref/TAIR10Genome.fasta  FASTQ_REV    > BASE_2.sai
 
sleep 2s

#for bwa sampe: we are building sam
singularity exec ~/BUILD/VERN/idr_bwa.sif bwa sampe ../ref/TAIR10Genome.fasta   BASE_1.sai  BASE_2.sai   FASTQ_FWD  FASTQ_REV  > BASE.sam


singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools view -bt ../ref/TAIR10Genome.fasta -o BASE_unsorted.bam  BASE.sam

singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools sort -@ 8  -o  BAM/BASE.bam  BASE_unsorted.bam
 
singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools index    BAM/BASE.bam 

singularity exec ~/BUILD/VERN/idr_bwa.sif  samtools flagstat BAM/BASE.bam  >  BASE.stat

```





