# Extracted from ./data/repos/pandas/pandas/tests/window/test_base_indexer.py
# GH: 35579
df = DataFrame({"b": [None, None, None, 7]})
indexer = FixedForwardWindowIndexer(window_size=2)
result = df.rolling(window=indexer, min_periods=0, step=step).count()
expected = DataFrame({"b": [0.0, 0.0, 1.0, 1.0]})[::step]
tm.assert_frame_equal(result, expected)
