
import sys

def odometer_generation(alphabet, k):
    n = len(alphabet)
    if k==0: #whether word length is equal to 0
        return []
        
    indices= [0]*k #creating and setting odometer to a zero
    result=[]
    
    while True:
        word="".join(alphabet[i] for i in indices) #converting digits to letters
        result.append(word) #adding to the list
        
        pos= k-1#2-1=1 , changing odometer's roller(digit wheel) one step back, during the first iteration to set it to the last position
        while pos>=0: #if we still have space from left to move to
            indices[pos]+=1 #moving the wheel of odometer
            if indices[pos]<n: #checking limits
                break #go back and save the word
            else: # Did we run out of the alfabet?
                indices[pos]=0
                pos-=1 
        
        if pos < 0: #have we passed the leftest wheel?
            break
    
    return result

#alfabet creating
alf =input('input sorted alphabet ')
ncomb=int(input('input out word lenght '))

    
if ncomb>10: 
    print('ncomb must be equal or less than 10')
    sys.exit(1)

#function and 
combs =odometer_generation(alf, ncomb) # generate combinatios 
for kmer in combs:
    print(kmer)
