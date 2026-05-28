from Bio import SeqIO

def run1(input_file):
    count_cds= 0 # cds counter
    unique_species =set() # counter of unique species strings with func set()
    
    with open(input_file, "r") as fl:   #standart opening in the read mode                          
        records = list(SeqIO.parse(fl, 'genbank'))

    for i in records:
        cds = [e for e in i.features if e.type=='CDS'] #pulls out coding sequences 
        count_cds += len(cds)  #counts overall length

        species = i.annotations.get('source') # Extracting names of species
        if species:
            unique_species.add(species) #making list with unique species names

        print(f'Species: {species}.Number of CDS: {len(cds)}')

    print('\n----------------')
    print('overall number of CDS: ', count_cds)
    print('Найденные виды: ', unique_species)

# next part:
#The Loop (for s in unique_species): The code opens your set of saved GenBank names and looks at them one by one.
#then looks for any mention
#if there is at least one returns True
    has_falco = any("Falco peregrinus" in s for s in unique_species) 
    has_malus = any("Malus domestica" in s for s in unique_species)
#-------------------------------
    if count_cds >= 10 and has_falco and has_malus: #checks both conditions: presence of targeted species and >=10 coding sequences
        print('Correct')
        return records
    else:
        print('Incorrect')
        return None
