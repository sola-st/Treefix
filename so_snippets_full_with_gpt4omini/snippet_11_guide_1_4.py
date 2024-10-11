# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/136097/difference-between-staticmethod-and-classmethod
from l3.Runtime import _l_
class Apple:
    _l_(1533)


    _counter = 0
    _l_(1523)

    @staticmethod
    def about_apple():
        _l_(1525)

        print('Apple is good for you.')
        _l_(1524)

    @classmethod
    def make_apple_juice(cls, number_of_apples):
        _l_(1529)

        print('Making juice:')
        _l_(1526)
        for i in range(number_of_apples):
            _l_(1528)

            cls._juice_this(i)
            _l_(1527)

    @classmethod
    def _juice_this(cls, apple):
        _l_(1532)

        print('Juicing apple %d...' % apple)
        _l_(1530)
        cls._counter += 1
        _l_(1531)

