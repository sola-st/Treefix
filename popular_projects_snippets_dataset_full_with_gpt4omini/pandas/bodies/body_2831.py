# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
df = DataFrame(np.random.randn(3, 3))

result = df.reindex(index=range(4), columns=range(4))
expected = df.reindex(list(range(4))).reindex(columns=range(4))

tm.assert_frame_equal(result, expected)

df = DataFrame(np.random.randint(0, 10, (3, 3)))

result = df.reindex(index=range(4), columns=range(4))
expected = df.reindex(list(range(4))).reindex(columns=range(4))

tm.assert_frame_equal(result, expected)

df = DataFrame(np.random.randint(0, 10, (3, 3)))

result = df.reindex(index=range(2), columns=range(2))
expected = df.reindex(range(2)).reindex(columns=range(2))

tm.assert_frame_equal(result, expected)

df = DataFrame(np.random.randn(5, 3) + 1j, columns=["a", "b", "c"])

result = df.reindex(index=[0, 1], columns=["a", "b"])
expected = df.reindex([0, 1]).reindex(columns=["a", "b"])

tm.assert_frame_equal(result, expected)
