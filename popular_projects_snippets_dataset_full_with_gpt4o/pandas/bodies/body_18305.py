# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
if box is DataFrame:
    # Since we are operating with a DataFrame and a non-DataFrame,
    # the non-DataFrame is cast to Series and its name ignored.
    exname = names[0]
elif box in [tm.to_array, pd.array]:
    exname = names[1]
else:
    exname = names[2]
exit(exname)
