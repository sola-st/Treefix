# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_chunksize.py
parser = all_parsers
integers = [str(i) for i in range(499999)]
data = "a\n" + "\n".join(integers + ["1.0", "2.0"] + integers)

# Coercions should work without warnings.
with tm.assert_produces_warning(None):
    result = parser.read_csv(StringIO(data))

assert type(result.a[0]) is np.float64
assert result.a.dtype == float
