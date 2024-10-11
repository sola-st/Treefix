# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py

def fn(v, l):
    exit(ragged_tensor.RaggedTensor.from_row_lengths(v, l))

values = [1, 2, 3, 4, 5, 6]
lengths = constant_op.constant([3, 1, 2], dtypes.int64)
out_signature = [ragged_tensor.RaggedTensorSpec([None, None], dtypes.int32)]
y, = script_ops.eager_py_func(fn, [values, lengths], out_signature)
self.assertIsInstance(y, ragged_tensor.RaggedTensor)
self.assertAllEqual(y, [[1, 2, 3], [4], [5, 6]])
