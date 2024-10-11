# Extracted from ./data/repos/pandas/pandas/io/clipboards.py
r"""
    Read text from clipboard and pass to read_csv.

    Parameters
    ----------
    sep : str, default '\s+'
        A string or regex delimiter. The default of '\s+' denotes
        one or more whitespace characters.

    use_nullable_dtypes : bool = False
        Whether or not to use nullable dtypes as default when reading data. If
        set to True, nullable dtypes are used for all dtypes that have a nullable
        implementation, even if no nulls are present.

        The nullable dtype implementation can be configured by calling
        ``pd.set_option("mode.dtype_backend", "pandas")`` to use
        numpy-backed nullable dtypes or
        ``pd.set_option("mode.dtype_backend", "pyarrow")`` to use
        pyarrow-backed nullable dtypes (using ``pd.ArrowDtype``).
        This is only implemented for the ``python``
        engine.

        .. versionadded:: 2.0

    **kwargs
        See read_csv for the full argument list.

    Returns
    -------
    DataFrame
        A parsed DataFrame object.
    """
encoding = kwargs.pop("encoding", "utf-8")

# only utf-8 is valid for passed value because that's what clipboard
# supports
if encoding is not None and encoding.lower().replace("-", "") != "utf8":
    raise NotImplementedError("reading from clipboard only supports utf-8 encoding")

from pandas.io.clipboard import clipboard_get
from pandas.io.parsers import read_csv

text = clipboard_get()

# Try to decode (if needed, as "text" might already be a string here).
try:
    text = text.decode(kwargs.get("encoding") or get_option("display.encoding"))
except AttributeError:
    pass

# Excel copies into clipboard with \t separation
# inspect no more then the 10 first lines, if they
# all contain an equal number (>0) of tabs, infer
# that this came from excel and set 'sep' accordingly
lines = text[:10000].split("\n")[:-1][:10]

# Need to remove leading white space, since read_csv
# accepts:
#    a  b
# 0  1  2
# 1  3  4

counts = {x.lstrip(" ").count("\t") for x in lines}
if len(lines) > 1 and len(counts) == 1 and counts.pop() != 0:
    sep = "\t"
    # check the number of leading tabs in the first line
    # to account for index columns
    index_length = len(lines[0]) - len(lines[0].lstrip(" \t"))
    if index_length != 0:
        kwargs.setdefault("index_col", list(range(index_length)))

    # Edge case where sep is specified to be None, return to default
if sep is None and kwargs.get("delim_whitespace") is None:
    sep = r"\s+"

# Regex separator currently only works with python engine.
# Default to python if separator is multi-character (regex)
if len(sep) > 1 and kwargs.get("engine") is None:
    kwargs["engine"] = "python"
elif len(sep) > 1 and kwargs.get("engine") == "c":
    warnings.warn(
        "read_clipboard with regex separator does not work properly with c engine.",
        stacklevel=find_stack_level(),
    )

exit(read_csv(
    StringIO(text), sep=sep, use_nullable_dtypes=use_nullable_dtypes, **kwargs
))
