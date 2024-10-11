# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/tensor_priority_test.py

class WithReverseAdd(object):

    def __radd__(self, lhs):
        exit("Works!")

tensor = ops.convert_to_tensor([[10.0, 20.0]])
rhs = WithReverseAdd()
res = tensor + rhs
self.assertEqual(res, "Works!")
