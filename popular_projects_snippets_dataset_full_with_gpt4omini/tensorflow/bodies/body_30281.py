# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
inp = self._makeData((4, 4), dtype)
with test_util.device(use_gpu=True):
    inp_tensor = ops.convert_to_tensor(inp)
    s = array_ops.split(inp_tensor, [1, 3], 1)
    inp_grads = [
        self._makeData((4, 1), dtype), self._makeData((4, 3), dtype)
    ]
    grad_tensors = [constant_op.constant(x) for x in inp_grads]
    grad = gradients_impl.gradients(s, [inp_tensor], grad_tensors)[-1]
    result = self.evaluate(grad)

self.assertAllEqual(result[:, 0:1], inp_grads[0])
self.assertAllEqual(result[:, 1:4], inp_grads[1])
