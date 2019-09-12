from manimlib.imports import *
class bx1(Scene):

    def construct(self):

        ## making object
        x_0 = Line(np.array([0,-4,0]),np.array([0,4,0]),color=WHITE)
        y_0 = Line(np.array([-7,0,0]),np.array([7,0,0]),color=WHITE)
        x__1 =  Line(np.array([-1,-4,0]),np.array([-1,4,0]),color=BLUE)
        x__2 =  Line(np.array([-2,-4,0]),np.array([-2,4,0]),color=BLUE)
        x__3 =  Line(np.array([-3,-4,0]),np.array([-3,4,0]),color=BLUE)
        x__4 =  Line(np.array([-4,-4,0]),np.array([-4,4,0]),color=BLUE)
        x__5 =  Line(np.array([-5,-4,0]),np.array([-5,4,0]),color=BLUE)
        x__6 =  Line(np.array([-6,-4,0]),np.array([-6,4,0]),color=BLUE)
        x__7 =  Line(np.array([-7,-4,0]),np.array([-7,4,0]),color=BLUE)
        x_1 =  Line(np.array([1,-4,0]),np.array([1,4,0]),color=BLUE)
        x_2 =  Line(np.array([2,-4,0]),np.array([2,4,0]),color=BLUE)
        x_3 =  Line(np.array([3,-4,0]),np.array([3,4,0]),color=BLUE)
        x_4 =  Line(np.array([4,-4,0]),np.array([4,4,0]),color=BLUE)
        x_5 =  Line(np.array([5,-4,0]),np.array([5,4,0]),color=BLUE)
        x_6 =  Line(np.array([6,-4,0]),np.array([6,4,0]),color=BLUE)
        x_7 =  Line(np.array([7,-4,0]),np.array([7,4,0]),color=BLUE)
        y__1 = Line(np.array([-7,-1,0]),np.array([7,-1,0]),color=BLUE)
        y__2 = Line(np.array([-7,-2,0]),np.array([7,-2,0]),color=BLUE)
        y__3 = Line(np.array([-7,-3,0]),np.array([7,-3,0]),color=BLUE)
        y__4 = Line(np.array([-7,-4,0]),np.array([7,-4,0]),color=BLUE)

        y_1 = Line(np.array([-7,1,0]),np.array([7,1,0]),color=BLUE)
        y_2 = Line(np.array([-7,2,0]),np.array([7,2,0]),color=BLUE)
        y_3 = Line(np.array([-7,3,0]),np.array([7,3,0]),color=BLUE)
        y_4 = Line(np.array([-7,4,0]),np.array([7,4,0]),color=BLUE)
        
        coordinate = VGroup(x_0,x_1,x_2,x_3,x_4,x_5,x_6,x_7,x__1,x__2,x__3,x__4,x__5,x__6,x__7,y_0,y_1,y_2,y_3,y_4,y__1,y__2,y__3,y__4)

        text1 = TextMobject("直线运动")
        text2 = TextMobject("相互作用")
        text3 = TextMobject("牛顿定律")

        formula11 = TexMobject("v=v_0+a t")
        formula12 = TexMobject("x=v_{0} t+\\frac{1}{2} a t^{2}")
        formula13 = TexMobject("v^{2}-v_{0}^{2}=2 a x")


        formula21 = TexMobject("F=k x")
        formula22 = TexMobject("F_{\\mathrm{f}}=\\mu F_{\\mathrm{N}}")
        formula31 = TexMobject("F=m a")

        ## showing
        self.play(Write(coordinate))

        self.play(Write(text1))
        self.wait(1)
        self.play(ApplyMethod(text1.shift,LEFT*4+UP*2))

        self.play(Write(text2))
        self.wait(1)
        self.play(ApplyMethod(text2.shift,RIGHT*4+UP*2))

        self.play(Write(text3))
        self.wait(1)
        self.play(ApplyMethod(text3.shift,UP*2))
        ## formula
        self.play(Write(formula11))
        self.wait(1)
        self.play(ApplyMethod(formula11.shift,LEFT*4+UP*1))
        self.play(Write(formula12))
        self.wait(1)
        self.play(ApplyMethod(formula12.shift,LEFT*4))
        self.play(Write(formula13))
        self.wait(1)
        self.play(ApplyMethod(formula13.shift,LEFT*4+DOWN*1))

        self.play(Write(formula21))
        self.wait(1)
        self.play(ApplyMethod(formula21.shift,RIGHT*4+UP*1))
        self.play(Write(formula22))
        self.wait(1)
        self.play(ApplyMethod(formula22.shift,RIGHT*4+DOWN*1))

        self.play(Write(formula31))
        self.wait(5)