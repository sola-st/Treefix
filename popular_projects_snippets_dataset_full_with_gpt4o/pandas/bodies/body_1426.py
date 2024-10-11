# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
obj = frame_or_series(np.arange(len(index)), index=index)
with pytest.raises(ValueError, match="slice step cannot be zero"):
    indexer_sl(obj)[::0]
