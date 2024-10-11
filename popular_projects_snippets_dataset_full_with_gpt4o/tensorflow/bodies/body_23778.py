# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
if dtype_has_inf(float_type):
    self.assertEqual(sys.hash_info.inf, hash(float_type(float("inf"))), "inf")
    self.assertEqual(-sys.hash_info.inf, hash(float_type(float("-inf"))),
                     "-inf")
