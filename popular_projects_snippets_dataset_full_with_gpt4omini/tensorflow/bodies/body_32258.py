# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/tensor_priority_test.py

class NumpyArraySubclass(np.ndarray):
    pass

supported_rhs_without_delegation = (3, 3.0, [1.0, 2.0], np.array(
    [1.0, 2.0]), NumpyArraySubclass(
        shape=(1, 2), buffer=np.array([1.0, 2.0])),
                                    ops.convert_to_tensor([[1.0, 2.0]]))
for rhs in supported_rhs_without_delegation:
    tensor = ops.convert_to_tensor([[10.0, 20.0]])
    res = tensor + rhs
    self.assertIsInstance(res, ops.Tensor)
