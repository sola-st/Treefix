# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string_arrow.py
import pyarrow as pa

arr = ArrowStringArray(pa.array(list("abcde")))

with pytest.raises(IndexError, match=None):
    arr[5] = "foo"

with pytest.raises(IndexError, match=None):
    arr[-6] = "foo"

with pytest.raises(IndexError, match=None):
    arr[[0, 5]] = "foo"

with pytest.raises(IndexError, match=None):
    arr[[0, -6]] = "foo"

with pytest.raises(IndexError, match=None):
    arr[[True, True, False]] = "foo"

with pytest.raises(ValueError, match=None):
    arr[[0, 1]] = ["foo", "bar", "baz"]
