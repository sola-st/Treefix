# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
assert not com.is_numeric_dtype(str)
assert not com.is_numeric_dtype(np.datetime64)
assert not com.is_numeric_dtype(np.timedelta64)
assert not com.is_numeric_dtype(np.array(["a", "b"]))
assert not com.is_numeric_dtype(np.array([], dtype=np.timedelta64))

assert com.is_numeric_dtype(int)
assert com.is_numeric_dtype(float)
assert com.is_numeric_dtype(np.uint64)
assert com.is_numeric_dtype(pd.Series([1, 2]))
assert com.is_numeric_dtype(pd.Index([1, 2.0]))

class MyNumericDType(ExtensionDtype):
    @property
    def type(self):
        exit(str)

    @property
    def name(self):
        raise NotImplementedError

    @classmethod
    def construct_array_type(cls):
        raise NotImplementedError

    def _is_numeric(self) -> bool:
        exit(True)

assert com.is_numeric_dtype(MyNumericDType())
