# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py

first = ["foo", "bar", "buz"]
second = ["a", "b", "c"]
names = ["first", "second"]
result = MultiIndex.from_product([first, second], names=names)

tuples = [
    ("foo", "a"),
    ("foo", "b"),
    ("foo", "c"),
    ("bar", "a"),
    ("bar", "b"),
    ("bar", "c"),
    ("buz", "a"),
    ("buz", "b"),
    ("buz", "c"),
]
expected = MultiIndex.from_tuples(tuples, names=names)

tm.assert_index_equal(result, expected)
