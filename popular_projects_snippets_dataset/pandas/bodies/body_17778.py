# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_inference.py
arr = np.arange(10).astype(np.int64).view("M8[s]")
dta = DatetimeArray._simple_new(arr, dtype=arr.dtype)
res = frequencies.infer_freq(dta)
assert res == "S"

arr2 = arr.view("m8[ms]")
tda = TimedeltaArray._simple_new(arr2, dtype=arr2.dtype)
res2 = frequencies.infer_freq(tda)
assert res2 == "L"
