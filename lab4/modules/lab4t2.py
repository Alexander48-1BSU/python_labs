
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction #special function for counting gc share
import textwrap #shorten strings
import os #'operating system', we need it to create an output folder

def run2(fl):
    container = []

    with open(fl, "r") as file: #standart opening in reading mode, fl is sequence.gb made in the task 1
        for i in SeqIO.parse(file, "genbank"): # parse through genbank pieces 
            result = gc_fraction(i.seq) #count gc pairs in the sequence
            container.append((i, result)) # SeqI0(i) plus gc rate(result), we will need i to extract id and description then

    container.sort(key=lambda x: x[1]) #sorting with a key, [1] means that order is created based on gc share(rate), not SeqI0
    os.makedirs('output', exist_ok=True) #creates an output folder if it does not exist yet
 

    with open('output/lab4t2.txt', 'w', encoding='utf-8') as out_fl: #opening file in writing mode and standart encoding
        for i, e in container: #i is SeqI0, e is result

            text =f"{i.id}: {i.description}, GC={e}" #f-string to unite regular text and variales
            wrapped_text=textwrap.fill(text, width=65, initial_indent='     ') #wrapping text, initial_indent is an aesthetic parameter, adds margin from the left
            print(wrapped_text) #check, print result
            out_fl.write(wrapped_text +'\n') #writing from a new string (we are in a cycle)
            
            
    
