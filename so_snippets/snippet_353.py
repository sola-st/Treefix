# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/855759/what-is-the-intended-use-of-the-optional-else-clause-of-the-try-statement-in
from l3.Runtime import _l_
try:
    _l_(1427)

    do_init_stuff()
    _l_(1420)
except:
    _l_(1422)

    handle_init_suff_execption()
    _l_(1421)
else:
    try:
        _l_(1426)

        do_middle_stuff()
        _l_(1423)
    except:
        _l_(1425)

        handle_middle_stuff_exception()
        _l_(1424)

