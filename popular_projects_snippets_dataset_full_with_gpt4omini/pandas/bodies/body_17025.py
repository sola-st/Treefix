# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
df = DataFrame(np.random.randn(10, 4))

pieces = [df[:5], None, None, df[5:]]
result = concat(pieces)
tm.assert_frame_equal(result, df)
with pytest.raises(ValueError, match="All objects passed were None"):
    concat([None, None])
