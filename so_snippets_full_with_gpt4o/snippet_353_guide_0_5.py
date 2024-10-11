do_init_stuff = lambda: (_ for _ in ()).throw(Exception('Initialization failed')) # pragma: no cover
handle_init_suff_execption = lambda: print('Initialization exception handled') # pragma: no cover
do_middle_stuff = lambda: print('Middle stuff done') # pragma: no cover
handle_middle_stuff_exception = lambda: print('Middle stuff exception handled') # pragma: no cover

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

