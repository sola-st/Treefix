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
