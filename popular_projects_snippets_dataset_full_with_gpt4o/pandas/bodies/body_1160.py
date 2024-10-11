# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_multiindex.py
# GH#42145
complex_data = [1 + 2j, 4 - 3j, 10 - 1j]
non_complex_data = [3, 4, 5]
result = DataFrame(
    {
        "x": complex_data,
        "y": non_complex_data,
        "z": non_complex_data,
    }
)
result.set_index(["x", "y"], inplace=True)
expected = DataFrame(
    {"z": non_complex_data},
    index=MultiIndex.from_arrays(
        [complex_data, non_complex_data],
        names=("x", "y"),
    ),
)
tm.assert_frame_equal(result, expected)
