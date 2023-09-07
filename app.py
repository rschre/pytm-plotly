from collections import namedtuple
from math import sqrt, pi
from random import randint, randrange

from matplotlib.figure import Figure
from pytmlib import AbstractExercise
from pytmlib import Latex
from pytmlib import entrypoint


class Exercise(AbstractExercise):
    EP = 8.854187817e-12

    @property
    def version(self) -> str:
        return "0.1.0"

    @entrypoint
    def start(self):
        q_1 = {
            "q": round(randrange(-100, 100) * 1e-7, 8),
            "x": randint(-10, 10),
            "y": randint(-10, 10),
        }
        q_2 = {
            "q": round(randrange(-100, 100) * 1e-7, 8),
            "x": randint(-10, 10),
            "y": randint(-10, 10),
        }
        q_3 = {
            "q": round(randrange(-100, 100) * 1e-7, 8),
            "x": randint(-10, 10),
            "y": randint(-10, 10),
        }

        A = {"x": randint(-10, 10), "y": randint(-10, 10)}

        figure = self._get_figure(q_1, q_2, q_3, A)

        r_1A = self._get_directional_vector(q_1["x"], q_1["y"], A["x"], A["y"])
        r_2A = self._get_directional_vector(q_2["x"], q_2["y"], A["x"], A["y"])
        r_3A = self._get_directional_vector(q_3["x"], q_3["y"], A["x"], A["y"])

        question = Latex(
            r"""
            Berechnen Sie das E-Feld im Punkt A({x_A}, {y_A}).
            Koordinaten sind in Centimeter angegeben.
            """.format(
                x_A=A["x"], y_A=A["y"]
            )
        )

        charges = Latex(
            r"""
            Die Ladungen sind wie folgt gegeben (in Coulomb)):
            \\q1: {q1} C ({x1}, {y1})
            \\q2: {q2} C ({x2}, {y2})
            \\q3: {q3} C ({x3}, {y3})
            """.format(
                q1=q_1["q"],
                q2=q_2["q"],
                q3=q_3["q"],
                x1=q_1["x"],
                x2=q_2["x"],
                x3=q_3["x"],
                y1=q_1["y"],
                y2=q_2["y"],
                y3=q_3["y"],
            )
        )

        return (
            self.output.add_paragraph(question)
            .add_paragraph(charges)
            .add_figure(figure)
            .add_action(
                "Solve",
                self.solve,
                q1=q_1,
                q2=q_2,
                q3=q_3,
                r1A=r_1A,
                r2A=r_2A,
                r3A=r_3A,
            )
        )

    def solve(self, **kwargs):
        result = self._get_resulting_field(**kwargs)

        return self.output.add_paragraph(
            Latex(
                r"""
                    $\overrightarrow{E_x} = $"""
                + " "
                + str(int(result["x"]))
                + r""" $\frac{N}{C}$ \\
                    $\overrightarrow{E_y} = $"""
                + " "
                + str(int(result["y"]))
                + r""" $\frac{N}{C}$ \\
                    $\overrightarrow{E} = $"""
                + " "
                + str(int(sqrt(result["x"] ** 2 + result["y"] ** 2)))
                + r""" $\frac{N}{C}$ \\
                """
            )
        ).add_action("Back to start", self.start)

    @staticmethod
    def _get_figure(q_1, q_2, q_3, A):
        figure = Figure()
        axes = figure.add_subplot(1, 1, 1)

        axes.set_xlabel("x [cm]")
        axes.set_ylabel("y [cm]")
        axes.set_ylim(-12, 12)
        axes.set_xlim(-12, 12)
        axes.set_title("Berechnung E-Feld")

        for q in [q_1, q_2, q_3]:
            if q["q"] < 0:
                axes.plot(q["x"], q["y"], "ro")
            else:
                axes.plot(q["x"], q["y"], "bo")

        axes.plot(A["x"], A["y"], color="green", marker="s")

        axes.text(q_1["x"] + 1, q_1["y"], "q1")
        axes.text(q_2["x"] + 1, q_2["y"], "q2")
        axes.text(q_3["x"] + 1, q_3["y"], "q3")
        axes.text(A["x"] + 1, A["y"], "A")
        axes.grid()

        return figure

    @staticmethod
    def _get_directional_vector(x0, y0, x1, y1):
        x = (x1 - x0) * 0.01
        y = (y1 - y0) * 0.01
        value = sqrt(x * x + y * y)

        return {
            "x": x,
            "y": y,
            "value": value,
        }

    @staticmethod
    def _get_resulting_field(q1, q2, q3, r1A, r2A, r3A):
        E_1A_x = q1["q"] * r1A["x"] / (4 * pi * Exercise.EP * r1A["value"] ** 3)
        E_1A_y = q1["q"] * r1A["y"] / (4 * pi * Exercise.EP * r1A["value"] ** 3)
        E_2A_x = q2["q"] * r2A["x"] / (4 * pi * Exercise.EP * r2A["value"] ** 3)
        E_2A_y = q2["q"] * r2A["y"] / (4 * pi * Exercise.EP * r2A["value"] ** 3)
        E_3A_x = q3["q"] * r3A["x"] / (4 * pi * Exercise.EP * r3A["value"] ** 3)
        E_3A_y = q3["q"] * r3A["y"] / (4 * pi * Exercise.EP * r3A["value"] ** 3)

        E_A_x = E_1A_x + E_2A_x + E_3A_x
        E_A_y = E_1A_y + E_2A_y + E_3A_y

        return {"x": round(E_A_x, 2), "y": round(E_A_y, 2)}


app = Exercise()
