import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        list(map(lambda color, count:
                 list(map(lambda _: self.contents.append(color), range(count))),
                 kwargs.keys(), kwargs.values()))

        self.__initial_contents = copy.copy(self.contents)

    def draw(self, count):
        if len(self.contents) == 0:
            self.initial_state()

        if len(self.contents) >= count:
            drawn = random.sample(self.contents, count)
            list(map(lambda item: self.contents.remove(item), drawn))
        else:
            drawn = self.contents

        return drawn

    def initial_state(self):
        self.contents = copy.copy(self.__initial_contents)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_count = 0
    expected = next(map(lambda color, count:
                        list(map(lambda _: color, range(count))),
                        expected_balls.keys(), expected_balls.values()))

    for _ in range(num_experiments):
        hat.initial_state()
        drawn = hat.draw(num_balls_drawn)

        try:
            list(map(lambda color: drawn.remove(color), expected))
            expected_count += 1
        except ValueError:
            pass

    probability = expected_count / num_experiments

    return probability
