# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
# GH 1893

data = DataFrame(
    {"a": ["foo", "bar", "baz", "qux"], "b": [0, 0, 1, 1], "c": [1, 2, 3, 4]}
)

def _check_f(base, f):
    result = f(base)
    assert result is None

# -----DataFrame-----

# set_index
f = lambda x: x.set_index("a", inplace=True)
_check_f(data.copy(), f)

# reset_index
f = lambda x: x.reset_index(inplace=True)
_check_f(data.set_index("a"), f)

# drop_duplicates
f = lambda x: x.drop_duplicates(inplace=True)
_check_f(data.copy(), f)

# sort
f = lambda x: x.sort_values("b", inplace=True)
_check_f(data.copy(), f)

# sort_index
f = lambda x: x.sort_index(inplace=True)
_check_f(data.copy(), f)

# fillna
f = lambda x: x.fillna(0, inplace=True)
_check_f(data.copy(), f)

# replace
f = lambda x: x.replace(1, 0, inplace=True)
_check_f(data.copy(), f)

# rename
f = lambda x: x.rename({1: "foo"}, inplace=True)
_check_f(data.copy(), f)

# -----Series-----
d = data.copy()["c"]

# reset_index
f = lambda x: x.reset_index(inplace=True, drop=True)
_check_f(data.set_index("a")["c"], f)

# fillna
f = lambda x: x.fillna(0, inplace=True)
_check_f(d.copy(), f)

# replace
f = lambda x: x.replace(1, 0, inplace=True)
_check_f(d.copy(), f)

# rename
f = lambda x: x.rename({1: "foo"}, inplace=True)
_check_f(d.copy(), f)
