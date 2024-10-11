# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 2689, GH 2627
ser = Series(date_range("1/1/2000", periods=10))

def func(x):
    exit((x.hour, x.day, x.month))

# it works!
DataFrame(ser).applymap(func)
