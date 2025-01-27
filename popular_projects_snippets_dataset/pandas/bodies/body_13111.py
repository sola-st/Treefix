# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
with pytest.raises(ValueError, match="No engine"):
    ExcelWriter("nothing")
