# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
inp = self._makeData((4, 4), dtype)
with self.cached_session():
    inp_tensor = ops.convert_to_tensor(inp)
    s = array_ops.split(value=inp_tensor, num_or_size_splits=4, axis=1)
    inp_grads = [self._makeData((4, 1), dtype)for _ in range(4)]
    grad_tensors = [constant_op.constant(x) for x in inp_grads]
    grad = gradients_impl.gradients(s, [inp_tensor], grad_tensors)[0]
    result = self.evaluate(grad)
for i in range(4):
    self.assertAllEqual(result[:, i:i + 1], inp_grads[i])
