# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_unsupported.py
from pandas.io.parsers.readers import _pyarrow_unsupported as pa_unsupported

data = """1,2,3,,
        1,2,3,4,
        1,2,3,4,5
        1,2,,,
        1,2,3,4,"""

for default in pa_unsupported:
    msg = (
        f"The {repr(default)} option is not "
        f"supported with the 'pyarrow' engine"
    )
    kwargs = {default: object()}
    default_needs_bool = {"warn_bad_lines", "error_bad_lines"}
    if default == "dialect":
        kwargs[default] = "excel"  # test a random dialect
    elif default in default_needs_bool:
        kwargs[default] = True
    elif default == "on_bad_lines":
        kwargs[default] = "warn"
    with pytest.raises(ValueError, match=msg):
        read_csv(StringIO(data), engine="pyarrow", **kwargs)
