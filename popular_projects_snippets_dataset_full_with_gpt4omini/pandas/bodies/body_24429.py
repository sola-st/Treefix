# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
result = options.copy()

fallback_reason = None

# C engine not supported yet
if engine == "c":
    if options["skipfooter"] > 0:
        fallback_reason = "the 'c' engine does not support skipfooter"
        engine = "python"

sep = options["delimiter"]
delim_whitespace = options["delim_whitespace"]

if sep is None and not delim_whitespace:
    if engine in ("c", "pyarrow"):
        fallback_reason = (
            f"the '{engine}' engine does not support "
            "sep=None with delim_whitespace=False"
        )
        engine = "python"
elif sep is not None and len(sep) > 1:
    if engine == "c" and sep == r"\s+":
        result["delim_whitespace"] = True
        del result["delimiter"]
    elif engine not in ("python", "python-fwf"):
        # wait until regex engine integrated
        fallback_reason = (
            f"the '{engine}' engine does not support "
            "regex separators (separators > 1 char and "
            r"different from '\s+' are interpreted as regex)"
        )
        engine = "python"
elif delim_whitespace:
    if "python" in engine:
        result["delimiter"] = r"\s+"
elif sep is not None:
    encodeable = True
    encoding = sys.getfilesystemencoding() or "utf-8"
    try:
        if len(sep.encode(encoding)) > 1:
            encodeable = False
    except UnicodeDecodeError:
        encodeable = False
    if not encodeable and engine not in ("python", "python-fwf"):
        fallback_reason = (
            f"the separator encoded in {encoding} "
            f"is > 1 char long, and the '{engine}' engine "
            "does not support such separators"
        )
        engine = "python"

quotechar = options["quotechar"]
if quotechar is not None and isinstance(quotechar, (str, bytes)):
    if (
        len(quotechar) == 1
        and ord(quotechar) > 127
        and engine not in ("python", "python-fwf")
    ):
        fallback_reason = (
            "ord(quotechar) > 127, meaning the "
            "quotechar is larger than one byte, "
            f"and the '{engine}' engine does not support such quotechars"
        )
        engine = "python"

if fallback_reason and self._engine_specified:
    raise ValueError(fallback_reason)

if engine == "c":
    for arg in _c_unsupported:
        del result[arg]

if "python" in engine:
    for arg in _python_unsupported:
        if fallback_reason and result[arg] != _c_parser_defaults[arg]:
            raise ValueError(
                "Falling back to the 'python' engine because "
                f"{fallback_reason}, but this causes {repr(arg)} to be "
                "ignored as it is not supported by the 'python' engine."
            )
        del result[arg]

if fallback_reason:
    warnings.warn(
        (
            "Falling back to the 'python' engine because "
            f"{fallback_reason}; you can avoid this warning by specifying "
            "engine='python'."
        ),
        ParserWarning,
        stacklevel=find_stack_level(),
    )

index_col = options["index_col"]
names = options["names"]
converters = options["converters"]
na_values = options["na_values"]
skiprows = options["skiprows"]

validate_header_arg(options["header"])

if index_col is True:
    raise ValueError("The value of index_col couldn't be 'True'")
if is_index_col(index_col):
    if not isinstance(index_col, (list, tuple, np.ndarray)):
        index_col = [index_col]
result["index_col"] = index_col

names = list(names) if names is not None else names

# type conversion-related
if converters is not None:
    if not isinstance(converters, dict):
        raise TypeError(
            "Type converters must be a dict or subclass, "
            f"input was a {type(converters).__name__}"
        )
else:
    converters = {}

# Converting values to NA
keep_default_na = options["keep_default_na"]
na_values, na_fvalues = _clean_na_values(na_values, keep_default_na)

# handle skiprows; this is internally handled by the
# c-engine, so only need for python and pyarrow parsers
if engine == "pyarrow":
    if not is_integer(skiprows) and skiprows is not None:
        # pyarrow expects skiprows to be passed as an integer
        raise ValueError(
            "skiprows argument must be an integer when using "
            "engine='pyarrow'"
        )
else:
    if is_integer(skiprows):
        skiprows = list(range(skiprows))
    if skiprows is None:
        skiprows = set()
    elif not callable(skiprows):
        skiprows = set(skiprows)

        # put stuff back
result["names"] = names
result["converters"] = converters
result["na_values"] = na_values
result["na_fvalues"] = na_fvalues
result["skiprows"] = skiprows

exit((result, engine))
