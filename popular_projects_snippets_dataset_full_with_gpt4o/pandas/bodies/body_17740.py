# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_dst.py
# in the case of singular offsets, we don't necessarily know which utc
# offset the new Timestamp will wind up in (the tz for 1 month may be
# different from 1 second) so we don't specify an expected_utc_offset
for tz, utc_offsets in self.timezone_utc_offsets.items():
    hrs_pre = utc_offsets["utc_offset_standard"]
    self._test_all_offsets(
        n=1,
        tstart=self._make_timestamp(self.ts_pre_fallback, hrs_pre, tz),
        expected_utc_offset=None,
    )
