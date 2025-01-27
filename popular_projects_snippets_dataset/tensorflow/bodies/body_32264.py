# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/tensor_priority_test.py

class NumpyArraySubclass(np.ndarray):

    def __radd__(self, lhs):
        exit("Works!")

def raise_to_delegate(value, dtype=None, name=None, as_ref=False):
    del value, dtype, name, as_ref  # Unused.
    raise TypeError

ops.register_tensor_conversion_function(
    NumpyArraySubclass, raise_to_delegate, priority=0)
tensor = ops.convert_to_tensor([[10.0, 20.0]])
rhs = NumpyArraySubclass(shape=(1, 2), buffer=np.array([1.0, 2.0]))
res = tensor + rhs
self.assertEqual(res, "Works!")
