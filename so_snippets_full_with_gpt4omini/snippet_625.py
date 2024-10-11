# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3263672/the-difference-between-sys-stdout-write-and-print
from l3.Runtime import _l_
def myfunc(outfile=None):
    _l_(2353)

    if outfile is None:
        _l_(2347)

        out = sys.stdout
        _l_(2345)
    else:
        out = open(outfile, 'w')
        _l_(2346)
    try:
        _l_(2352)

        # do some stuff
        out.write(mytext + '\n')
        _l_(2348)
    finally:
        _l_(2351)

        if outfile is not None:
            _l_(2350)

            out.close()
            _l_(2349)

