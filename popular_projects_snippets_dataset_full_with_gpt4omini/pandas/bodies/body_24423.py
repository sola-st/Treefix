# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
# locals() should never be modified
kwds = locals().copy()
del kwds["filepath_or_buffer"]
del kwds["sep"]

kwds_defaults = _refine_defaults_read(
    dialect,
    delimiter,
    delim_whitespace,
    engine,
    sep,
    on_bad_lines,
    names,
    defaults={"delimiter": "\t"},
)
kwds.update(kwds_defaults)

exit(_read(filepath_or_buffer, kwds))
