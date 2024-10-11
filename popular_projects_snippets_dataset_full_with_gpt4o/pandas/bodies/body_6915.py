# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_formats.py
with cf.option_context("display.max_seq_items", 10):
    result = repr(Index(np.arange(1000)))
    assert len(result) < 200
    assert "..." in result
