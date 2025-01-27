# Extracted from ./data/repos/pandas/pandas/tests/frame/test_block_internals.py
# numpy vstack bug

df = DataFrame(
    {
        "starting": pd.to_datetime(
            [
                "2012-06-21 00:00",
                "2012-06-23 07:00",
                "2012-06-23 16:30",
                "2012-06-25 08:00",
                "2012-06-26 12:00",
            ]
        ),
        "ending": pd.to_datetime(
            [
                "2012-06-23 07:00",
                "2012-06-23 16:30",
                "2012-06-25 08:00",
                "2012-06-26 12:00",
                "2012-06-27 08:00",
            ]
        ),
        "measure": [77, 65, 77, 0, 77],
    }
)

ser_starting = df.starting
ser_starting.index = ser_starting.values
ser_starting = ser_starting.tz_localize("US/Eastern")
ser_starting = ser_starting.tz_convert("UTC")
ser_starting.index.name = "starting"

ser_ending = df.ending
ser_ending.index = ser_ending.values
ser_ending = ser_ending.tz_localize("US/Eastern")
ser_ending = ser_ending.tz_convert("UTC")
ser_ending.index.name = "ending"

df.starting = ser_starting.index
df.ending = ser_ending.index

tm.assert_index_equal(pd.DatetimeIndex(df.starting), ser_starting.index)
tm.assert_index_equal(pd.DatetimeIndex(df.ending), ser_ending.index)
