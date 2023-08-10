"""
Major gene if its present in atleast two replicates

"""
import glob
from collections import defaultdict

cluster = glob.glob('*-nearest1KB-genes-unique_genelist.csv')

#1-nearest1KB-genes-unique_genelist.csv

d = defaultdict(list)
for c in cluster:
    d[c[:-42]].append(c)

for k, v in d.items():
    assert len(v)> 1

def read_genes(filer):
    genes = set()
    with open(filer) as inp:
      for line in inp:
          genes.add(line.strip()) 
    return genes                   



for gp, reps in d.items():
    with open('atleast2-' + gp + '.csv', 'w') as outf:
       reps_genes = [ read_genes(filer) for filer in reps]
       union_genes =  list(set().union(*reps_genes))
       for g in union_genes:
           present  = sum([  1  for pool in reps_genes if g in pool])
           if present >= 2: # atleast two
              outf.write(','.join([g, str(present)]) + '\n') 