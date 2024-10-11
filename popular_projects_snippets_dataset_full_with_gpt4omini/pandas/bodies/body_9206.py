# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_missing.py
# https://github.com/pandas-dev/pandas/issues/21097
if named:
    Point = collections.namedtuple("Point", "x y")
else:
    Point = lambda *args: args  # tuple
cat = Categorical(np.array([Point(0, 0), Point(0, 1), None], dtype=object))
result = cat.fillna(Point(0, 0))
expected = Categorical([Point(0, 0), Point(0, 1), Point(0, 0)])

tm.assert_categorical_equal(result, expected)

# Case where the Point is not among our categories; we want ValueError,
#  not NotImplementedError GH#41914
cat = Categorical(np.array([Point(1, 0), Point(0, 1), None], dtype=object))
msg = "Cannot setitem on a Categorical with a new category"
with pytest.raises(TypeError, match=msg):
    cat.fillna(Point(0, 0))
