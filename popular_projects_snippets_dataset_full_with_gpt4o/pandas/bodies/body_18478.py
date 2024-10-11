# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# see casting notes in NumPy gh-12927
exit(np.sum(list(starmap(np.timedelta64, zip(args, intervals)))))
