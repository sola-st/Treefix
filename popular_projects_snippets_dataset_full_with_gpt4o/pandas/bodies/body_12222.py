# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_unsupported.py
from pandas.io.parsers.readers import _python_unsupported as py_unsupported

data = """1,2,3,,
1,2,3,4,
1,2,3,4,5
1,2,,,
1,2,3,4,"""

for default in py_unsupported:
    msg = (
        f"The {repr(default)} option is not "
        f"supported with the {repr(python_engine)} engine"
    )

    kwargs = {default: object()}
    with pytest.raises(ValueError, match=msg):
        read_csv(StringIO(data), engine=python_engine, **kwargs)
