from manim import *

class basicIntegral(Scene):
    def construct(self):
        
        equationSpacing = 5;
        
        equation1 = MathTex(
            "\int_{0}^{1} x^2 \,dx")
        
        equation2 = MathTex(
            "\\frac{1}{3} x^3 \Big|_0^1")
        
        equation3 = MathTex(
            "\\frac{1}{3} 1^3 - \\frac{1}{3} 0^3")
        
        equation4 = MathTex(
            "\\frac{1}{3}")
        
        
        equation1.shift(UP)
        
        self.play(Write(equation1))
        self.wait(1)
        self.play(equation1.animate.shift(LEFT))
        
        equal1 = MathTex("=").next_to(equation1, RIGHT)
        self.play(FadeIn(equal1))
        
        equation2.next_to(equal1, RIGHT)
        equation1Copy = equation1.copy();
        self.play(Transform(equation1Copy, equation2))
        self.wait(1)
        
        equal2 = MathTex("=").next_to(equal1, DOWN*equationSpacing)
        self.play(FadeIn(equal2))
        
        equation3.next_to(equal2, RIGHT)
        equation2Copy = equation2.copy();
        self.play(Transform(equation2Copy, equation3))
        self.wait(1)
        
        equal3 = MathTex("=").next_to(equal2, DOWN*equationSpacing)
        self.play(FadeIn(equal3))
        
        equation4.next_to(equal3, RIGHT)
        equation3Copy = equation3.copy();
        self.play(Transform(equation3Copy, equation4))
        self.wait(1)
        
        self.remove(equation1Copy)
        self.remove(equation2Copy)
        self.remove(equation3Copy)
        
        shiftAmountUP = 0;
        shiftAmountLEFT = 5;
        self.play(equation1.animate.shift(UP*shiftAmountUP + LEFT*shiftAmountLEFT),\
                  equation2.animate.shift(UP*shiftAmountUP + LEFT*shiftAmountLEFT),\
                  equation3.animate.shift(UP*shiftAmountUP + LEFT*shiftAmountLEFT),\
                  equation4.animate.shift(UP*shiftAmountUP + LEFT*shiftAmountLEFT),\
                  equal1.animate.shift(UP*shiftAmountUP + LEFT*shiftAmountLEFT),\
                  equal2.animate.shift(UP*shiftAmountUP + LEFT*shiftAmountLEFT),\
                  equal3.animate.shift(UP*shiftAmountUP + LEFT*shiftAmountLEFT))
            
        self.wait(2)
      
        ax = Axes(
            x_range=[0, 2],
            y_range=[0, 2],
            x_axis_config={"numbers_to_include": [0, 1]},
            y_axis_config={"numbers_to_include": [0, 1]},
            tips=False,
        )
        ax.scale(0.5)
        ax.shift(RIGHT*2)
        
        labels = ax.get_axis_labels()
        
        curve = ax.plot(lambda x:  x ** 2, x_range=[0, 1], color=BLUE_C)
        yEquals0 = ax.plot(lambda x:  0, x_range=[0, 1])
        area = ax.get_area(curve, [0, 1], bounded_graph=yEquals0, color=RED, opacity=0.75)
        
        
        self.play(Create(ax), Create(labels), run_time = 2)
        self.wait(0.5)
        self.play(Create(curve), run_time = 2)
        self.play(FadeIn(area))
        self.wait(1)
        
        