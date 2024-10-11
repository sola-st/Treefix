# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3263672/the-difference-between-sys-stdout-write-and-print
from l3.Runtime import _l_
def myfunc(outfile=None):
    _l_(13906)

    if outfile is None:
        _l_(13900)

        out = sys.stdout
        _l_(13898)
    else:
        out = open(outfile, 'w')
        _l_(13899)
    try:
        _l_(13905)

        # do some stuff
        out.write(mytext + '\n')
        _l_(13901)
    finally:
        _l_(13904)

        if outfile is not None:
            _l_(13903)

            out.close()
            _l_(13902)

