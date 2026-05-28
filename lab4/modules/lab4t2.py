from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

def run2(fl):
    container = []

    with open(fl, "r") as file:
        for i in SeqIO.parse(file, "genbank"): # parse through genbank pieces 
            result = gc_fraction(i.seq) #count gc pairs in the sequence
            container.append((i, result)) # id plus gc rate

    container.sort(key=lambda x: x[1]) #sorting with a key

    for i, e in container:
        print(f"{i.id}: {i.description}, GC={e}")