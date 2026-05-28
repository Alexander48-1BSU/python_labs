
from modules.lab4t1 import run1   #adding commands from other tasks in the modules folder
from modules.lab4t2 import run2
from modules.lab4t3 import run3


def main():
    input_file = "sequence.gb" # sequence.gb was created manually according to the guide in the appedix of the file with variants and tasks
    
    
    is_valid = run1(input_file)
#the first script (lav4t1) just makes sure that sequence.jb was created properly
    if is_valid:
#executing tasks 2&3 scripts passing sequence.gb throw variable input_files
        run2(input_file)
        run3(input_file)

        print("The execution has ended")


if __name__ == "__main__":  #__name__ is one of the hidden python variable, if its meaning is __main__(
#that means the file starts directly) we execute the project, I had never used it before and I am glad that I found out how does it work
    main()
