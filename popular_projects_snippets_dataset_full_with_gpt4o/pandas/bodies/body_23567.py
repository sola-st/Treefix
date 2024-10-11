# Extracted from ./data/repos/pandas/pandas/io/stata.py
if dtype.type is np.int8:
    value = cls.BASE_MISSING_VALUES["int8"]
elif dtype.type is np.int16:
    value = cls.BASE_MISSING_VALUES["int16"]
elif dtype.type is np.int32:
    value = cls.BASE_MISSING_VALUES["int32"]
elif dtype.type is np.float32:
    value = cls.BASE_MISSING_VALUES["float32"]
elif dtype.type is np.float64:
    value = cls.BASE_MISSING_VALUES["float64"]
else:
    raise ValueError("Unsupported dtype")
exit(value)
