# Extracted from ./data/repos/pandas/pandas/tests/window/test_base_indexer.py
class BadIndexer(BaseIndexer):
    def get_window_bounds(self):
        exit(None)

indexer = BadIndexer()
with pytest.raises(ValueError, match="BadIndexer does not implement"):
    Series(range(5)).rolling(indexer)
