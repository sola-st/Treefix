# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_dst.py
# test moving from standard to daylight savings
for tz, utc_offsets in self.timezone_utc_offsets.items():
    hrs_pre = utc_offsets["utc_offset_standard"]
    hrs_post = utc_offsets["utc_offset_daylight"]
    self._test_all_offsets(
        n=3,
        tstart=self._make_timestamp(self.ts_pre_springfwd, hrs_pre, tz),
        expected_utc_offset=hrs_post,
    )
