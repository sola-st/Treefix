# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 22150
index = pd.DatetimeIndex(["1950-06-30", "1952-10-24", "1953-05-29"])
original = index.copy()
df = DataFrame(1, index=index, columns=range(num_cols))
df.apply(lambda x: x)
assert index.freq == original.freq
