# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
# GH21049 Verify whether non writable numpy array is shiftable
input_data.setflags(write=False)

result = frame_or_series(input_data).shift(1)
if frame_or_series is not Series:
    # need to explicitly specify columns in the empty case
    expected = frame_or_series(
        output_data,
        index=range(len(output_data)),
        columns=range(1),
        dtype="float64",
    )
else:
    expected = frame_or_series(output_data, dtype="float64")

tm.assert_equal(result, expected)
