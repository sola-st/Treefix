from typing import Callable # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.verbose = True # pragma: no cover
def out(message: str, bold: bool = False): print(message if not bold else f'\033[1m{message}\033[0m') # pragma: no cover
path = '/some/path/to/file' # pragma: no cover
message = 'this is a test message' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/report.py
from l3.Runtime import _l_
if self.verbose:
    _l_(5383)

    out(f"{path} ignored: {message}", bold=False)
    _l_(5382)
