# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
idx = list(range(3))
cols = ["A", "B", "C"]
df1 = DataFrame(
    index=idx,
    columns=cols,
    data=np.array(
        [[0.0, 0.5, 1.0], [1.5, 2.0, 2.5], [3.0, 3.5, 4.0]], dtype=float
    ),
)
df2 = DataFrame(index=idx, columns=cols, data=np.ones((len(idx), len(cols))))

expected = DataFrame(
    index=idx,
    columns=cols,
    data=np.array([[0.0, 0.5, 1.0], [1.5, 2.0, -1], [-1, -1, -1]], dtype=float),
)

df1[df1 > 2.0 * df2] = -1
tm.assert_frame_equal(df1, expected)
with pytest.raises(ValueError, match="Item wrong length"):
    df1[df1.index[:-1] > 2] = -1
