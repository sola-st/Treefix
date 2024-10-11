# Extracted from ./data/repos/pandas/pandas/tests/io/test_orc.py
columns = [
    "boolean1",
    "byte1",
    "short1",
    "int1",
    "long1",
    "float1",
    "double1",
    "bytes1",
    "string1",
]
dtypes = [
    "bool",
    "int8",
    "int16",
    "int32",
    "int64",
    "float32",
    "float64",
    "object",
    "object",
]
expected = pd.DataFrame(index=pd.RangeIndex(0))
for colname, dtype in zip(columns, dtypes):
    expected[colname] = pd.Series(dtype=dtype)

inputfile = os.path.join(dirpath, "TestOrcFile.emptyFile.orc")
got = read_orc(inputfile, columns=columns)

tm.assert_equal(expected, got)
