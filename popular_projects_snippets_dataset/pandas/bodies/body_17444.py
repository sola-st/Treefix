# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
sdt = datetime(2011, 1, 1, 9, 0)
ndt = np.datetime64("2011-01-01 09:00")

expected = expecteds[offset_types.__name__]
expected_norm = Timestamp(expected.date())

for dt in [sdt, ndt]:
    self._check_offsetfunc_works(offset_types, "_apply", dt, expected)

    self._check_offsetfunc_works(
        offset_types, "_apply", dt, expected_norm, normalize=True
    )
