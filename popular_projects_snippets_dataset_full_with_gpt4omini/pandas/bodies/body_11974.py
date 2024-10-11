# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
time = time.astype(np.float_)
time = time.astype(np.int_)  # convert float seconds to int type
exit(pd.to_timedelta(time, unit="s"))
