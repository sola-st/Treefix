# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
A = np.arange(5).repeat(20)
B = np.tile(np.arange(5), 20)
random.shuffle(A)
random.shuffle(B)
frame = DataFrame({"A": A, "B": B, "C": np.random.randn(100)})

result = frame.sort_values(by=["A", "B"])
indexer = np.lexsort((frame["B"], frame["A"]))
expected = frame.take(indexer)
tm.assert_frame_equal(result, expected)

result = frame.sort_values(by=["A", "B"], ascending=False)
indexer = np.lexsort(
    (frame["B"].rank(ascending=False), frame["A"].rank(ascending=False))
)
expected = frame.take(indexer)
tm.assert_frame_equal(result, expected)

result = frame.sort_values(by=["B", "A"])
indexer = np.lexsort((frame["A"], frame["B"]))
expected = frame.take(indexer)
tm.assert_frame_equal(result, expected)
