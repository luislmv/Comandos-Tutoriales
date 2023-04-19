from manim import *

class Script(Scene):
    def construct(self):
        ob1 = Triangle(color=BLUE)
        ob2 = Square(color=BLUE)
        ob3 = RegularPolygon(n=5, color=BLUE)
        ob4 = Circle(color=BLUE)
        ob5 = Triangle(color=RED)
        ob6 = Square(color=RED)
        ob7 = RegularPolygon(n=5, color=RED)
        ob8 = Circle(color=RED)
        
        ob_list = [ob1, ob2, ob3, ob4 , ob5, ob6, ob7, ob8]
        pos_list = [UL, LEFT, DL, DOWN, DR, RIGHT, UR, UP]
        for i in range(0,8):
            self.add(ob_list[i].shift(pos_list[i]*2.5))
        
        self.wait(1)
        
        for i in range(1,9):
            self.play(*[ob_list[j].animate.move_to(pos_list[(i+j)%8]*2.5) for j in range(0,8)])
            self.wait(1)