from manim import *

def color_grad(A,B,k,n) :
    t = k/n
    c = color_to_int_rgb(A)*(1-t) + color_to_int_rgb(B)*t
    return rgb_to_color(c/255)

class Saddle_node(Scene):
    def construct(self):
        t = 2
        grid = NumberPlane(x_range=[-2, 2, 0.2], y_range=[-2, 2, 0.2], x_length=7 * 16 / 9, y_length=7)

        c = ValueTracker(1)

        func = lambda x: x ** 2

        func2 = always_redraw(lambda: grid.plot(lambda x: x ** 2 + c.get_value(), color=ORANGE))

        self.play(DrawBorderThenFill(grid))
        self.wait(t)
        self.play(Create(func2))

        id = grid.plot(lambda x: x)
        self.play(Create(id))

        start_value = -0.3
        x = start_value

        def make_some_real_shit_happen():
            result = VGroup()
            x = start_value
            for i in range(30):
                result.add(
                    Line(grid.coords_to_point(x, x), grid.coords_to_point(x, x ** 2 + c.get_value()),color=color_grad(WHITE,RED_C,i,30)),
                    Line(grid.coords_to_point(x, x ** 2 + c.get_value()),
                         grid.coords_to_point(x ** 2 + c.get_value(), x ** 2 + c.get_value()),color=color_grad(WHITE,RED_C,i,30))
                )
                x = x ** 2 + c.get_value()

            return result

        d = Dot(grid.coords_to_point(x, x))
        self.add(d)
        lines = always_redraw(make_some_real_shit_happen)
        self.play(Create(lines))
        value = always_redraw(lambda: Tex(f"$c={c.get_value():.2f}$").to_corner(DR))
        self.play(Write(value))

        self.play(c.animate(run_time=5*t).set_value(0.3))
        self.play(c.animate(run_time=10*t, rate_func=linear).set_value(0.2))
        self.play(c.animate(run_time=5*t).set_value(-0.7))
        self.play(c.animate(run_time=10*t, rate_func=linear).set_value(-0.8))
        self.play(c.animate(run_time=5*t).set_value(-1.2))
        self.play(c.animate(run_time=10*t, rate_func=linear).set_value(-1.3))
        self.play(c.animate(run_time=5*t).set_value(-1.5))

        self.wait(5)

        #self.play()


class Beginnings(Scene) :
    def construct(self):
        title = Tex("Famille quadratique").scale(1.2)
        subtitle = Tex("$Q_c(x)=x^2+c$").next_to(title,DOWN)
        self.play(Write(title))
        self.wait(1)
        self.play(Write(subtitle))
        self.wait(10)
        self.play(FadeOut(title,subtitle))
        self.wait(5)

        title = Tex("Orbites").to_edge(UP)
        self.play(Write(title))
        self.wait(10)

        ex = Tex(r"Exemple : $f(x)=\sqrt{x}$")
        self.play(Write(ex))
        self.wait(5)
        self.play(ex.animate.next_to(title,DOWN))
        self.wait(1)

        xs = [
            Tex("$x_0=256$").next_to(ex,DOWN),
            Tex(r"$x_1 = \sqrt{x_0}$", r"$ = \sqrt{256}$",r"$ = 16$"),
            Tex(r"$x_2 = \sqrt{x_1}$", r"$ = \sqrt{16}$",r"$ = 4$"),
            Tex(r"$x_3 = \sqrt{x_2}$", r"$ = \sqrt{4}$",r"$ = 2$"),
            Tex(r"$x_4 = \sqrt{x_3}$", r"$ = \sqrt{2}$",r"$ \approx 1.41$"),
            Tex(r"\vdots")
        ]

        self.play(Write(xs[0]))
        self.wait(5)

        for i in range(1,len(xs)) :
            xs[i].next_to(xs[i-1],DOWN)
            for j,k in enumerate(xs[i]) :
                k.shift(j*RIGHT/10)
                self.play(Write(k))
                self.wait(1)
            self.wait(5)

        self.play(*[FadeOut(mob) for mob in self.mobjects])

        self.wait(3)

        title = Tex("Intuition Géométrique").scale(1.2).to_edge(UP)
        self.play(Write(title))

        graph = NumberPlane(x_range=[-2,2,0.2],x_length=14,y_range=[-2,2,0.2],y_length=7).shift(DOWN/2)

        self.play(DrawBorderThenFill(graph))

        self.wait(3)

        func = lambda x : x**3-3*x

        F = graph.plot(func,color=ORANGE)
        Id = graph.plot(lambda x: x)

        self.play(Create(F))
        self.wait(1)
        self.play(Create(Id))

        self.wait(5)

        x = 0.45

        D1 = Dot(graph.coords_to_point(x,x))
        self.add(D1)
        label1 = Tex("$(x_n,x_n)$").scale(0.5).next_to(D1,UP).shift(0.5*LEFT)
        self.play(Write(label1))
        self.wait(10)

        D2 = Dot(graph.coords_to_point(x,func(x)))
        label2 = Tex("$(x_n,f(x_n))$").scale(0.5).next_to(D2,DOWN).shift(0.5*LEFT)
        L1 = DashedLine(D1,D2)

        self.play(Create(L1))
        self.play(Create(D2),Write(label2))
        self.wait(10)

        D3 = Dot(graph.coords_to_point(func(x), func(x)))
        label3 = Tex("$(x_{n+1},x_{n+1})$").scale(0.5).next_to(D3,DOWN)
        L2 = DashedLine(D2, D3)

        self.play(Create(L2))
        self.play(Create(D3), Write(label3))
        self.wait(10)

        x = func(x)

        D4 = Dot(graph.coords_to_point(x, x))
        self.add(D4)

        D5 = Dot(graph.coords_to_point(x, func(x)))
        L3 = DashedLine(D4, D5)

        self.play(Create(L3))

        D6 = Dot(graph.coords_to_point(func(x), func(x)))
        label4 = Tex("$(x_{n+2},x_{n+2})$").scale(0.5).next_to(D6, DOWN)
        L4 = DashedLine(D5, D6)

        self.play(Create(L4))
        self.play(Create(D6),Write(label4))
        self.wait(15)

        self.play(*[FadeOut(mob) for mob in self.mobjects])


        self.wait(5)


class PointsFixes(Scene) :
    def construct(self):
        title = Tex("Points fixes").scale(1.2)

        self.play(Write(title))
        self.wait(5)

        new_title = Tex("Définition").to_corner(UL)

        self.play(Transform(title,new_title))
        self.wait(5)

        df = Tex("$x$ est point fixe de $f$ $\\iff f(x) = x$")
        self.play(Write(df))
        self.wait(10)
        ex = Tex("Exemples").next_to(df,DOWN)

        self.play(Write(ex))

        exemples = VGroup(
            Tex("$f(x)=x^3-3x$ aux points -2, 0, et 2"),
            Tex("$f(x)=sin(x)$ au point 0").shift(DOWN),
            Tex("$f(x)=\\sqrt{x}$ au point 1").shift(2*DOWN)
        ).next_to(ex,DOWN).scale(3/4)

        for k in exemples :
            self.wait(3)
            self.play(Write(k))

        self.wait(10)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        title = Tex("Théorème des points fixes").to_edge(UP)
        self.play(Write(title))
        self.wait(5)

        estdit = Tex("Un point fixe $x$ de $f$ est dit :").shift(4*LEFT)

        pos1 = Tex("• Attractif si $|f'(x)| < 1$").next_to(estdit,RIGHT)
        pos2 = Tex("• Répulsif si $|f'(x)| > 1$").next_to(pos1,DOWN)
        pos3 = Tex("• Neutre si $|f'(x)| = 1$").next_to(pos2,DOWN)

        self.play(Write(estdit))

        self.wait(3)

        self.play(Write(pos1))
        self.wait(2)

        self.play(Write(pos2))
        self.wait(2)

        self.play(Write(pos3))
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects])

        self.wait(5)