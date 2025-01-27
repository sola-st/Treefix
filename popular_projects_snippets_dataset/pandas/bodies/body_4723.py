# Extracted from ./data/repos/pandas/pandas/tests/strings/test_extract.py
er = [np.nan, np.nan]  # empty row
mixed = Series(
    [
        "aBAD_BAD",
        np.nan,
        "BAD_b_BAD",
        True,
        datetime.today(),
        "foo",
        None,
        1,
        2.0,
    ]
)

result = mixed.str.extract(".*(BAD[_]+).*(BAD)", expand=True)
expected = DataFrame([["BAD_", "BAD"], er, ["BAD_", "BAD"], er, er, er, er, er, er])
tm.assert_frame_equal(result, expected)
