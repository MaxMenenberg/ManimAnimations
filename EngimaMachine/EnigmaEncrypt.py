from manim import *
import numpy as np
import csv

# Load the data from a rotor file into a list
def loadRotorFile(fileName):
    with open(fileName, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        letters = []
        for n in range(len(data[0])):
            letters.append(chr(int(data[0][n]))) 
            
    return letters
            
    
# Get the index of the outer letter from a rotor Vgroup given a char letter
def getOuterRotorLetterIndex(vGroup, letter):
    for n in range(len(vGroup)):
        if vGroup[n].text == letter:
            return n
        
# Get the corresponding inner index of a rotor VGroup given a letter from a 
# member of the outer VGroup        
def getInnerRotorLetterIndex(vGroup, letter):
    minDistance = 999;
    minLetterIndex = 0;
    [x1,y1,z1] = letter.get_center();
    for n in range(len(vGroup)):
        [tempX, tempY, tempZ] = vGroup[n].get_center();
        tempDistance = np.sqrt((x1-tempX)**2 + (y1 - tempY)**2)
        
        if tempDistance < minDistance:
            minDistance = tempDistance
            minLetterIndex = n
    return minLetterIndex
    
class EnigmaEncrypt(Scene):
    def construct(self):
        
        plainText = 'AD'
        plainTextFontSize = 25;
        plainTextLetters = VGroup()
        cypherTextLetters = VGroup()
        for n in range(len(plainText)):
            plainTextLetters.add(Text(plainText[n], font_size = plainTextFontSize))
            print(plainTextLetters[n].text)
        
        plainTextLabel = Text("Plain Text: ", font_size = plainTextFontSize)
        plainTextLabel.move_to(LEFT*5 + UP*3)
        
        cypherTextLabel = Text("Cypher Text: ",font_size = plainTextFontSize)
        cypherTextLabel.next_to(plainTextLabel, DOWN, buff = 0.1)
        cypherTextLabel.shift(LEFT*0.17)
        
        # Create the 3 rotor circles
        rotorShift = 0;
        rotor1 = Circle(radius = 1, color = BLUE)
        rotor1.move_to(LEFT*(3+rotorShift))
        
        rotor2 = Circle(radius = 1, color = BLUE)
        rotor2.move_to(LEFT*rotorShift)
        
        rotor3 = Circle(radius = 1, color = BLUE)
        rotor3.move_to(RIGHT*(3-rotorShift))
        
        #Create the letter groups for the 3 rotors
        outG1 = VGroup()
        inG1 = VGroup()
        
        outG2 = VGroup()
        inG2 = VGroup()
         
        outG3 = VGroup()
        inG3 = VGroup()
        
        refIn = VGroup()
        refOut = VGroup()
        
        outerLetterRadius = 1.15
        outerLetterFont = 15
        
        innerLetterRadius = 0.85;
        innerLetterFont = 12;
        
        reflectorFont = 15;
        
        rotorActionRunTime = 0.5;
        
        # Populate the letter groups with the rotor data
        rotor1Letters = loadRotorFile('rotor1.csv')
        rotor2Letters = loadRotorFile('rotor2.csv')
        rotor3Letters = loadRotorFile('rotor3.csv')
        reflectorLetters = loadRotorFile('reflector.csv')
        
        for n in range(26):
            angle = n*2*np.pi/26;
            
            tempLetter = Text(chr(n+65), font_size = outerLetterFont)
            tempLetterInner = Text(rotor1Letters[n], font_size = innerLetterFont, color = RED)
            tempLetter.move_to(rotor1.get_center() + outerLetterRadius*np.cos(angle)*RIGHT + outerLetterRadius*np.sin(angle)*UP )
            tempLetterInner.move_to(rotor1.get_center() + innerLetterRadius*np.cos(angle)*RIGHT + innerLetterRadius*np.sin(angle)*UP )
            outG1.add(tempLetter)
            inG1.add(tempLetterInner)
            
            tempLetter = Text(chr(n+65), font_size = outerLetterFont)
            tempLetterInner = Text(rotor2Letters[n], font_size = innerLetterFont, color = RED)
            tempLetter.move_to(rotor2.get_center() + outerLetterRadius*np.cos(angle)*RIGHT + outerLetterRadius*np.sin(angle)*UP )
            tempLetterInner.move_to(rotor2.get_center() + innerLetterRadius*np.cos(angle)*RIGHT + innerLetterRadius*np.sin(angle)*UP )
            outG2.add(tempLetter)
            inG2.add(tempLetterInner)
            
            tempLetter = Text(chr(n+65), font_size = outerLetterFont)
            tempLetterInner = Text(rotor3Letters[n], font_size = innerLetterFont, color = RED)
            tempLetter.move_to(rotor3.get_center() + outerLetterRadius*np.cos(angle)*RIGHT + outerLetterRadius*np.sin(angle)*UP )
            tempLetterInner.move_to(rotor3.get_center() + innerLetterRadius*np.cos(angle)*RIGHT + innerLetterRadius*np.sin(angle)*UP )
            outG3.add(tempLetter)
            inG3.add(tempLetterInner)
            
            tempLetter = Text(chr(n+65), font_size = reflectorFont)
            tempLetterRef = Text(reflectorLetters[n], font_size = reflectorFont, color = YELLOW)     
            refIn.add(tempLetter)
            refOut.add(tempLetterRef)


        refIn.arrange(RIGHT, buff = 0.1)
        refIn.move_to(DOWN*2)       
        
        refOut.arrange(RIGHT, buff = 0.1)
        refOut.next_to(refIn, DOWN)  

        reflectorBox = Rectangle(height = 1, width = 7, color = BLUE)
        reflectorBox.move_to((refIn.get_center() + refOut.get_center())/2)
        
        engimaBox = Rectangle(height = 5, width = 9, color = PURPLE)
        engimaBox.move_to(DOWN*0.7)
        
        

        # Draw the rotors and the letter mapping
        self.play(Create(rotor1))
        self.play(Create(rotor2))
        self.play(Create(rotor3))
        
        self.play(Create(outG1, run_time = 1), Create(inG1, run_time = 1))
        self.play(Create(outG2, run_time = 1), Create(inG2, run_time = 1))
        self.play(Create(outG3, run_time = 1), Create(inG3, run_time = 1))
        
        self.play(Create(refIn), Create(refOut))
        self.play(FadeIn(reflectorBox))
        self.play(FadeIn(engimaBox))
 
        # Draw the plain text    
        plainTextLetters.arrange(RIGHT, buff = 0.1)
        plainTextLetters.next_to(plainTextLabel, RIGHT)
        
        self.play(Create(plainTextLabel), Create(cypherTextLabel))
        
        self.add(plainTextLetters)
        self.play(Create(plainTextLetters))
        
        # Process each letter through the rotors
        for n in range(len(plainTextLetters)):
            
            # Create a copy of the letter to pass around
            tempLetterCopy = plainTextLetters[n].copy()
            self.add(tempLetterCopy)
            
            # Find the letter mapping on the rotor that matches
            # the current letter
            
            # Pass through rotor1
            outIdx1 = getOuterRotorLetterIndex(outG1, plainTextLetters[n].text)
            inIdx1 = getInnerRotorLetterIndex(inG1, outG1[outIdx1])
            
            self.play(Transform(tempLetterCopy, outG1[outIdx1]))
            self.remove(tempLetterCopy)
            
            self.play(outG1[outIdx1].animate.scale(2), inG1[inIdx1].animate.scale(2), run_time = rotorActionRunTime)
            self.play(outG1[outIdx1].animate.scale(0.5), run_time = rotorActionRunTime)
            
            # Rotate the inner letters of the first rotor by 1 
            # one position
            rotations = []
            for m in range(26):
                rotations.append(inG1[m].animate.move_to(inG1[np.mod(m+1,26)].get_center()))
            
            self.play(*rotations, run_time = rotorActionRunTime)
            
            # Pass through rotor2
            tempLetterCopy = inG1[inIdx1].copy()
            self.add(tempLetterCopy)
            
            outIdx2 = getOuterRotorLetterIndex(outG2, tempLetterCopy.text)
            inIdx2 = getInnerRotorLetterIndex(inG2, outG2[outIdx2])
            
            self.play(Transform(tempLetterCopy, outG2[outIdx2]), inG1[inIdx1].animate.scale(0.5))
            self.remove(tempLetterCopy)
            
            self.play(outG2[outIdx2].animate.scale(2), inG2[inIdx2].animate.scale(2), run_time = rotorActionRunTime)
            self.play(outG2[outIdx2].animate.scale(0.5), run_time = rotorActionRunTime)
            
            # Pass through rotor3
            tempLetterCopy = inG2[inIdx2].copy()
            self.add(tempLetterCopy)
            
            outIdx3 = getOuterRotorLetterIndex(outG3, tempLetterCopy.text)
            inIdx3 = getInnerRotorLetterIndex(inG3, outG3[outIdx3])
            
            self.play(Transform(tempLetterCopy, outG3[outIdx3]), inG2[inIdx2].animate.scale(0.5))
            self.remove(tempLetterCopy)
            
            self.play(outG3[outIdx3].animate.scale(2), inG3[inIdx3].animate.scale(2), run_time = rotorActionRunTime)
            self.play(outG3[outIdx3].animate.scale(0.5), run_time = rotorActionRunTime)
            
            # Display cypher text
            cypherTextTempLetter = Text(inG3[inIdx3].text, font_size = plainTextFontSize) 
            cypherTextLetters.add(cypherTextTempLetter)
            cypherTextLetters.arrange(RIGHT)
            cypherTextLetters.next_to(cypherTextLabel, RIGHT)
           
            
            tempLetterCopy = inG3[inIdx3].copy()
            self.play(Transform(tempLetterCopy, cypherTextTempLetter), inG3[inIdx3].animate.scale(0.5))
            
            
            self.add(cypherTextLetters)
            self.remove(tempLetterCopy)
            self.wait(1)
            