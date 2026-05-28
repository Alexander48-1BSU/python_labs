from Bio import SeqIO

def run1(input_file):
    count_cds = 0 #cds counter
    unique_species = set() #counter of unique sp
    
    with open(input_file, "r") as fl:
        records = list(SeqIO.parse(fl, 'genbank'))

    for i in records:
        cds = [y for y in i.features if y.type == 'CDS']
        count_cds += len(cds) #adding length of coding seq

        # Extract the biological species name
        species = i.annotations.get('source')
        if species:
            unique_species.add(species)

        print(f'Species: {species} | Number of CDS: {len(cds)}')

    print('\n--------------------------------------')
    print('Общее количество CDS: ', count_cds)
    print('Найденные виды: ', unique_species)

    # Define the exact species required for Variant 5
    expected_species = {'Falco peregrinus', 'Malus domestica'}

    # Verify BOTH conditions: At least 10 CDS, and the exact two required species
    if count_cds >= 10 and unique_species == expected_species:
        print('Correct')
        print(records)
        return records
    else:
        print('incorrect')
        return None

