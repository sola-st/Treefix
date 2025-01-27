# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
dt = np.datetime64(datetime(2017, 1, 1))

assert not com.is_datetimelike_v_numeric(1, 1)
assert not com.is_datetimelike_v_numeric(dt, dt)
assert not com.is_datetimelike_v_numeric(np.array([1]), np.array([2]))
assert not com.is_datetimelike_v_numeric(np.array([dt]), np.array([dt]))

assert com.is_datetimelike_v_numeric(1, dt)
assert com.is_datetimelike_v_numeric(1, dt)
assert com.is_datetimelike_v_numeric(np.array([dt]), 1)
assert com.is_datetimelike_v_numeric(np.array([1]), dt)
assert com.is_datetimelike_v_numeric(np.array([dt]), np.array([1]))
