from manimlib.imports import *

class bx2(Scene):

    def construct(self):

        ## making object
        text111 = TexMobject("x=v_{0} t+\\frac{1}{2} a t^{2}")
        text222 = TextMobject("相互作用")
        text333 = TextMobject("牛顿定律")


        ## showing
        self.play(Write(text111))
        self.wait(1)
        self.play(ApplyMethod(text111.shift,LEFT*4+UP*2))

        self.play(Write(text222))
        self.wait(1)
        self.play(ApplyMethod(text222.shift,RIGHT*4+UP*2))

        self.play(Write(text333))
        self.wait(1)
        self.play(ApplyMethod(text333.shift,UP*2))
        ## formula


class bx1(Scene):

    def construct(self):

        ## making object
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


class latex(Scene):
    def construct(self):
        example_text = TextMobject(
            "This is a some text",
            tex_to_color_map={"text": YELLOW}
        )
        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",


        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()







class test1(Scene):

    def construct(self):

        ## making object
        w1 = TextMobject("离暑假课结束还有两天直线运动")


        ##position
        ## showing object
        self.play(Write(w1))
        self.wait(1)
        self.wait(3)


class test2(Scene):

    def construct(self):

        ## making object
        ring = Annulus(inner_radius=.4,outer_radius=1,color=BLUE)
        square = Square(color=ORANGE,fill_color=ORANGE,fill_opacity=0.5)
        rect = Rectangle(height=3.2,width=1.2,color=PINK,fill_color=PINK,fill_opacity=0.5)

        line01 = Line(np.array([0,3.6,0]),np.array([0,2,0]),color=BLUE)
        line02 = Line(np.array([-1,2,0]),np.array([-1,-1,0]),color=BLUE)
        line03 = Line(np.array([1,2,0]),np.array([1,0.5,0]),color=BLUE)

        ## position
        ring.shift(UP * 2)
        square.shift(LEFT+DOWN * 2)
        rect.shift(RIGHT + DOWN * (3.2/2 - 0.5))

        ## showing object
        self.add(line01)
        self.play(GrowFromCenter(ring))
        self.wait(0.5)
        self.play(FadeIn(line02),FadeIn(line03))
        self.wait(0.5)
        self.play(FadeInFromDown(square))
        self.play(FadeInFromDown(rect))
        self.wait()

class love_death_robot(Scene):

    def construct(self):

        ## making object
        circle01 = Circle(fill_color=RED,color=RED)
        circle02 = Circle(fill_color=RED,color=RED)
        square01 = Square(fill_color=RED,color=RED)
        love = VGroup(circle01,circle02,square01)

        rect01 = Rectangle(height=1,width=1,fill_color=RED,color=RED)
        rect02 = Rectangle(height=1,width=1,fill_color=RED,color=RED)
        deth = VGroup(rect01,rect02)

        square02 = Rectangle(fill_color=RED,color=RED)
        square02.scale(1.6)
        c01 = Circle(color=RED)
        c02 = Circle(color=RED)
        c01.scale(0.45)
        c02.scale(0.45)
        robot = VGroup(square02,c01,c02)

        line= Line(np.array([-6,-2.4,0]),np.array([6,-2.4,0]))

        text01 = TextMobject("Love\n Death\n+\nRobots")
        text01.scale(1.8)

        group_all = VGroup(love,deth,robot,line,text01)

        ## position
        circle01.shift((UP+LEFT) * np.sqrt(2)/2)
        circle02.shift((UP+RIGHT) * np.sqrt(2)/2)
        square01.rotate(np.pi/4)

        rect01.rotate(np.pi/4)
        rect02.rotate(-np.pi/4)

        c01.shift((np.array([-0.72,0.6,0])))
        c02.shift((np.array([0.72,0.6,0])))
        robot.shift(RIGHT*4)

        text01.shift((DOWN * 2.5))

        ## showing
        self.play(ShowCreation(circle01),ShowCreation(circle02),ShowCreation(square01))
        self.wait(1)
        self.play(ApplyMethod(love.shift,LEFT*4))
        self.wait(1)

        self.play(ShowCreation(rect01),ShowCreation(rect02))
        self.wait(1)












