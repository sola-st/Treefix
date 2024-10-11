import sys # pragma: no cover

sys.version_info = (3, 8, 5, 'final', 0) # pragma: no cover
sys.argv = ['test_script.py'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9079036/how-do-i-detect-the-python-version-at-runtime
from l3.Runtime import _l_
def check_installation(rv):
    _l_(14688)

    current_version = sys.version_info
    _l_(14682)
    if current_version[0] == rv[0] and current_version[1] >= rv[1]:
        _l_(14686)

        pass
        _l_(14683)
    else:
        sys.stderr.write( "[%s] - Error: Your Python interpreter must be %d.%d or greater (within major version %d)\n" % (sys.argv[0], rv[0], rv[1], rv[0]) )
        _l_(14684)
        sys.exit(-1)
        _l_(14685)
    aux = 0
    _l_(14687)
    return aux


# Calling the 'check_installation' function checks if Python is >= 2.7 and < 3
required_version = (2,7)
_l_(14689)
check_installation(required_version)
_l_(14690)

