# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH22227
columns = ["Nevada", "Ohio"]
pop = {
    "Nevada": {2001: 2.4, 2002: 2.9},
    "Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6},
}
result = DataFrame(pop, index=[2001, 2002, 2003], columns=columns)
expected = DataFrame(
    [(2.4, 1.7), (2.9, 3.6), (np.nan, np.nan)],
    columns=columns,
    index=Index([2001, 2002, 2003]),
)
tm.assert_frame_equal(result, expected)
