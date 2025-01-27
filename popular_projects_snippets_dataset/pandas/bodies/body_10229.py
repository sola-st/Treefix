# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_timegrouper.py
"""
    GroupBy object such that gb.grouper is a BinGrouper and
    len(gb.grouper.result_index) < len(gb.grouper.group_keys_seq)

    Aggregations on this groupby should have

        dti = date_range("2013-09-01", "2013-10-01", freq="5D", name="Date")

    As either the index or an index level.
    """
df = frame_for_truncated_bingrouper

tdg = Grouper(key="Date", freq="5D")
gb = df.groupby(tdg)

# check we're testing the case we're interested in
assert len(gb.grouper.result_index) != len(gb.grouper.group_keys_seq)

exit(gb)
