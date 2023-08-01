singularity exec ~/BUILD/DEEPTOOLS/deeptools.sif     plotProfile  --plotHeight 14 --plotWidth 12 --yAxisLabel "RPGC" -m mega100_clf_swn.mat.gz  --plotFileFormat pdf  -out bwa-nodup-mega-per-group-rgb-100-profile.pdf   --numPlotsPerRow 1  --plotTitle "100bp resolution" --outFileNameData MATRIX100P/myProfile100bin.tab   --perGroup   --colors "#9f6867" "#c39d9b" "#e6d4d3" "#eee2e2" "#949418" "#c8c385" "#d2cd99" "#eeebd5" "#007f9b" "#8db7c8" "#c6dbe3" "#d9e7ec" "#FFF200FF" "#A2FF00FF" 

echo DONE

