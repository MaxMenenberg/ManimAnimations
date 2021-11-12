import os
import numpy as np
import csv

alphabetInts = [];
reflector = [];
for n in range(26):
    alphabetInts.append(n+65)
    reflector.append(n)
    
    
    
rotor1 = alphabetInts.copy();
rotor2 = alphabetInts.copy();
rotor3 = alphabetInts.copy();


# Create randomly shuffled rotors
for n in range(1000):
    randIndexA = np.random.randint(0, 26)
    randIndexB = np.random.randint(0, 26)
    
    rotor1[randIndexA], rotor1[randIndexB] = \
        rotor1[randIndexB], rotor1[randIndexA]
        
for n in range(1000):
    randIndexA = np.random.randint(0, 26)
    randIndexB = np.random.randint(0, 26)
    
    rotor2[randIndexA], rotor2[randIndexB] = \
        rotor2[randIndexB], rotor2[randIndexA]
        
for n in range(1000):
    randIndexA = np.random.randint(0, 26)
    randIndexB = np.random.randint(0, 26)
    
    rotor3[randIndexA], rotor3[randIndexB] = \
        rotor3[randIndexB], rotor3[randIndexA]
        
# Create the reflector
forbiddenIndices = [];
for n in range(20):
    randIndexA = np.random.randint(0, 26)
    randIndexB = np.random.randint(0, 26)
    
    # If we have swapped on of these elements, dont do it again
    if (randIndexA in forbiddenIndices) or (randIndexB in forbiddenIndices):
        pass
    else:
        reflector[randIndexA], reflector[randIndexB] = \
        reflector[randIndexB], reflector[randIndexA]
        forbiddenIndices.append(randIndexA)
        forbiddenIndices.append(randIndexB)
      
for n in range(26):
    reflector[n] = reflector[n] + 65;
 
with open('rotor1.csv', 'w+', newline = '') as file:
    write = csv.writer(file)
    write.writerow(rotor1)
    
 
with open('rotor2.csv', 'w+', newline = '') as file:
    write = csv.writer(file)
    write.writerow(rotor2)
    
 
with open('rotor3.csv', 'w+', newline = '') as file:
    write = csv.writer(file)
    write.writerow(rotor3)
    
 
with open('reflector.csv', 'w+', newline = '') as file:
    write = csv.writer(file)
    write.writerow(reflector)
    