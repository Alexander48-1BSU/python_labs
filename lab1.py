
import sys

def odometer_generation(alphabet, k):
    if k==0:
        return []
        
    indices= [0]*k #setting odometer to a zero
    result=[]
    
    while True:
        word="".join(alphabet[i] for i in indices) #converting digits to letters
        result.append(word) #adding to the list
        
        pos= k-1#2-1=1 , moving odometer changing odometer's roller(digit wheel)
        while pos>=0:
            indices[pos]+=1 #C++
            if indices[pos]<n: #checking limits
                break
            else:
                indices[pos]=0
                pos-=1 
        
        if pos < 0: #have we passed the leftest wheel?
            break
    
    return result

#alfabet creating
alf =input('input sorted alphabet ')
ncomb=input('input out word lenght ')
n =len(alf)
    
if ncomb>10: 
    print('ncomb must be equal or less than 10')
    sys.exit(1)

#function and 
combs =odometer_generation(alf, ncomb) # generate combinatios 
for kmer in combs:
    print(kmer)