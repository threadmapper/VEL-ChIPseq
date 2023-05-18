import os

md_orginal = {}
with open('checksums_MLN-suggested-fixed-renamed.csv') as inp:
 next(inp)
 for line in inp:
     mat_name, orig_hash, orig_name, bio_name =  line.strip().split(',')
     md_orginal[bio_name] = orig_hash
     assert os.path.exists(bio_name) 

assert len(md_orginal) == 48


md = {}
with open('md5checks.txt') as inp:
 #next(inp)
 for line in inp:
     m, filer = line.strip().split()
     md[filer] = m 

print len(md)
for s, m in md_orginal.items():
    print s
    print md_orginal[s] 
    print md[s]
    assert md_orginal[s] == md[s]
    
gz_files = set()
with open('sample-sheet-names.txt') as inp:
 next(inp)
 for line in inp:
     gz_files.add( line.strip())

print len(gz_files)#48 

for gz in gz_files:
    if gz in md:
       assert md[gz] == md_orginal[gz], 'Filed' 
    else:
       print 'Missing', gz  #Missing ColFRI-6WT0-for-ColFRI-FLAG-Rep1.fq.gz
