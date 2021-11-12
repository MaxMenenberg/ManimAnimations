from manim import *
import numpy as np

class EnigmaRotor(Scene):
    def construct(self):
        
        letterGroup = VGroup()
        
        rotor = Circle(radius = 1, color = BLUE)
        rotor.move_to(ORIGIN)
        
        centerDot = Dot(ORIGIN)
        centerDot.set_fill(WHITE)
        
        edgeDot = Dot(LEFT*2)
        edgeDot.set_fill(BLUE)
        
        
        self.add(edgeDot)
        self.add(centerDot)
        
        
        letterRadius = 1.15
        letterFont = 15
        for n in range(26):
            angle = n*2*np.pi/26;
            tempLetter = Text(chr(n+65), font_size = letterFont)
            tempLetter.move_to(letterRadius*np.cos(angle)*RIGHT + letterRadius*np.sin(angle)*UP )
            letterGroup.add(tempLetter)
        
        self.add(rotor)
        self.play(Create(letterGroup, run_time = 2))
        
        
        M = 5
        k = 3
        for m in range(M):
        
            rotations = []
        
            for n in range(26):
                rotations.append(letterGroup[n].animate.move_to(letterGroup[np.mod(n+k,26)].get_center()))
                
            self.play(*rotations)
        
        self.wait(1)
        