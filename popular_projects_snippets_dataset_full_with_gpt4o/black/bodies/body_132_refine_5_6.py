from operator import attrgetter # pragma: no cover
from hashlib import sha256 # pragma: no cover

self = type('Mock', (object,), { # pragma: no cover
    'target_versions': [type('Version', (object,), {'value': v})() for v in [3, 6, 9]], # pragma: no cover
    'line_length': 80, # pragma: no cover
    'string_normalization': True, # pragma: no cover
    'is_pyi': False, # pragma: no cover
    'is_ipynb': False, # pragma: no cover
    'skip_source_first_line': False, # pragma: no cover
    'magic_trailing_comma': True, # pragma: no cover
    'experimental_string_processing': False, # pragma: no cover
    'preview': True, # pragma: no cover
    'python_cell_magics': ['%%time', '%%capture'] # pragma: no cover
}) # pragma: no cover

from operator import attrgetter # pragma: no cover
from hashlib import sha256 # pragma: no cover

class Version: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'target_versions': [Version(1), Version(2)], # pragma: no cover
    'line_length': 88, # pragma: no cover
    'string_normalization': True, # pragma: no cover
    'is_pyi': False, # pragma: no cover
    'is_ipynb': False, # pragma: no cover
    'skip_source_first_line': True, # pragma: no cover
    'magic_trailing_comma': True, # pragma: no cover
    'experimental_string_processing': False, # pragma: no cover
    'preview': True, # pragma: no cover
    'python_cell_magics': {'timeit', 'display'} # pragma: no cover
})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/mode.py
from l3.Runtime import _l_
if self.target_versions:
    _l_(17672)

    version_str = ",".join(
        str(version.value)
        for version in sorted(self.target_versions, key=attrgetter("value"))
    )
    _l_(17670)
else:
    version_str = "-"
    _l_(17671)
parts = [
    version_str,
    str(self.line_length),
    str(int(self.string_normalization)),
    str(int(self.is_pyi)),
    str(int(self.is_ipynb)),
    str(int(self.skip_source_first_line)),
    str(int(self.magic_trailing_comma)),
    str(int(self.experimental_string_processing)),
    str(int(self.preview)),
    sha256((",".join(sorted(self.python_cell_magics))).encode()).hexdigest(),
]
_l_(17673)
aux = ".".join(parts)
_l_(17674)
exit(aux)
