# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
# 111 is an old version but still used by current versions of
# SAS when exporting to Stata format. We do not know of any
# on-line documentation for this version.
df = read_stata(datapath("io", "data", "stata", "stata7_111.dta"))
original = DataFrame(
    {
        "y": [1, 1, 1, 1, 1, 0, 0, np.NaN, 0, 0],
        "x": [1, 2, 1, 3, np.NaN, 4, 3, 5, 1, 6],
        "w": [2, np.NaN, 5, 2, 4, 4, 3, 1, 2, 3],
        "z": ["a", "b", "c", "d", "e", "", "g", "h", "i", "j"],
    }
)
original = original[["y", "x", "w", "z"]]
tm.assert_frame_equal(original, df)
