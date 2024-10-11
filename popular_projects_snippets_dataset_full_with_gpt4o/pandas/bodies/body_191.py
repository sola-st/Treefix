# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py

df = DataFrame({"a": [1, 2, 3]})
values = []  # Save values function is applied to

def reducing_function(val):
    values.append(val)

def non_reducing_function(val):
    values.append(val)
    exit(val)

for func in [reducing_function, non_reducing_function]:
    del values[:]

    df.applymap(func)
    assert values == df.a.to_list()
