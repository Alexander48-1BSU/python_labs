from Bio import SeqIO

from modules.lab4t1 import run1
from modules.lab4t2 import run2
from modules.lab4t3 import run3


def main():
    input_file = "sequence.gb"
    
    # run1 checks if the file is valid. Let's assume it returns True/Records if good.
    is_valid = run1(input_file)

    if is_valid:
        # Pass the file string ('sequence.gb') directly to the other modules
        result_2 = run2(input_file)
        result_3 = run3(input_file)

        print("All tasks have been successfully executed!")


if __name__ == "__main__":
    main()