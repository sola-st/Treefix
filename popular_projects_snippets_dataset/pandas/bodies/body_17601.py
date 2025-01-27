# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py
hdays = [datetime(2013, 1, 1) for ele in range(4)]
pth = datapath("tseries", "offsets", "data", "cday-0.14.1.pickle")
cday0_14_1 = read_pickle(pth)
cday = CDay(holidays=hdays)
assert cday == cday0_14_1
