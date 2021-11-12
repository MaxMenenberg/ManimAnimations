from manim import *

class SerpinskiTriangle(Scene):
    def construct(self):
        
        
        N = 2000;
        pointSize = 0.03;
        lineWidth = 2;
        
        # Create a boundary triangle
        tri = Triangle()
        tri.set_stroke(YELLOW, opacity=0.5)
        tri.move_to(ORIGIN)
        tri.scale(3)
        
        self.add(tri)
        
        # Create points on the triangle vertices
        A = Dot(tri.get_corner(LEFT+DOWN))
        A.set_fill(BLUE, opacity=1)
        B = Dot(tri.get_corner(RIGHT+DOWN))
        B.set_fill(GREEN, opacity=1)
        C = Dot(tri.get_corner(UP))
        C.set_fill(RED, opacity=1)
        
        self.play(Create(tri))
        self.wait(0.1)
        self.play(Create(A))    
        self.wait(0.1)
        self.play(Create(B))  
        self.wait(0.1)
        self.play(Create(C))  
        
        self.wait(2)
        
        tempPoint = Dot(point = UP*0.25 + RIGHT*0.25, radius=pointSize);
        self.add(tempPoint)
        
        for n in range(N):
            
            if n < 50:
                delay = ((50-n)/50)/2.5
            else:
                delay = 0.05;
            
            # Pick a random vertex
            v = np.random.randint(3)
            
            # Draw a line between the current point and the randomly selected 
            # vertex
            if v == 0:
                tempLine = Line(tempPoint.get_center(), A.get_center(),stroke_width = lineWidth).set_color(ORANGE)
            elif v == 1:
                tempLine = Line(tempPoint.get_center(), B.get_center(),stroke_width = lineWidth).set_color(ORANGE)
            else:
                tempLine = Line(tempPoint.get_center(), C.get_center(),stroke_width = lineWidth).set_color(ORANGE)
        
            # Animate the line
            
            if n < 100:
                self.play(Create(tempLine), run_time = delay)
                tempPoint = Dot(tempLine.get_center(), radius=pointSize);
                self.add(tempPoint)
                self.wait(delay)
                self.remove(tempLine)
            else:
                tempPoint = Dot(tempLine.get_center(), radius=pointSize);
                self.add(tempPoint)
                #self.wait(0.1)
        self.wait(1)