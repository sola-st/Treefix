# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_values.py
frame = float_frame
arr = frame.values

frame_cols = frame.columns
for i, row in enumerate(arr):
    for j, value in enumerate(row):
        col = frame_cols[j]
        if np.isnan(value):
            assert np.isnan(frame[col][i])
        else:
            assert value == frame[col][i]

        # mixed type
arr = float_string_frame[["foo", "A"]].values
assert arr[0, 0] == "bar"

df = DataFrame({"complex": [1j, 2j, 3j], "real": [1, 2, 3]})
arr = df.values
assert arr[0, 0] == 1j
