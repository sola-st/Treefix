# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/split_op_test.py
with test_util.device(use_gpu=True):
    tf_ans = array_ops.split(value=x, num_or_size_splits=num, axis=dim)
    out = self.evaluate(tf_ans)
self.assertEqual(x.size, 0)
self.assertEqual(len(out), num)
for i in range(num):
    self.assertEqual(out[i].shape, expected_shape)
    self.assertEqual(expected_shape, tf_ans[i].get_shape())
