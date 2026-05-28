from Bio import SeqIO
import textwrap #shorten text
import os  #import operational system to handle output folder creations

def run3(fl):
    os.makedirs('output', exist_ok=True) #creates an output folder if it does not exist yet (in our case it will exist based on main.py structure)

    with open(fl, "r") as input_fl:
        with open('output/lab4t3.txt', 'w', encoding='utf-8') as out_fl: #writes an output in standart encoding inside the output folder
            
            for record in SeqIO.parse(input_fl, "genbank"): #parsing throw genbank objects with the biopython function
                for i in record.features: 
                    if i.type =="CDS":  #selecting coding sequences
#---------------------------------------------------------------
#                         pull out translation (qualifiers meaning = 'translation'.
#                         qualifiers always return list, so pulling out the first object to avoid list datatype
                        protein =i.qualifiers['translation'][0] 
#----------------------------------------------------------------                       
                        wrapped_protein = textwrap.fill(protein, width=66) #takes fisrt 66 aminoacids
                        

                        output_block = ( #creates an output using f strings
                            f"{record.id}: {record.description}\n"
                            f"the location={i.location}\n"
                            f"Translation results=\n"
                            f"{wrapped_protein}\n\n"
                        )
                        
                        # Route the aggregated block to standard output
                        print(output_block, end="") 
                        
                        # Route the aggregated block to the persistent text file
                        out_fl.write(output_block)
