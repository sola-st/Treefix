# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH 7101

# doc example (indexing.rst)

# multi-index
arrays = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
]
tuples = list(zip(*arrays))
index = MultiIndex.from_tuples(tuples, names=["first", "second"])
s = Series(np.random.randn(8), index=index)

with option_context("display.max_rows", 10):
    assert len(str(s).split("\n")) == 10
with option_context("display.max_rows", 3):
    assert len(str(s).split("\n")) == 5
with option_context("display.max_rows", 2):
    assert len(str(s).split("\n")) == 5
with option_context("display.max_rows", 1):
    assert len(str(s).split("\n")) == 4
with option_context("display.max_rows", 0):
    assert len(str(s).split("\n")) == 10

# index
s = Series(np.random.randn(8), None)

with option_context("display.max_rows", 10):
    assert len(str(s).split("\n")) == 9
with option_context("display.max_rows", 3):
    assert len(str(s).split("\n")) == 4
with option_context("display.max_rows", 2):
    assert len(str(s).split("\n")) == 4
with option_context("display.max_rows", 1):
    assert len(str(s).split("\n")) == 3
with option_context("display.max_rows", 0):
    assert len(str(s).split("\n")) == 9
