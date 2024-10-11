# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
with tm.ensure_clean("foo.xlsx") as path:
    with ExcelWriter(path) as writer:
        assert os.fspath(writer) == str(path)
