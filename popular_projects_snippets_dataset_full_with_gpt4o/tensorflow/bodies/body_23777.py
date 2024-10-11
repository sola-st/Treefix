# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
for name, nan in [("PositiveNan", float_type(float("nan"))),
                  ("NegativeNan", float_type(float("-nan")))]:
    with self.subTest(name):
        nan_hash = hash(nan)
        nan_object_hash = object.__hash__(nan)
        # The hash of a NaN is either 0 or a hash of the object pointer.
        self.assertIn(nan_hash, (sys.hash_info.nan, nan_object_hash),
                      str(nan))
