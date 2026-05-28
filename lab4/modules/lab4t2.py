
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import textwrap
import os

def run2(fl):
    container = []

    with open(fl, "r") as file:
        for i in SeqIO.parse(file, "genbank"): # parse through genbank pieces 
            result = gc_fraction(i.seq) #count gc pairs in the sequence
            container.append((i, result)) # id plus gc rate

    container.sort(key=lambda x: x[1]) #sorting with a key
    os.makedirs('output', exist_ok=True)
 

    with open('output/lab4t2.txt', 'w', encoding='utf-8') as out_fl:
        for i, e in container:

            text = f"{i.id}: {i.description}, GC={e}"
            wrapped_text = textwrap.fill(text, width=65, initial_indent='     ') #wrapping text
            print(wrapped_text) #check
            out_fl.write(wrapped_text + '\n') #writing from a new string
            
            
            
    