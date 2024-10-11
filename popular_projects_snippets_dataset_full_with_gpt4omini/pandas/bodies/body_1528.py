# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH34687
from scipy.sparse import eye

df = DataFrame.sparse.from_spmatrix(eye(5))
result = df.loc[range(2)]
expected = DataFrame(
    [[1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0]],
    dtype=SparseDtype("float64", 0.0),
)
tm.assert_frame_equal(result, expected)

result = df.loc[range(2)].loc[range(1)]
expected = DataFrame(
    [[1.0, 0.0, 0.0, 0.0, 0.0]], dtype=SparseDtype("float64", 0.0)
)
tm.assert_frame_equal(result, expected)
