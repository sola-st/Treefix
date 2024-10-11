class Mock(object): # pragma: no cover
    def do_init_stuff(self): # pragma: no cover
        raise Exception('Initialization failure') # pragma: no cover
    def handle_init_suff_execption(self): # pragma: no cover
        print('Handled init exception') # pragma: no cover
    def do_middle_stuff(self): # pragma: no cover
        pass # pragma: no cover
    def handle_middle_stuff_exception(self): # pragma: no cover
        pass # pragma: no cover
mock = Mock() # pragma: no cover
do_init_stuff = mock.do_init_stuff # pragma: no cover
handle_init_suff_execption = mock.handle_init_suff_execption # pragma: no cover
do_middle_stuff = mock.do_middle_stuff # pragma: no cover
handle_middle_stuff_exception = mock.handle_middle_stuff_exception # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/855759/what-is-the-intended-use-of-the-optional-else-clause-of-the-try-statement-in
from l3.Runtime import _l_
try:
    _l_(13590)

    do_init_stuff()
    _l_(13583)
except:
    _l_(13585)

    handle_init_suff_execption()
    _l_(13584)
else:
    try:
        _l_(13589)

        do_middle_stuff()
        _l_(13586)
    except:
        _l_(13588)

        handle_middle_stuff_exception()
        _l_(13587)

