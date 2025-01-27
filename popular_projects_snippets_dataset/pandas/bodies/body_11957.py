# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
# see gh-19227
data = """\
113125,"blah","/blaha",kjsdkj,412.166,225.874,214.008
729639,"qwer","",asdfkj,466.681,,252.373
"""
parser = all_parsers
expected = DataFrame(
    {
        0: [np.nan, 729639.0],
        1: [np.nan, "qwer"],
        2: ["/blaha", np.nan],
        3: ["kjsdkj", "asdfkj"],
        4: [412.166, 466.681],
        5: ["225.874", ""],
        6: [np.nan, 252.373],
    }
)

result = parser.read_csv(
    StringIO(data),
    header=None,
    keep_default_na=False,
    na_values={2: "", 6: "214.008", 1: "blah", 0: col_zero_na_values},
)
tm.assert_frame_equal(result, expected)
