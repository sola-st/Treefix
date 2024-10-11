# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_misc.py
# GH#28055 ints_to_pydatetime with readonly array
arr = np.array([np.datetime64("2012-02-15T12:00:00.000000000")])
arr.setflags(write=False)
dti = pd.to_datetime(arr)
list(dti)
