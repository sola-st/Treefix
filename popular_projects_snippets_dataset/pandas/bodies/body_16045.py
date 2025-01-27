# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_align.py
b = datetime_series[:5].copy()

# do copy
a = datetime_series.copy()
ra, _ = a.align(b, join="left")
ra[:5] = 5
assert not (a[:5] == 5).any()

# do not copy
a = datetime_series.copy()
ra, _ = a.align(b, join="left", copy=False)
ra[:5] = 5
assert (a[:5] == 5).all()

# do copy
a = datetime_series.copy()
b = datetime_series[:5].copy()
_, rb = a.align(b, join="right")
rb[:3] = 5
assert not (b[:3] == 5).any()

# do not copy
a = datetime_series.copy()
b = datetime_series[:5].copy()
_, rb = a.align(b, join="right", copy=False)
rb[:2] = 5
assert (b[:2] == 5).all()
