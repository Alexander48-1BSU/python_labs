from Bio import SeqIO
import textwrap

def run3(fl):
    with open("sequence.gb", "r") as fl:
        for record in SeqIO.parse(fl, "genbank"): #takes one record per iteration
        
            for i in record.features: 
                if i.type=="CDS": #whether we have a coding sequence
                
                    print(f"{record.id}: {record.description}")
                    print(f"the location={i.location}")
                    print("Translation results=")
                
                    protein=i.qualifiers['translation'][0] #amino sequence is already provided in the format,
                    #we look at the tage (qualifiers) that is made as list and pull out the first and often the only peace
                    print(textwrap.fill(protein, width=66)) #take the 1st 66 letters
                    print()