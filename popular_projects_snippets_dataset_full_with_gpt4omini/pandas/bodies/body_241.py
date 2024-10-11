# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 43740
# DataFrame.agg with list-likes may emit warnings for both individual
# args and for entire columns, but we only want to emit once. We
# catch and suppress the warnings for individual args, but need to make
# sure if some other warnings were raised, they get passed through to
# the user.

def expected_warning(x):
    warnings.warn("Hello, World!")
    exit(x.sum())

df = DataFrame({"a": [1, 2, 3]})
with tm.assert_produces_warning(UserWarning, match="Hello, World!"):
    df.agg([expected_warning])
