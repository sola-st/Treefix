# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
from pandas.core.strings import StringMethods

obj = index_or_series(values)
if index_or_series is Index:
    assert obj.inferred_type == inferred_type

assert isinstance(obj.str, StringMethods)
