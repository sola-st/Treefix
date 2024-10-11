directory = '/my/test/directory' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8933237/how-do-i-check-if-directory-exists-in-python
from l3.Runtime import _l_
try:
    from pathlib import Path
    _l_(12554)

except ImportError:
    pass
Path("/my/directory").mkdir(parents=True, exist_ok=True)
_l_(12555)
try:
    import os
    _l_(12557)

except ImportError:
    pass
if not os.path.exists(directory):
    _l_(12559)

    os.makedirs(directory)
    _l_(12558)
try:
    import os, errno
    _l_(12561)

except ImportError:
    pass

try:
    _l_(12566)

    os.makedirs(directory)
    _l_(12562)
except OSError as e:
    _l_(12565)

    if e.errno != errno.EEXIST:
        _l_(12564)

        raise
        _l_(12563)

try:
    _l_(12570)

    os.makedirs("path/to/directory")
    _l_(12567)
except FileExistsError:
    _l_(12569)

    # directory already exists
    pass
    _l_(12568)

os.makedirs("path/to/directory", exist_ok=True)  # succeeds even if directory exists.
_l_(12571)  # succeeds even if directory exists.

