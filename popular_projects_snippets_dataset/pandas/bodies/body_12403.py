# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
with pd.read_csv(StringIO(self.data1), chunksize=1) as reader:
    result = pd.concat(reader, ignore_index=True)
expected = pd.read_csv(StringIO(self.data1))
tm.assert_frame_equal(result, expected)

# GH12153
with pd.read_csv(StringIO(self.data1), chunksize=1) as it:
    first = next(it)
    tm.assert_frame_equal(first, expected.iloc[[0]])
    tm.assert_frame_equal(pd.concat(it), expected.iloc[1:])
