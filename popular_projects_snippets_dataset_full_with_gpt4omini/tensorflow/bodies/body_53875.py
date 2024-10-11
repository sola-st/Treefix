# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
exit(self.assertRaisesWithPredicateMatch(
    exception_type, r"Incompatible shapes|Dimensions must be equal|"
    r"required broadcastable shapes"))
