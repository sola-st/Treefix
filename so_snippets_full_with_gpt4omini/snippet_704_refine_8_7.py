import sys # pragma: no cover

sys = type('MockSys', (object,), {'version_info': (3, 8, 0), 'stderr': open('/dev/null', 'w'), 'argv': ['script.py'], 'exit': exit})() # pragma: no cover

import sys # pragma: no cover

sys = type('MockSys', (object,), {'version_info': (2, 7, 18), 'stderr': open('/dev/null', 'w'), 'argv': ['script.py'], 'exit': exit})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9079036/how-do-i-detect-the-python-version-at-runtime
from l3.Runtime import _l_
def check_installation(rv):
    _l_(2991)

    current_version = sys.version_info
    _l_(2985)
    if current_version[0] == rv[0] and current_version[1] >= rv[1]:
        _l_(2989)

        pass
        _l_(2986)
    else:
        sys.stderr.write( "[%s] - Error: Your Python interpreter must be %d.%d or greater (within major version %d)\n" % (sys.argv[0], rv[0], rv[1], rv[0]) )
        _l_(2987)
        sys.exit(-1)
        _l_(2988)
    aux = 0
    _l_(2990)
    return aux


# Calling the 'check_installation' function checks if Python is >= 2.7 and < 3
required_version = (2,7)
_l_(2992)
check_installation(required_version)
_l_(2993)

