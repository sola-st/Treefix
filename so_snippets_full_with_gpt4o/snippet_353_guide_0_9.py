class MockInitError(Exception): pass # pragma: no cover
class MockMiddleError(Exception): pass # pragma: no cover
def do_init_stuff(): raise MockInitError('Initial error') # pragma: no cover
def handle_init_suff_execption(): print('Init exception handled') # pragma: no cover
def do_middle_stuff(): raise MockMiddleError('Middle error') # pragma: no cover
def handle_middle_stuff_exception(): print('Middle exception handled') # pragma: no cover

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

