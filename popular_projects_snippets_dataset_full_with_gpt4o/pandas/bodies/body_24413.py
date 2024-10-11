# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
"""Generic reader of line files."""
# if we pass a date_parser and parse_dates=False, we should not parse the
# dates GH#44366
if kwds.get("parse_dates", None) is None:
    if kwds.get("date_parser", None) is None:
        kwds["parse_dates"] = False
    else:
        kwds["parse_dates"] = True

    # Extract some of the arguments (pass chunksize on).
iterator = kwds.get("iterator", False)
chunksize = kwds.get("chunksize", None)
if kwds.get("engine") == "pyarrow":
    if iterator:
        raise ValueError(
            "The 'iterator' option is not supported with the 'pyarrow' engine"
        )

    if chunksize is not None:
        raise ValueError(
            "The 'chunksize' option is not supported with the 'pyarrow' engine"
        )
elif (
    kwds.get("use_nullable_dtypes", False)
    and get_option("mode.dtype_backend") == "pyarrow"
    and kwds.get("engine") == "c"
):
    raise NotImplementedError(
        f"use_nullable_dtypes=True and engine={kwds['engine']} with "
        "mode.dtype_backend set to 'pyarrow' is not implemented."
    )
else:
    chunksize = validate_integer("chunksize", chunksize, 1)

nrows = kwds.get("nrows", None)

# Check for duplicates in names.
_validate_names(kwds.get("names", None))

# Create the parser.
parser = TextFileReader(filepath_or_buffer, **kwds)

if chunksize or iterator:
    exit(parser)

with parser:
    exit(parser.read(nrows))
