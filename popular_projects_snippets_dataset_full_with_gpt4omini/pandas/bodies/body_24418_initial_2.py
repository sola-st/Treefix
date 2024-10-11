import warnings # pragma: no cover
import pandas as pd # pragma: no cover
from typing import Optional # pragma: no cover

infer_datetime_format = None # pragma: no cover
lib = type('Mock', (object,), {'no_default': object()})() # pragma: no cover
find_stack_level = lambda: 1 # pragma: no cover
def _refine_defaults_read(*args, **kwargs): return {'delimiter': kwargs.get('delimiter', ',')} # pragma: no cover
dialect = None # pragma: no cover
delimiter = ',' # pragma: no cover
delim_whitespace = False # pragma: no cover
engine = 'python' # pragma: no cover
sep = ',' # pragma: no cover
on_bad_lines = 'raise' # pragma: no cover
names = None # pragma: no cover
_read = lambda filepath, kwds: 'Reading data from {}'.format(filepath) # pragma: no cover
filepath_or_buffer = 'example.csv' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
from l3.Runtime import _l_
if infer_datetime_format is not lib.no_default:
    _l_(5065)

    warnings.warn(
        "The argument 'infer_datetime_format' is deprecated and will "
        "be removed in a future version. "
        "A strict version of it is now the default, see "
        "https://pandas.pydata.org/pdeps/0004-consistent-to-datetime-parsing.html. "
        "You can safely remove this argument.",
        stacklevel=find_stack_level(),
    )
    _l_(5064)
# locals() should never be modified
kwds = locals().copy()
_l_(5066)
del kwds["filepath_or_buffer"]
_l_(5067)
del kwds["sep"]
_l_(5068)

kwds_defaults = _refine_defaults_read(
    dialect,
    delimiter,
    delim_whitespace,
    engine,
    sep,
    on_bad_lines,
    names,
    defaults={"delimiter": ","},
)
_l_(5069)
kwds.update(kwds_defaults)
_l_(5070)
aux = _read(filepath_or_buffer, kwds)
_l_(5071)

exit(aux)
