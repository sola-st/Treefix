# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
inp = np.random.rand(4, 4).astype("f")

with test_util.device(use_gpu=True):
    result = self.evaluate(array_ops.split(inp, [4], 0))
    self.assertAllEqual(result[0], inp)

    result = self.evaluate(array_ops.split(inp, [-1, 3], 0))
    self.assertAllEqual(result[0], inp[0:1, :])
    self.assertAllEqual(result[1], inp[1:4, :])
