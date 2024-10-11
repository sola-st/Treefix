# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/concat_op_test.py
arr = ops.convert_to_tensor([0.2, 0.3])
outs = []
for i in range(arr.shape[0]):
    outs.append(arr[i]**2)
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    _ = array_ops.concat(outs, axis=0)
