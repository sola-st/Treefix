# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/136097/difference-between-staticmethod-and-classmethod
from l3.Runtime import _l_
class Apple:
    _l_(13570)


    _counter = 0
    _l_(13560)

    @staticmethod
    def about_apple():
        _l_(13562)

        print('Apple is good for you.')
        _l_(13561)

    @classmethod
    def make_apple_juice(cls, number_of_apples):
        _l_(13566)

        print('Making juice:')
        _l_(13563)
        for i in range(number_of_apples):
            _l_(13565)

            cls._juice_this(i)
            _l_(13564)

    @classmethod
    def _juice_this(cls, apple):
        _l_(13569)

        print('Juicing apple %d...' % apple)
        _l_(13567)
        cls._counter += 1
        _l_(13568)

