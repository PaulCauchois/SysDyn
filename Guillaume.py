from manim import *
import random


class CantorSet(Scene):
    def construct(self):
        CONFIG = {
            "Cantor steps": 4
        }
        title = Text("Ensemble de Cantor").to_edge(UP)
        self.add(title)

        lines = [VGroup(Line(6 * LEFT, 6 * RIGHT))]
        self.play(FadeIn(lines[0]))
        self.wait(1)
        self.play(lines[0].animate.shift(2 * UP))
        self.wait(1)
        names = [Tex("$K_0$").next_to(lines[0], 2 * LEFT)]
        self.play(Write(names[0]))

        # Construction de Fucking Cantor de ses morts omg je veux tuer ce gars

        # TODO : Ajouter les bornes d'intervalle genre 1/3 et 2/3

        for i in range(1, CONFIG["Cantor steps"]):
            self.wait(5)
            l = VGroup()
            m = VGroup()
            r = VGroup()
            for k in lines[i - 1]:
                l.add(Line(k.get_start(), k.get_start() * 2 / 3 + k.get_end() / 3))
                m.add(Line(k.get_start() * 2 / 3 + k.get_end() / 3, k.get_start() / 3 + k.get_end() * 2 / 3))
                r.add(Line(k.get_start() / 3 + k.get_end() * 2 / 3, k.get_end()))
            w = VGroup()
            for k in range(len(l)):
                w.add(l[k])
                w.add(r[k])
            lines.append(w)
            self.play(lines[i].animate.shift(DOWN), m.animate.shift(DOWN))
            self.wait(5)
            self.play(FadeOut(m, shift=DOWN))
            self.wait(5)
            names.append(Tex(f"$K_{i}$").next_to(lines[i], 2 * LEFT))
            self.play(Write(names[i]))

        dots = Tex("\\vdots").next_to(names[len(names) - 1], DOWN)
        self.play(Write(dots))

        self.wait(5)

        Kant = Tex(r"$K = \displaystyle \bigcap_{n \in \mathbb{N}} K_n$").to_edge(DOWN).shift(UP / 2)

        box = SurroundingRectangle(Kant)
        self.play(Write(Kant))
        self.play(Create(box))

        self.wait(5)

        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != Kant and mob != box])
        self.remove(box)

        self.play(Kant.animate.to_corner(UR))

        box2 = SurroundingRectangle(Kant)
        self.add(box2)

        prop = Tex("Propriétés :").to_corner(UL)
        self.play(Write(prop))
        self.wait(2)

        # Propriétés

        prop1 = Tex("• Compact").scale(1.5)

        self.play(Write(prop1))
        self.wait(2)

        T = Tex(r"Suite décroissante de compacts \\ non vides").scale(0.5).next_to(prop1, DOWN)

        self.play(Write(T))

        self.wait(5)

        self.play(FadeOut(T), prop1.animate.next_to(prop, DOWN).to_edge(LEFT).scale(2 / 3))

        # TODO : Mettre to_edge pour bien aligner ces petits bâtards.

        self.wait(5)

        prop2 = Tex("• Mesure nulle").scale(1.5)

        self.play(Write(prop2))

        T1 = Tex(r"$\lambda(K_0) = 1$").scale(2 / 3).next_to(prop2, DOWN)
        T2 = Tex(r"$\lambda(K_{n+1}) = \frac{2}{3} \lambda (K_n)$").scale(2 / 3).next_to(T1, DOWN)
        T3 = Tex(
            r"$\lambda(K) = \displaystyle \lim_{n\rightarrow \infty} \lambda(K_{n})= \displaystyle \lim_{n\rightarrow \infty} \left (\frac{2}{3} \right )^{n}=0$").scale(
            2 / 3).next_to(T2, DOWN)

        self.play(Write(T1))
        self.wait(5)
        self.play(Write(T2))
        self.wait(5)
        self.play(Write(T3))

        self.wait(10)

        self.play(FadeOut(T1, T2, T3))
        self.play(prop2.animate.next_to(prop1, DOWN).scale(2 / 3).to_edge(LEFT))

        self.wait(2)

        prop3 = Tex("• Non vide").scale(1.5)

        self.play(Write(prop3))

        T = Tex(r"Non vide car $0 \in K$").scale(2 / 3).next_to(prop3, DOWN)

        self.play(Write(T))

        self.wait(5)

        self.play(FadeOut(T), prop3.animate.next_to(prop2, DOWN).scale(2 / 3).to_edge(LEFT))

        self.wait(5)

        prop4 = Tex("• Indénombrable").scale(1.5)

        T = Tex("Argument diagonal de Cantor").scale(2 / 3).next_to(prop4, DOWN)

        self.play(Write(prop4))

        self.wait(2)

        self.play(Write(T))

        self.play(prop4.animate.next_to(prop3, DOWN).scale(2 / 3).to_edge(LEFT))

        self.wait(5)

        # Fin des propriétés, argument diagonal de mah boi Cantor rpz

        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != T])
        self.play(T.animate.to_edge(UP).scale(1.5))

        self.wait(5)

        # Generating numbers :
        r1 = Tex('0.', random.choice(('0', '2')) + ' ',
                 ' '.join([random.choice(('0', '2')) for k in range(7)]) + '$\cdots$').scale(2).next_to(T,
                                                                                                        DOWN).to_edge(
            LEFT)
        r2 = Tex(
            '0.' + ' '.join([random.choice(('0', '2')) for k in range(1)]) + ' ',
            random.choice(('0', '2')) + ' ',
            ' '.join([random.choice(('0', '2')) for k in range(6)]) + '$\cdots$'
        ).scale(2).next_to(r1, DOWN)
        r3 = Tex(
            '0.' + ' '.join([random.choice(('0', '2')) for k in range(2)]) + ' ',
            random.choice(('0', '2')) + ' ',
            ' '.join([random.choice(('0', '2')) for k in range(5)]) + '$\cdots$'
        ).scale(2).next_to(r2, DOWN)
        r4 = Tex(
            '0.' + ' '.join([random.choice(('0', '2')) for k in range(3)]) + ' ',
            random.choice(('0', '2')) + ' ',
            ' '.join([random.choice(('0', '2')) for k in range(4)]) + '$\cdots$'
        ).scale(2).next_to(r3, DOWN)
        r5 = Tex(r'\vdots').scale(2).next_to(r4, DOWN)
        str(2 - int(r1[1].get_tex_string()))
        r6 = Tex('0.', r1[1].get_tex_string(), ' ' + r2[1].get_tex_string(), ' ' + r3[1].get_tex_string(),
                 ' ' + r4[1].get_tex_string(), '$\cdots$').scale(2).next_to(r5, DOWN).to_edge(LEFT)
        r6_tf = Tex('0.', str(2 - int(r1[1].get_tex_string())), ' ' + str(2 - int(r2[1].get_tex_string())),
                    ' ' + str(2 - int(r3[1].get_tex_string())), ' ' + str(2 - int(r4[1].get_tex_string())),
                    '$\cdots$').scale(
            2).next_to(r5, DOWN).to_edge(LEFT)

        self.play(FadeIn(r1))
        self.play(FadeIn(r2))
        self.play(FadeIn(r3))
        self.play(FadeIn(r4))
        self.play(FadeIn(r5))

        self.wait(2)

        box1 = SurroundingRectangle(r1[1])
        box2 = SurroundingRectangle(r2[1])
        box3 = SurroundingRectangle(r3[1])
        box4 = SurroundingRectangle(r4[1])

        self.play(Create(box1))
        self.play(Create(box2))
        self.play(Create(box3))
        self.play(Create(box4))

        self.wait(5)

        self.play(
            box1.animate.align_to(r6, DOWN),
            box2.animate.align_to(r6, DOWN),
            box3.animate.align_to(r6, DOWN),
            box4.animate.align_to(r6, DOWN)
        )
        self.wait(2)

        r6.shift(UP / 10)
        r6_tf.shift(UP / 10)

        self.play(Write(r6))

        self.wait(2)

        self.play(Transform(r6, r6_tf))

        self.wait(5)


class Construction(Scene):
    def construct(self):
        title = Tex("$c < -2$")
        self.play(Write(title))
        self.wait(5)
        self.play(title.animate.to_edge(UP))

        c = -2.2
        p = (1 + (1 - 4 * c) ** (1 / 2)) / 2

        grid = NumberPlane(x_range=[-3, 3, 0.5], y_range=[-3, 3, 0.5], x_length=7, y_length=7)

        self.play(DrawBorderThenFill(grid))
        self.wait(2)

        func = lambda x: x ** 2 + c

        Parabola = grid.plot(func, color=ORANGE)
        Id = grid.plot(lambda x: x)

        self.play(Create(Parabola))
        self.play(Create(Id))
        self.wait(5)

        Corners = VGroup(
            Dot(grid.coords_to_point(+p, +p)),
            Dot(grid.coords_to_point(-p, +p)),
            Dot(grid.coords_to_point(-p, -p)),
            Dot(grid.coords_to_point(+p, -p))
        )

        self.add(Corners)

        rect = VGroup(
            Line(Corners[0], Corners[1]),
            Line(Corners[1], Corners[2]),
            Line(Corners[2], Corners[3]),
            Line(Corners[3], Corners[0]),
        )

        self.play(Create(rect))
        self.wait(2)

        bv = 0.367
        Arc1 = grid.plot(func,x_range=[-bv,bv],color=PURE_BLUE)
        Line1 = grid.plot(lambda x:x,x_range=[-bv,bv],color=PURE_BLUE)
        A1 = Tex("$A_1$").next_to(Line1).scale(0.5).shift(DOWN/5)

        self.play(Create(Arc1))
        self.wait(2)
        self.play(Transform(Arc1,Line1))
        self.play(Write(A1))
        self.wait(5)

        A,B=Dot(grid.coords_to_point(-bv,-bv)),Dot(grid.coords_to_point(bv,bv))

        self.add(A,B)

        bv1 = 1.602
        bv2 = 1.354

        Line11 = Line(A, grid.coords_to_point(-bv2,-bv))
        Line12 = Line(A, grid.coords_to_point(bv2,-bv))
        Line21 = Line(B, grid.coords_to_point(-bv1, bv))
        Line22 = Line(B, grid.coords_to_point(bv1, bv))

        Line11d = Line(grid.coords_to_point(-bv2,-bv),grid.coords_to_point(-bv2,-bv2))
        Line12d = Line(grid.coords_to_point(bv2, -bv), grid.coords_to_point(bv2, bv2))
        Line21d = Line(grid.coords_to_point(-bv1, bv), grid.coords_to_point(-bv1, -bv1))
        Line22d = Line(grid.coords_to_point(bv1, bv), grid.coords_to_point(bv1, bv1))

        self.play(Create(Line11),Create(Line11d))
        self.wait(2)
        self.play(Create(Line21), Create(Line21d))
        self.wait(2)
        self.play(Create(Line22), Create(Line22d))
        self.wait(2)
        self.play(Create(Line12), Create(Line12d))
        self.wait(2)

        Arc21 = grid.plot(lambda x: x, x_range=[-bv1, -bv2], color=PURE_BLUE)
        A21 = Tex("$A_2$").next_to(Arc21).scale(0.5)

        Arc22 = grid.plot(lambda x: x, x_range=[bv2, bv1], color=PURE_BLUE)
        A22 = Tex("$A_2$").next_to(Arc22).scale(0.5).shift(DOWN/2+LEFT/2)

        self.play(Create(Arc21),Create(Arc22))
        self.play(FadeOut(A,B,Line11,Line11d,Line12,Line12d,Line21,Line21d,Line22,Line22d))
        self.play(Write(A21),Write(A22))
        self.wait(10)

        self.play(*[FadeOut(mob) for mob in self.mobjects if mob!=title])
        self.wait(5)

        final = Tex(r"$\Lambda=I \setminus \displaystyle \bigcup_{n\in \mathbb{N}^*} A_n $")
        self.play(Write(final))

        self.wait(5)


class OrbitDiag(Scene):
    def construct(self):
        title = Tex("Diagrammes d'orbite")
        self.play(Write(title))

        self.wait(5)
        self.play(FadeOut(title))

        Images = [
            ImageMobject("Image1.png"),
            ImageMobject("Image21.png").scale(2/3).shift(2*UP),
            ImageMobject("Image22.png").scale(2/3).shift(2*DOWN),
            ImageMobject("Image3.png")
        ]

        self.play(FadeIn(Images[0]))
        self.wait(5)
        self.play(FadeOut(Images[0]))
        self.play(FadeIn(Images[1],Images[2]))
        self.wait(5)
        self.play(FadeOut(Images[1], Images[2]))
        self.play(FadeIn(Images[3]))
        self.wait(5)
        self.play(FadeOut(Images[3]))


