import sys # pragma: no cover

class MockSysVersionInfo:# pragma: no cover
    def __init__(self, major, minor):# pragma: no cover
        self.major = major# pragma: no cover
        self.minor = minor# pragma: no cover
# pragma: no cover
    def __getitem__(self, index):# pragma: no cover
        return (self.major, self.minor)[index]# pragma: no cover
# pragma: no cover
sys.version_info = MockSysVersionInfo(3, 9) # pragma: no cover
def parse_single_version(src, version):# pragma: no cover
    if isinstance(src, str) and isinstance(version, tuple):# pragma: no cover
        return 0# pragma: no cover
    else:# pragma: no cover
        raise SyntaxError('Invalid version or source') # pragma: no cover
src = 'print("Hello, World!")' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/parsing.py
# TODO: support Python 4+ ;)
from l3.Runtime import _l_
versions = [(3, minor) for minor in range(3, sys.version_info[1] + 1)]
_l_(17626)

first_error = ""
_l_(17627)
for version in sorted(versions, reverse=True):
    _l_(17633)

    try:
        _l_(17632)

        aux = parse_single_version(src, version)
        _l_(17628)
        exit(aux)
    except SyntaxError as e:
        _l_(17631)

        if not first_error:
            _l_(17630)

            first_error = str(e)
            _l_(17629)

raise SyntaxError(first_error)
_l_(17634)
