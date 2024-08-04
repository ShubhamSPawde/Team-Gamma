#code of day21 to transform the curve to circle
from manim import *

class curvetocircle(Scene):
    def construct(self):
        cir=circle(radius=2)
        curve=Curve()

        self.play(Create(curve))
        self.play(Transform(curve,circle))
        self.play(FadeOut(cir))
