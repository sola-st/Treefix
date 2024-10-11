# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asfreq.py
offset_monthly = datetime_frame.asfreq(offsets.BMonthEnd())
rule_monthly = datetime_frame.asfreq("BM")

tm.assert_frame_equal(offset_monthly, rule_monthly)

filled = rule_monthly.asfreq("B", method="pad")  # noqa
# TODO: actually check that this worked.

# don't forget!
filled_dep = rule_monthly.asfreq("B", method="pad")  # noqa
