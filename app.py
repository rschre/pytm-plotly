from random import randint

from pytmlib import AbstractExercise
from pytmlib import Latex
from pytmlib import entrypoint


class Exercise(AbstractExercise):
    @property
    def version(self) -> str:
        return '0.1.0'

    @entrypoint
    def start(self):
        a = randint(1, 10)
        b = randint(1, 10)

        question = Latex('''
            Solve the following calculation:
            $$%d + %d = ?$$
            ''' % (a, b))

        return self.output \
            .add_paragraph(question) \
            .add_number_field('result', 'Result', step=1) \
            .add_action('Solve', self.solve, a=a, b=b)

    def solve(self, **kwargs):
        score = self.check(**kwargs)

        return self.output \
            .add_score(score) \
            .add_paragraph(f'Your score: {score}') \
            .add_action('Back to start', self.start)

    @classmethod
    def check(cls, a: int, b: int, result: int) -> float:
        return 1.0 if a + b == result else 0.0


app = Exercise()
