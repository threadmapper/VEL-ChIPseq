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

