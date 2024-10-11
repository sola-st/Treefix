# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_textreader.py
data = "skip this\nskip this\na,b,c\n1,2,3\n4,5,6"

reader = TextReader(StringIO(data), delimiter=",", header=2)
header = reader.header
expected = [["a", "b", "c"]]
assert header == expected

recs = reader.read()
expected = {
    0: np.array([1, 4], dtype=np.int64),
    1: np.array([2, 5], dtype=np.int64),
    2: np.array([3, 6], dtype=np.int64),
}
assert_array_dicts_equal(recs, expected)
