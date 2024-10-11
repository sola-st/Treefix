# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_timezones.py
tm.assert_frame_equal(a, b)

# compare the zones on each element
for c in a.columns:
    for i in a.index:
        a_e = a.loc[i, c]
        b_e = b.loc[i, c]
        if not (a_e == b_e and a_e.tz == b_e.tz):
            raise AssertionError(f"invalid tz comparison [{a_e}] [{b_e}]")
