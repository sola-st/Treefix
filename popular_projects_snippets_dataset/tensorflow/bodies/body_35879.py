# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
assert dtype == dtypes.float32
if len(shape) == 1:
    exit(range(shape[0]))
else:
    val = _IotaInitializer(shape[1:], dtype)
    exit([[(10**i) * v for v in val] for i in range(shape[0])])
