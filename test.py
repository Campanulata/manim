from manimlib.imports import *
class ComplexAnalysisOverlay(Scene):
    def construct(self):
        # objects
        numberplane = NumberPlane()
        trapezoid = Polygon(np.array([0,0,0]),np.array([0,1,0]),np.array([2,2.5,0]),np.array([2,0,0]),color=RED)
        # 梯形
        a = TextMobject("a",color=RED)
        a.shift(0.25*LEFT+0.5*UP)
        b = TextMobject("b",color=RED)
        b.shift(2.25*RIGHT+0.5*UP)
        h = TextMobject("h",color=RED)
        h.shift(1*RIGHT+0.25*DOWN)
        abh = VGroup(a,b,h)
        # 公式1
        s1 = TexMobject("S=\\frac{1}{2}(a+b) h")
        s1.shift(4*LEFT+2.5*UP)
        # 公式2
        dashedline = DashedLine(np.array([0,1,0]),np.array([2,1,0]))
        trapezoid_rectangle = Polygon(np.array([0,0,0]),np.array([0,1,0]),np.array([2,1,0]),np.array([2,0,0]),color=WHITE)
        trapezoid_rectangle_small = Polygon(np.array([-4.5,0.25,0]),np.array([-4.5,0.75,0]),np.array([-3.5,0.75,0]),np.array([-3.5,0.25,0]),color=WHITE)
        plus = TextMobject("+")
        plus.shift(3*LEFT+0.5*UP)
        trapezoid_angle = Polygon(np.array([0,1,0]),np.array([2,2.5,0]),np.array([2,1,0]),color=WHITE)
        trapezoid_angle_small = Polygon(np.array([-2.5,0.3,0]),np.array([-2,0.7,0]),np.array([-2,0.3,0]),color=WHITE)
        
        s2 = TexMobject("S=")
        s2.shift(5.2*LEFT+0.5*UP)
        # 公式3
        s3 = TexMobject("S=")
        s3.shift(5.2*LEFT+1.5*DOWN)

        dashedline3 = DashedLine(np.array([0,1,0]),np.array([-4/3,0,0]))
        angle_big3 = Polygon(np.array([-4/3,0,0]),np.array([2,2.5,0]),np.array([2,0,0]),color = WHITE)
        angle_small3 = Polygon(np.array([-4/3,0,0]),np.array([0,1,0]),np.array([0,0,0]),color=WHITE)
        angle_big3_s = Polygon(np.array([-4.5,-1.8,0]),np.array([-3.5,-1.2,0]),np.array([-3.5,-1.8,0]),color = WHITE)
        angle_small3_s = Polygon(np.array([-2.5,-1.7,0]),np.array([-2,-1.3,0]),np.array([-2,-1.7,0]),color = WHITE)
        cut = TextMobject("-")
        cut.shift(3*LEFT+1.5*DOWN)

        # showing
        self.add(numberplane)
        self.play(Write(trapezoid))
        self.play(Write(abh))
        self.play(Write(s1))
        self.play(Write(s2))
        self.play(Write(dashedline))
        self.play(Write(trapezoid_rectangle))
        self.play(ReplacementTransform(trapezoid_rectangle,trapezoid_rectangle_small))
        self.play(Write(plus))
        self.play(Write(trapezoid_angle))
        self.play(ReplacementTransform(trapezoid_angle,trapezoid_angle_small))
        self.play(Write(s3))
        self.play(Write(dashedline3))
        self.play(Write(angle_big3))
        self.play(ReplacementTransform(angle_big3,angle_big3_s))
        self.play(Write(cut))
        self.play(Write(angle_small3))
        self.play(ReplacementTransform(angle_small3,angle_small3_s))

