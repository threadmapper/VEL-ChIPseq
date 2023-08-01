#!/bin/bash -e
#SBATCH  --job-name=meg100c35
#SBATCH  -o     meg100c16.out
#SBATCH  -e     meg100c16.err
#SBATCH  --mem  60gb
#SBATCH  -c     16
#SBATCH  -p     jic-a100

mkdir -p MATRIX100P

singularity exec ~/BUILD/DEEPTOOLS/deeptools.sif   computeMatrix scale-regions   --scoreFileName VEL1-FLAG-6WT0.bw VEL1-FLAG-6WT0-input.bw VEL1-FLAG-NV.bw VEL1-FLAG-NV-input.bw VIN3-eGFP-6WT0.bw VIN3-eGFP-6WT0-input.bw VIN3-eGFP-NV.bw VIN3-eGFP-NV-input.bw VRN5-YFP-6WT0.bw VRN5-YFP-6WT0-input.bw VRN5-YFP-NV.bw VRN5-YFP-NV-input.bw CLF-GFP.bw SWN-GFP.bw  --samplesLabel vel1_cold-IP vel1_cold-Input vel1_nv-IP vel1_nv-Input vin3_cold-IP vin3_cold-Input vin3_nv-IP vin3_nv-Input vrn5_cold-IP vrn5_cold-Input vrn5_nv-IP vrn5_nv-Input CLF-GFP SWN-GFP  -R tss-test-from-exons-gene.bed  --beforeRegionStartLength 3000     --regionBodyLength 5000  --afterRegionStartLength 3000   --skipZeros -o mega100_cff_swn.mat.gz   --numberOfProcessors 16 

 

echo DONE

