
from manim import *
import numpy as np


def createRandomLetters():
    # Fill a list with A-Z and then randomly swap elements 100 times
    letters = [];
    for n in range(26):
        letters.append(chr(n+65))
        
    for n in range(100):
        pos1 = np.random.randint(0, 26)
        pos2 = np.random.randint(0, 26)
        letters[pos1], letters[pos2] = letters[pos2], letters[pos1]
  
    return letters
    
def getOuterRotorLetterIndex(vGroup, letter):
    for n in range(len(vGroup)):
        if vGroup[n].text == letter:
            return n
        
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
        
        # Create the 3 rotor circles
        rotorShift = 1;
        rotor1 = Circle(radius = 1, color = BLUE)
        rotor1.move_to(LEFT*(3+rotorShift)+UP)
        rotor1Letters = createRandomLetters()
        
        rotor2 = Circle(radius = 1, color = BLUE)
        rotor2.move_to(LEFT*rotorShift)
        rotor2Letters = createRandomLetters()
        
        rotor3 = Circle(radius = 1, color = BLUE)
        rotor3.move_to(RIGHT*(3-rotorShift)+UP)
        rotor3Letters = createRandomLetters()
        
        #Create the letter groups for the 3 rotors
        outerLetterGroup1 = VGroup()
        innerLetterGroup1 = VGroup()
        
        outerLetterGroup2 = VGroup()
        innerLetterGroup2 = VGroup()
         
        outerLetterGroup3 = VGroup()
        innerLetterGroup3 = VGroup()
        
        outerLetterRadius = 1.15
        outerLetterFont = 15
        
        innerLetterRadius = 0.85;
        innerLetterFont = 12;
        for n in range(26):
            angle = n*2*np.pi/26;
            
            tempLetter = Text(chr(n+65), font_size = outerLetterFont)
            tempLetterInner = Text(rotor1Letters[n], font_size = innerLetterFont, color = RED)
            tempLetter.move_to(rotor1.get_center() + outerLetterRadius*np.cos(angle)*RIGHT + outerLetterRadius*np.sin(angle)*UP )
            tempLetterInner.move_to(rotor1.get_center() + innerLetterRadius*np.cos(angle)*RIGHT + innerLetterRadius*np.sin(angle)*UP )
            outerLetterGroup1.add(tempLetter)
            innerLetterGroup1.add(tempLetterInner)
            
            tempLetter = Text(chr(n+65), font_size = outerLetterFont)
            tempLetterInner = Text(rotor2Letters[n], font_size = innerLetterFont, color = RED)
            tempLetter.move_to(rotor2.get_center() + outerLetterRadius*np.cos(angle)*RIGHT + outerLetterRadius*np.sin(angle)*UP )
            tempLetterInner.move_to(rotor2.get_center() + innerLetterRadius*np.cos(angle)*RIGHT + innerLetterRadius*np.sin(angle)*UP )
            outerLetterGroup2.add(tempLetter)
            innerLetterGroup2.add(tempLetterInner)
            
            tempLetter = Text(chr(n+65), font_size = outerLetterFont)
            tempLetterInner = Text(rotor3Letters[n], font_size = innerLetterFont, color = RED)
            tempLetter.move_to(rotor3.get_center() + outerLetterRadius*np.cos(angle)*RIGHT + outerLetterRadius*np.sin(angle)*UP )
            tempLetterInner.move_to(rotor3.get_center() + innerLetterRadius*np.cos(angle)*RIGHT + innerLetterRadius*np.sin(angle)*UP )
            outerLetterGroup3.add(tempLetter)
            innerLetterGroup3.add(tempLetterInner)
        
        
        # Since we can access the text in the Vgroup we can programtically
        # pass a letter through the enigma machine
        print(outerLetterGroup1[0].text)
        
        self.play(Create(rotor1))
        #self.play(Create(rotor2))
        #self.play(Create(rotor3))
        
        self.play(Create(outerLetterGroup1, run_time = 1), Create(innerLetterGroup1, run_time = 1))
        #self.play(Create(outerLetterGroup2, run_time = 1), Create(innerLetterGroup2, run_time = 1))
        #self.play(Create(outerLetterGroup3, run_time = 1), Create(innerLetterGroup3, run_time = 1))
        
        inputWord = "DOG"
        inputWordFontSize = 25;
        inputWordLetters = VGroup()
        for n in range(len(inputWord)):
            inputWordLetters.add(Text(inputWord[n], font_size = inputWordFontSize))
            
        inputWordLetters.arrange(DOWN)
        inputWordLetters.move_to(LEFT*6 + UP*2)
        
        self.add(inputWordLetters)
        self.play(Create(inputWordLetters))
        
     
            
        print(len(inputWordLetters))
        
        firstLetterOuterIndex = getOuterRotorLetterIndex(outerLetterGroup1, inputWordLetters[0].text)
        self.play(Transform(inputWordLetters[0], \
                            outerLetterGroup1[firstLetterOuterIndex] ))
        inputWordLetters.remove(inputWordLetters[0])
        
        firstLetterInnerIndex = getInnerRotorLetterIndex(innerLetterGroup1, outerLetterGroup1[firstLetterOuterIndex])
        
        self.play(outerLetterGroup1[firstLetterOuterIndex].animate.scale(2), innerLetterGroup1[firstLetterInnerIndex].animate.scale(2), run_time = 1)
        self.play(outerLetterGroup1[firstLetterOuterIndex].animate.scale(0.5), innerLetterGroup1[firstLetterInnerIndex].animate.scale(0.5), run_time = 1)
        self.wait(2)