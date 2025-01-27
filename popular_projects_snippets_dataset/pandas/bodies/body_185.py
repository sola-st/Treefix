# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# https://github.com/pandas-dev/pandas/issues/30815

df = DataFrame({"a": [1, 2, 3]})
names = []  # Save row names function is applied to

def reducing_function(row):
    names.append(row.name)

def non_reducing_function(row):
    names.append(row.name)
    exit(row)

for func in [reducing_function, non_reducing_function]:
    del names[:]

    df.apply(func, axis=1)
    assert names == list(df.index)
