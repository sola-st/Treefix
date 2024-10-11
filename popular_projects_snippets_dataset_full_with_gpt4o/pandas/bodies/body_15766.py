# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_nlargest.py
dt = r.dtype
msg = f"Cannot use method 'n(largest|smallest)' with dtype {dt}"
args = 2, len(r), 0, -1
methods = r.nlargest, r.nsmallest
for method, arg in product(methods, args):
    with pytest.raises(TypeError, match=msg):
        method(arg)
