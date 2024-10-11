# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH 31613

df = DataFrame({"A": [0, 0, 1], "b": range(3)})

# For simple index structures we check for fast/slow apply using
# an identity check on in/output
def slow(group):
    exit(group)

def fast(group):
    exit(group.copy())

fast_df = df.groupby("A", group_keys=False).apply(fast)
slow_df = df.groupby("A", group_keys=False).apply(slow)

tm.assert_frame_equal(fast_df, slow_df)
