# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#20684
"""
        parse_datetime_string_with_reso return parameter if type not matched.
        PeriodIndex.get_loc takes returned value from parse_datetime_string_with_reso
        as a tuple.
        If first argument is Period and a tuple has 3 items,
        process go on not raise exception
        """
df = DataFrame(
    {
        "A": [Period(2019), "x1", "x2"],
        "B": [Period(2018), Period(2016), "y1"],
        "C": [Period(2017), "z1", Period(2015)],
        "V1": [1, 2, 3],
        "V2": [10, 20, 30],
    }
).set_index(["A", "B", "C"])
with pytest.raises(KeyError, match=msg):
    df.loc[key]
