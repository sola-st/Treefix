# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
from l3.Runtime import _l_
if infer_datetime_format is not lib.no_default:
    _l_(16739)

    warnings.warn(
        "The argument 'infer_datetime_format' is deprecated and will "
        "be removed in a future version. "
        "A strict version of it is now the default, see "
        "https://pandas.pydata.org/pdeps/0004-consistent-to-datetime-parsing.html. "
        "You can safely remove this argument.",
        stacklevel=find_stack_level(),
    )
    _l_(16738)
# locals() should never be modified
kwds = locals().copy()
_l_(16740)
del kwds["filepath_or_buffer"]
_l_(16741)
del kwds["sep"]
_l_(16742)

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
_l_(16743)
kwds.update(kwds_defaults)
_l_(16744)
aux = _read(filepath_or_buffer, kwds)
_l_(16745)

exit(aux)
