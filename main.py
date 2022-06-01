from manim import *
from random import random as rnd
import numpy as np


def cts(x, y):
    return (x - 2.5) * RIGHT + (y - 2.5) * UP


class Introduction(Scene):
    def construct(self):
        self.wait(3)

        title = Tex("Introduction aux systèmes dynamiques")
        self.play(Write(title))

        self.wait(10)

        new_title = Tex("Exemples").to_corner(UL)

        self.play(Transform(title, new_title))
        self.wait()

        billard = VGroup(Rectangle(width=5, height=5, color=BLUE), Circle(radius=1, color=BLUE))
        points = (cts(3, 4), cts(1, 5), cts(0, 4.5), cts(2.13, 3.43), cts(2.733, 5))

        d = Dot().move_to(UP)

        self.play(Create(billard))
        self.wait()
        for k in range(4):
            l = Line(points[k], points[k + 1])
            self.play(MoveAlongPath(d, l, rate_func=linear, run_time=l.get_length() / 2))
        self.play(billard.animate.shift(LEFT * 5).scale(0.5), FadeOut(d, shift=5 * LEFT))
        self.wait(0.5)
        B = Tex("Billards").next_to(billard, DOWN)
        self.play(Write(B))
        self.wait()

        spawning_area = Rectangle(width=2.5, height=2.5, color=BLUE)

        func = lambda pos: 10 * (pos[2] - pos[0]) * RIGHT + (pos[0] * (28 - pos[1]) - pos[2]) * UP + (
                    pos[0] * pos[2] - pos[1] * 8 / 3) * OUT

        stream_lines = StreamLines(func, x_range=[-2.5, 2.5, 0.2], y_range=[-2.5, 2.5, 0.2], stroke_width=2, padding=1,
                                   max_anchors_per_line=30)

        self.add(stream_lines)

        stream_lines.start_animation()

        self.wait(2)

        self.play(Create(spawning_area),stream_lines.end_animation())

        lorenz = StreamLines(func, x_range=[-1, 1, 0.1], y_range=[-1, 1, 0.1], stroke_width=1, padding=0.1)

        L = Tex("Attracteurs").next_to(spawning_area, DOWN)

        self.play(Create(lorenz),Write(L))
        self.wait()

        M = ImageMobject("Mandelbrot.png").scale_to_fit_height(billard.height).shift(4.75*RIGHT)
        MR = SurroundingRectangle(M,color=BLUE)

        self.play(Create(MR),FadeIn(M))

        self.wait(5)

        Texte = Tex("Fonctions itérées").next_to(MR,DOWN)

        self.play(Write(Texte))

        self.wait(5)

        self.play(*[FadeOut(mob) for mob in self.mobjects])



class Fractales(ThreeDScene):
    def construct(self):
        title = Tex("Introduction aux Fractales")
        self.play(Write(title))
        self.wait(10)

        self.play(FadeOut(title,shift=UP))
        title = Tex("Définitions").to_edge(UP)
        self.play(FadeIn(title,shift=UP))

        self.wait(3)

        df = Tex(r"Un ensemble S est une {{fractale}} \\ si sa {{dimension fractale}} est supérieure \\ à sa {{dimension topologique}}.")
        df.set_color_by_tex("fractale",YELLOW)
        df.set_color_by_tex("dimension fractale", GREEN)
        df.set_color_by_tex("dimension topologique", BLUE)
        self.play(Write(df))
        self.wait(5)

        topo = df[5]
        frac = df[3]
        self.play(FadeOut(df))
        self.wait(2)
        topo.next_to(title,DOWN)
        self.play(FadeIn(topo))
        self.wait(10)

        Ex1 = VGroup(
            Dot(rnd()*UP+rnd()*LEFT+rnd()*DOWN+rnd()*RIGHT),
            Dot(rnd()*UP+rnd()*LEFT+rnd()*DOWN+rnd()*RIGHT),
            Dot(rnd()*UP+rnd()*LEFT+rnd()*DOWN+rnd()*RIGHT),
            Dot(rnd()*UP+rnd()*LEFT+rnd()*DOWN+rnd()*RIGHT),
            Dot(rnd()*UP+rnd()*LEFT+rnd()*DOWN+rnd()*RIGHT),
            Dot(rnd()*UP+rnd()*LEFT+rnd()*DOWN+rnd()*RIGHT),
            Dot(rnd()*UP+rnd()*LEFT+rnd()*DOWN+rnd()*RIGHT),
            Dot(rnd()*UP+rnd()*LEFT+rnd()*DOWN+rnd()*RIGHT),
            Dot(rnd()*UP+rnd()*LEFT+rnd()*DOWN+rnd()*RIGHT),
            Dot(rnd()*UP+rnd()*LEFT+rnd()*DOWN+rnd()*RIGHT),
        ).shift(LEFT*4)

        self.play(Create(Ex1))
        dim0 = Tex("Dimension 0",color=BLUE).next_to(Ex1,DOWN)
        self.wait(3)
        self.play(Write(dim0))
        self.wait(3)

        Ex2 = CubicBezier(Ex1[1].get_start(),Ex1[2].get_start(),Ex1[3].get_start(),Ex1[0].get_start()).shift(RIGHT*4).scale(2)
        self.play(Create(Ex2))
        self.wait(3)
        dim1 = Tex("Dimension 1",color=BLUE).next_to(Ex2,DOWN).shift(DOWN/2)

        self.play(Write(dim1))
        self.wait(3)

        sphere = Sphere().shift(4*RIGHT)
        dim3 = Tex("Dimension 3",color=BLUE).next_to(sphere,DOWN)
        self.play(Create(sphere))
        self.wait(2)
        self.move_camera(phi=PI/4)
        self.wait(3)
        self.move_camera(phi=1.2*PI/4)
        self.move_camera(phi=PI/4)
        self.wait(1)
        self.play(Write(dim3))
        self.move_camera(phi=0)
        self.wait(2)
        lol = Tex("Note : Cette sphère est en réalité une surface, donc de dimension 2, mais \"cette boule\" n'avait pas le même charme.").scale(0.3).to_edge(DOWN)
        self.play(FadeIn(lol))
        self.wait(2)

        self.play(FadeOut(sphere,Ex1,Ex2,dim0,dim1,dim3,topo,lol))
        self.wait(5)

        frac.next_to(title,DOWN)

        self.play(Write(frac))
        self.wait(7)
        S = ImageMobject("Sierpinski.png").scale(2/3)

        self.play(FadeIn(S))
        self.wait(5)
        self.play(S.animate.scale(1/2).shift(S.get_height()*UP/4))
        Q = S.copy().shift(S.get_height()*(LEFT*9/16+LEFT*1/64+DOWN))
        R = S.copy().shift(S.get_height()*(RIGHT*9/16+RIGHT*1/64+DOWN))
        self.play(FadeIn(Q,R))
        self.wait(7)

        self.play(FadeOut(Q,R,S))

        m = Tex("$2^d=3$")
        n = Tex(r"$d=\frac{\ln(3)}{\ln(2)}$").next_to(m,DOWN)

        self.play(Write(m))
        self.play(Write(n))
        self.wait(5)

class Julia(Scene) :
    def construct(self):
        title = Tex("Ensembles de Julia")
        self.play(Write(title))
        self.wait(10)

        self.play(FadeOut(title, shift=UP))
        title = Tex("Définitions").to_edge(UP)
        self.play(FadeIn(title, shift=UP))
        self.wait(3)

        B = Tex(r"Orbite de z bornée : \\ {{k}} t.q {{$|f^n(z)|$}}{{$<k$}} pour tout n")
        B.set_color_by_tex("k",YELLOW)
        B.set_color_by_tex("$|f^n(z)|$",GREEN)
        B.set_color_by_tex("$<k$",YELLOW)

        self.play(Write(B))
        self.wait(10)
        self.play(B.animate.scale(2/3).to_edge(LEFT).shift(2*UP))
        self.wait(2)

        E = Tex(r"$K(f) = \{z : \text{Orbite de z est bornée} \}$")
        F = Tex(r"$J(f) = \partial K(f)$").next_to(E,DOWN)

        self.play(Write(E))
        self.wait(5)
        self.play(Write(F))
        self.wait(2)

        self.play(E.animate.scale(2/3).to_edge(LEFT))
        self.play(F.animate.scale(2/3).to_edge(LEFT).shift(DOWN))

        self.wait(5)

        self.play(FadeOut(title,B,E,F))
        self.wait(3)

        title = Tex(r"$c=0$")

        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))
        self.wait(1)

        t = Tex("$Q_0=z^2$").next_to(title,DOWN)

        self.play(Write(t))

        grid = ComplexPlane()

        self.play(DrawBorderThenFill(grid))

        z = Dot(grid.number_to_point(1+1j))

        self.add(z)
        self.wait(2)

        z1 = Dot(grid.number_to_point((1+1j)**2))

        a = Arrow(z,z1)

        self.add(z1)

        self.play(Create(a))
        self.wait(10)

        r = grid.number_to_point(1+0j)


        c = Circle(radius = (r[0]**2+r[1]**2+r[2]**2)**(1/2))

        k = Tex("$K_0$").next_to(c,UR)

        self.play(Create(c),Write(k))

        self.wait(10)

        self.play(*[FadeOut(mob) for mob in self.mobjects])

        self.wait(3)

        title = Tex("Cas général")

        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))
        self.wait(2)

        prop1 = Tex(r"$R = \frac{1+\sqrt{1+4|c|}}{2}$")
        prop2 = Tex(r"Si $|z|>R$, alors $z \notin K_c$").next_to(prop1,DOWN)

        self.play(Write(prop1))
        self.wait(10)
        self.play(Write(prop2))
        self.wait(20)

        self.play(FadeOut(title,prop1,prop2))

        self.wait(2)

        title = Tex("Exemples : ")

        self.play(Write(title))
        self.wait(2)
        self.play(title.animate.to_edge(UP))
        self.wait(2)

        Images = [ImageMobject(f"Julia{k}.png").scale((1/3 if k%2 == 0 else 1/6)) for k in range(4)]

        Images[0].to_corner(UL)
        Images[1].to_corner(UR)
        Images[2].to_corner(DL)
        Images[3].to_corner(DR)

        self.play(FadeIn(Images[0],Images[1],Images[2],Images[3]))











        self.wait(7)











class Mandelbrot(Scene) :
    def construct(self):
        title = Tex("Ensemble de Mandelbrot")
        self.play(Write(title))

        self.wait(2)

        self.play(FadeOut(title))

        M = ImageMobject("Mandelbrot.png").scale(1/6)

        self.wait(5)

        self.play(FadeIn(M))

        self.wait(10)