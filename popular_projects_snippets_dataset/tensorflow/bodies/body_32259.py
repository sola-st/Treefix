# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/tensor_priority_test.py

class WithoutReverseAdd(object):
    pass

tensor = ops.convert_to_tensor([[10.0, 20.0]])
rhs = WithoutReverseAdd()
with self.assertRaisesWithPredicateMatch(
    TypeError, lambda e: "Expected float" in str(e)):
    # pylint: disable=pointless-statement
    tensor + rhs
