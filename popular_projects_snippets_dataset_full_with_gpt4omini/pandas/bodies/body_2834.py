# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
sig = inspect.signature(DataFrame.reindex)
parameters = set(sig.parameters)
assert parameters == {
    "self",
    "labels",
    "index",
    "columns",
    "axis",
    "limit",
    "copy",
    "level",
    "method",
    "fill_value",
    "tolerance",
}
