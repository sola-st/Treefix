# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
x_np = 4
for use_gpu in [False, True]:
    with self.subTest(use_gpu=use_gpu):
        with self.cached_session(use_gpu=use_gpu):
            x_tf = self.evaluate(array_ops.reverse_v2(x_np, []))
            self.assertAllEqual(x_tf, x_np)
