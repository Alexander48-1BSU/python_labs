from Bio import SeqIO
import textwrap
import os

def run3(fl):
    # Establish the output directory structure
    os.makedirs('output', exist_ok=True)

    # Initialize file streams for both reading and writing
    with open(fl, "r") as input_fl:
        with open('output/lab4t3.txt', 'w', encoding='utf-8') as out_fl:
            
            for record in SeqIO.parse(input_fl, "genbank"): 
                for i in record.features: 
                    if i.type == "CDS": 
                        
                        # Extract structural annotations
                        protein = i.qualifiers['translation'][0] 
                        wrapped_protein = textwrap.fill(protein, width=66)
                        
                        # Concatenate the biological metadata and sequence into a single memory block
                        output_block = (
                            f"{record.id}: {record.description}\n"
                            f"the location={i.location}\n"
                            f"Translation results=\n"
                            f"{wrapped_protein}\n\n"
                        )
                        
                        # Route the aggregated block to standard output
                        print(output_block, end="") 
                        
                        # Route the aggregated block to the persistent text file
                        out_fl.write(output_block)