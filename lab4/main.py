from Bio import SeqIO

from modules.lab4t1 import run1
from modules.lab4t2 import run2
from modules.lab4t3 import run3


def main():
    input_file = "sequence.gb"
    data = run1(input_file)

    if data:
        result_2 = run2(data)
        result_3 = run3(data)

        print("all tasks are made")


if __name__ == "__main__":
    main()
