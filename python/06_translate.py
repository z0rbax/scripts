#!//usr/bin/python3

import argparse,os,sys,csv
'''
parser=argparse.ArgumentParser(
usage='translate.py antibiotics_code.tsv srst2_argannot.tsv output_translated.tsv\n\nThis script translate the srst2_argannot.tsv table to an antibiotic category.')
parser.add_argument("antibiotics_code.tsv", help="path/to/antibiotics_code.tsv file")
parser.add_argument("srst2_argannot.tsv", help="srst2_argannot.tsv file")

args=parser.parse_args()
dirpath = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

if len(sys.argv)==1:
    os.system(dirpath+"/translate.py -h")
    exit(1)
'''
code = {}
with open(sys.argv[1], 'r') as code_table:
    for i in csv.reader(code_table, delimiter='\t'):
        code[i[1]] = i[0]

#print(d)
rsrt_results = {}
with open(sys.argv[2], 'r') as argannotable:
    for k in csv.reader(argannotable, delimiter='\t'):
        rsrt_results[k[0]] = k[1:]

#for gene in sorted(code):
#   print(gene,':',code[gene])

#for genes in sorted(rsrt_results):
#    print(genes,':',rsrt_results[genes])

result = []
for ids in sorted(rsrt_results):
    assignid = {}
    for genes in rsrt_results[ids]:
        for gene_id in sorted(code):
            if genes == gene_id:
                assignid[ids] = code[gene_id]
        #print(assignid)
        result.append(assignid.copy())

#print(result)

super_dict = {}
for x in result:
    for k, v in x.items():
        super_dict.setdefault(k, []).append(v)

#print(super_dict)

#with open('test.txt', 'a') as output:
with open(sys.argv[3], 'a') as output:
    for k, v in sorted(super_dict.items()):
        #print(k + '\t' + ', '.join(v)) #category by gene
        print(k + '\t' + ', '.join(sorted(set(v))), file=output) #only unique categories
