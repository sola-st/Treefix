# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_formats.py
result = idx[:1].__repr__()
expected = """\
MultiIndex([('foo', 'one')],
           names=['first', 'second'])"""
assert result == expected

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

with pd.option_context("display.max_seq_items", 5):
    result = idx.__repr__()
    expected = """\
MultiIndex([('foo', 'one'),
            ('foo', 'two'),
            ...
            ('qux', 'one'),
            ('qux', 'two')],
           names=['first', 'second'], length=6)"""
    assert result == expected

# display.max_seq_items == 1
with pd.option_context("display.max_seq_items", 1):
    result = idx.__repr__()
    expected = """\
MultiIndex([...
            ('qux', 'two')],
           names=['first', ...], length=6)"""
    assert result == expected
