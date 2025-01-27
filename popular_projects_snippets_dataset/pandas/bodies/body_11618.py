# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_categorical.py
# see gh-18186
parser = all_parsers
data = np.sort([str(i) for i in range(524289)])
expected = DataFrame({"a": Categorical(data, ordered=True)})

actual = parser.read_csv(StringIO("a\n" + "\n".join(data)), dtype="category")
actual["a"] = actual["a"].cat.reorder_categories(
    np.sort(actual.a.cat.categories), ordered=True
)
tm.assert_frame_equal(actual, expected)
