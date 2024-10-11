from pathlib import Path # pragma: no cover
import os # pragma: no cover
import errno # pragma: no cover

directory = '/my/directory' # pragma: no cover

from pathlib import Path # pragma: no cover
import os # pragma: no cover
import errno # pragma: no cover

directory = 'my_test_directory' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8933237/how-do-i-check-if-directory-exists-in-python
from l3.Runtime import _l_
try:
    from pathlib import Path
    _l_(550)

except ImportError:
    pass
Path("/my/directory").mkdir(parents=True, exist_ok=True)
_l_(551)
try:
    import os
    _l_(553)

except ImportError:
    pass
if not os.path.exists(directory):
    _l_(555)

    os.makedirs(directory)
    _l_(554)
try:
    import os, errno
    _l_(557)

except ImportError:
    pass

try:
    _l_(562)

    os.makedirs(directory)
    _l_(558)
except OSError as e:
    _l_(561)

    if e.errno != errno.EEXIST:
        _l_(560)

        raise
        _l_(559)

try:
    _l_(566)

    os.makedirs("path/to/directory")
    _l_(563)
except FileExistsError:
    _l_(565)

    # directory already exists
    pass
    _l_(564)

os.makedirs("path/to/directory", exist_ok=True)  # succeeds even if directory exists.
_l_(567)  # succeeds even if directory exists.

