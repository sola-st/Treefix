self = type('Mock', (object,), {'verbose': True})() # pragma: no cover
out = lambda msg, bold: print(msg) # pragma: no cover
path = '/some/path' # pragma: no cover
message = 'Some message' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/report.py
from l3.Runtime import _l_
if self.verbose:
    _l_(16877)

    out(f"{path} ignored: {message}", bold=False)
    _l_(16876)
