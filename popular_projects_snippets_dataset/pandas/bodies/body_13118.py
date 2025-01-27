# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
with tm.ensure_clean("foo.xlsx") as path:
    df = DataFrame({"A": [1, 2]})
    df.to_excel(path)
    with ExcelFile(path) as xl:
        result = os.fspath(xl)
    assert result == path
