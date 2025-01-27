# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# We only check tz-naive for DTA bc the bounds are slightly different
#  for other tzs
i8vals = np.asarray([NaT.value + n for n in range(1, 5)], dtype="i8")
arr = self.array_cls(i8vals, freq="ns")
arr[0]  # should not raise OutOfBoundsDatetime

index = pd.Index(arr)
index[0]  # should not raise OutOfBoundsDatetime

ser = pd.Series(arr)
ser[0]  # should not raise OutOfBoundsDatetime
