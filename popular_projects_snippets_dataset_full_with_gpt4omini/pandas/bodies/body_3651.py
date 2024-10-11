# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename.py
sig = inspect.signature(DataFrame.rename)
parameters = set(sig.parameters)
assert parameters == {
    "self",
    "mapper",
    "index",
    "columns",
    "axis",
    "inplace",
    "copy",
    "level",
    "errors",
}
