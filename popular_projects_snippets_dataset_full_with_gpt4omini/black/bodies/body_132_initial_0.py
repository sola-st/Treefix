from hashlib import sha256 # pragma: no cover
from operator import attrgetter # pragma: no cover

self = type('Mock', (object,), { 'target_versions': [], 'line_length': 80, 'string_normalization': True, 'is_pyi': False, 'is_ipynb': False, 'skip_source_first_line': False, 'magic_trailing_comma': True, 'experimental_string_processing': False, 'preview': False, 'python_cell_magics': [] })() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/mode.py
from l3.Runtime import _l_
if self.target_versions:
    _l_(6232)

    version_str = ",".join(
        str(version.value)
        for version in sorted(self.target_versions, key=attrgetter("value"))
    )
    _l_(6230)
else:
    version_str = "-"
    _l_(6231)
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
_l_(6233)
aux = ".".join(parts)
_l_(6234)
exit(aux)
