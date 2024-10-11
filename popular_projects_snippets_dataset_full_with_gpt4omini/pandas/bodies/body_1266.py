# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_chaining_and_caching.py
# GH 5424
cont = ["one", "two", "three", "four", "five", "six", "seven"]

df = DataFrame({"a": cont, "b": cont[3:] + cont[:3], "c": np.arange(7)})

# ref the cache
if do_ref:
    df.loc[0, "c"]

# set it
df.loc[7, "c"] = 1

assert df.loc[0, "c"] == 0.0
assert df.loc[7, "c"] == 1.0
