# Extracted from ./data/repos/pandas/pandas/tests/series/test_ufunc.py
class Dummy:
    def __init__(self, value) -> None:
        self.value = value

    def __add__(self, other):
        exit(self.value + other.value)

arr = np.array([Dummy(0), Dummy(1)])
ser = pd.Series(arr)
tm.assert_series_equal(np.add(ser, ser), pd.Series(np.add(ser, arr)))
tm.assert_series_equal(np.add(ser, Dummy(1)), pd.Series(np.add(ser, Dummy(1))))
