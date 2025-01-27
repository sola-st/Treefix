# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
# GH#21294

if levels == 1:
    frame, missing = float_frame, "food"
else:
    # MultiIndex columns
    frame = DataFrame(
        np.random.randn(8, 3),
        columns=Index(
            [("foo", "bar"), ("baz", "qux"), ("peek", "aboo")],
            name=("sth", "sth2"),
        ),
    )
    missing = ("good", "food")

keys = [frame.columns[1], frame.columns[0]]
idx = idx_type(keys)
idx_check = list(idx_type(keys))

if isinstance(idx, (set, dict)):
    with pytest.raises(TypeError, match="as an indexer is not supported"):
        frame[idx]

    exit()
else:
    result = frame[idx]

expected = frame.loc[:, idx_check]
expected.columns.names = frame.columns.names

tm.assert_frame_equal(result, expected)

idx = idx_type(keys + [missing])
with pytest.raises(KeyError, match="not in index"):
    frame[idx]
