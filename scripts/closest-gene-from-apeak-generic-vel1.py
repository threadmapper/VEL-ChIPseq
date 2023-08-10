"""

We get the list of gene within 1KB of a peak submit
 Note: We already picked the TSS site or chosen by a strand
 -  We sort by distance and keep the nearest 

Given the TSS and TES coordinates by strand [tss-test-from-exons-gene.bed]:

Chr1    3630    5899    AT1G01010       0       +
Chr1    5927    8737    AT1G01020       0       -
Chr1    11648   13714   AT1G01030       0       -
Chr1    23145   31227   AT1G01040       0       +

we picked the reference point [TSS-genes.bed]:

Chr1    3630    3631    AT1G01010       0       +
Chr1    8736    8737    AT1G01020       0       -
Chr1    13713   13714   AT1G01030       0       -
Chr1    23145   23146   AT1G01040       0       +

and then we compare point to point distances between a summit and a TSS

"""

import glob
from collections import defaultdict

if __name__ == '__main__':

    for trt_bed in ['VEL1@Before_cold@VEL1-FLAG-NV-rep1.bed', 'VEL1@Before_cold@VEL1-FLAG-NV-rep2.bed',
                    'VEL1@Before_cold@VEL1-FLAG-NV-rep3.bed', 'VEL1@Cold@VEL1-FLAG-6WT0-rep1.bed',
                    'VEL1@Cold@VEL1-FLAG-6WT0-rep2.bed', 'VEL1@Cold@VEL1-FLAG-6WT0-rep3.bed']:

        print('sample_bed: ', trt_bed)
        trt = 'genes_summit-f_s_' + trt_bed

        all_genes_within1KB_csv = trt[:-4] + '-all_genes_within1KB.csv'
        dist_all_genes_within1KB_csv = trt[:-4] + '-dist_all_genes_within1KB.csv'
        winner_gene_list_csv = trt[:-4] + '-winner_gene_list.csv'
        uniq_closest_genes_across_peaks_csv = trt[:-4] + '-nearest1KB-genes-unique_genelist.csv'

        hits = defaultdict(list)
        uniq_genes = set()
        with open(trt) as inp:
            gene_names_uniq = set()
            for line in inp:
                A = line.strip().split()
                head = ['chrom', 'p_beg', 'p_end', 'peak_name', 'summit_score', 'gene_chrom', 'g_beg', 'g_end', 'gene',
                        'zero', 'strand', 'summit_file_name']
                assert len(A) == len(head)
                d = dict(zip(head, A))
                assert d['chrom'] == d['gene_chrom']

                peak = d['peak_name']  # peak name
                p_beg, p_end = int(d['p_beg']), int(d['p_end'])
                g_beg, g_end = int(d['g_beg']), int(d['g_end'])

                dist = abs(p_beg - g_beg)  # this a single coord
                # dist1 = abs(p_end - g_end) # this a single coord
                # assert  dist == dist1
                assert dist <= 1000, ' more than 1KB part'
                hits[peak].append([dist, d['gene']])
                uniq_genes.add(d['gene'])

        print('unique_peaks:', len(hits))  # unique_peaks 7874
        print('uniq_genes:', len(uniq_genes))

        with open(all_genes_within1KB_csv, 'w') as outf:
            for g in uniq_genes:
                outf.write(g + '\n')

        with open(dist_all_genes_within1KB_csv, 'w') as outf:
            outf.write(','.join(map(str, ['unique_peak_id', 'dist', 'gene'])) + '\n')
            for p, gene_list in hits.items():
                for dist, g in sorted(gene_list, key=lambda x: x[0]):
                    outf.write(','.join(map(str, [p, dist, g])) + '\n')

        # sorting begins
        popular_peak = {}
        winner_peaks = {}
        uniq_closest_genes_across_peaks = set()
        with open(winner_gene_list_csv, 'w') as outf:
            for p, gene_list in hits.items():
                popular_peak[p] = gene_list
                dist, g = sorted(gene_list, key=lambda x: x[0])[0]  # closest gene
                uniq_closest_genes_across_peaks.add(g)
                outf.write(','.join(map(str, [dist, p, g])) + '\n')
                winner_peaks[p] = g

        print('qualified_peaks: ', len(winner_peaks))
        print('uniq_genes_found_within1KB: ', len(uniq_genes))
        print('uniq_genes_closest_1KB_peaks = ', len(uniq_closest_genes_across_peaks))

        with open(uniq_closest_genes_across_peaks_csv, 'w') as outf:
            for g in uniq_closest_genes_across_peaks:
                outf.write(g + '\n')

        for p, genes in sorted(popular_peak.items(), key=lambda x: len(x[1]), reverse=True):
            print(p, genes)

        print('-'*80)


"""
sample_bed:  VEL1@Before_cold@VEL1-FLAG-NV-rep1.bed
unique_peaks: 7874
uniq_genes: 9066
qualified_peaks:  7874
uniq_genes_found_within1KB:  9066
uniq_genes_closest_1KB_peaks =  7447

popular peaks with many genes:
                                                      *               
VEL1-FLAG-NV-rep1_peak_7034 [[93, 'AT1G79280'], [8, 'AT1G79290'], [609, 'AT1G79300'], [812, 'AT1G79310']]
                                                                           *
VEL1-FLAG-NV-rep1_peak_7035 [[774, 'AT1G79280'], [673, 'AT1G79290'], [72, 'AT1G79300'], [131, 'AT1G79310']]

VEL1-FLAG-NV-rep1_peak_9767 [[315, 'AT2G36145'], [6, 'AT2G36140'], [722, 'AT2G36150'], [962, 'AT2G36160']]

VEL1-FLAG-NV-rep1_peak_20794 [[407, 'AT5G02810'], [313, 'AT5G02811'], [97, 'AT5G02815'], [174, 'AT5G02820']]

VEL1-FLAG-NV-rep1_peak_21467 [[59, 'AT5G09461'], [59, 'AT5G09463'], [59, 'AT5G09460'], [59, 'AT5G09462']]
VEL1-FLAG-NV-rep1_peak_26570 [[973, 'AT5G66210'], [774, 'AT5G66211'], [548, 'AT5G66230'], [573, 'AT5G66220']]
VEL1-FLAG-NV-rep1_peak_113 [[629, 'AT1G01880'], [391, 'AT1G01890'], [578, 'AT1G01900']]
VEL1-FLAG-NV-rep1_peak_489 [[107, 'AT1G05385'], [20, 'AT1G05390'], [248, 'AT1G05400']]
VEL1-FLAG-NV-rep1_peak_1024 [[527, 'AT1G10430'], [96, 'AT1G10440'], [620, 'AT1G10450']]
VEL1-FLAG-NV-rep1_peak_1093 [[606, 'AT1G11000'], [22, 'AT1G11010'], [106, 'AT1G11020']]
VEL1-FLAG-NV-rep1_peak_1167 [[289, 'AT1G11630'], [4, 'AT1G11640'], [78, 'AT1G11650']]
VEL1-FLAG-NV-rep1_peak_1689 [[123, 'AT1G15880'], [21, 'AT1G15885'], [861, 'AT1G15890']]
VEL1-FLAG-NV-rep1_peak_1828 [[65, 'AT1G17560'], [0, 'AT1G17570'], [546, 'AT1G17580']]
VEL1-FLAG-NV-rep1_peak_1837 [[99, 'AT1G17660'], [99, 'AT1G17670'], [158, 'AT1G17680']]
VEL1-FLAG-NV-rep1_peak_1918 [[92, 'AT1G18415'], [10, 'AT1G18430'], [220, 'AT1G18440']]

"""
