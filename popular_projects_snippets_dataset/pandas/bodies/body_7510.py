# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_formats.py
# display.max_seq_items == n
with pd.option_context("display.max_seq_items", 6):
    result = idx.__repr__()
    expected = """\
MultiIndex([('foo', 'one'),
            ('foo', 'two'),
            ('bar', 'one'),
            ('baz', 'two'),
            ('qux', 'one'),
            ('qux', 'two')],
           names=['first', 'second'])"""
    assert result == expected
