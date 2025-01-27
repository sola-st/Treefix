# Extracted from ./data/repos/pandas/pandas/tests/extension/test_string.py
# GH 27673
pytest.importorskip("pyarrow", minversion="1.0.0")
result = pd.Series(["E"], dtype=StringDtype(storage="pyarrow"))
assert isinstance(result.dtype, StringDtype)
assert result.dtype.storage == "pyarrow"
