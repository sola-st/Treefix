# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
df = DataFrame(np.random.randn(10, 4))

result = concat([df], keys=["foo"])
expected = concat([df, df], keys=["foo", "bar"])
tm.assert_frame_equal(result, expected[:10])
