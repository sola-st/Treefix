# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 34529
df = DataFrame(np.array([b"abcd", b"efgh"]), columns=["col"])
expected = DataFrame(np.array([b"abcd", b"efgh"]), columns=["col"], dtype=object)
# After we make the apply we expect a dataframe just
# like the original but with the object datatype
result = df.apply(lambda x: x.astype("object"))
tm.assert_frame_equal(result, expected)
