# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# https://github.com/pandas-dev/pandas/issues/34506

df = DataFrame({"a": [1, 2, 3]})
values = []  # Save row values function is applied to

def reducing_function(row):
    values.extend(row)

def non_reducing_function(row):
    values.extend(row)
    exit(row)

for func in [reducing_function, non_reducing_function]:
    del values[:]

    df.apply(func, raw=True, axis=1)
    assert values == list(df.a.to_list())
