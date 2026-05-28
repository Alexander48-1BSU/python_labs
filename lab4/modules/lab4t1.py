from Bio import SeqIO

def run1(input_file):
    count_cds = 0 # cds counter
    unique_species = set() # counter of unique species strings
    
    with open(input_file, "r") as fl:
        records = list(SeqIO.parse(fl, 'genbank'))

    for i in records:
        cds = [y for y in i.features if y.type == 'CDS']
        count_cds += len(cds) 

        # Extract the biological species name string
        species = i.annotations.get('source')
        if species:
            unique_species.add(species)

        print(f'Species: {species} | Number of CDS: {len(cds)}')

    print('\n--------------------------------------')
    print('Общее количество CDS: ', count_cds)
    print('Найденные виды: ', unique_species)

    # Substring evaluation to bypass NCBI nomenclature artifacts
    has_falco = any("Falco peregrinus" in s for s in unique_species)
    has_malus = any("Malus domestica" in s for s in unique_species)

    # Verify BOTH conditions: At least 10 CDS, and the target taxonomic strings exist
    if count_cds >= 10 and has_falco and has_malus:
        print('Correct: Validation passed.')
        return records
    else:
        print('Incorrect: Validation failed.')
        return None