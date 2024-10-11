# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
"""Tests optimized code for reversing rows with last dim size = 3."""
for reverse_f in [array_ops.reverse_v2, array_ops.reverse]:
    for outer_size in (1, 2):
        for middle_size in list(range(50)) + [100000]:
            with self.subTest(
                reverse_f=reverse_f,
                outer_size=outer_size,
                middle_size=middle_size,
                use_gpu=True):
                x_np = np.reshape(
                    np.arange(outer_size * middle_size * 3, dtype=np.float32),
                    newshape=(outer_size, middle_size, 3))
                x_tf = self.evaluate(reverse_f(x_np, [1]))
                np_answer = x_np[:, ::-1, :]
                self.assertAllEqual(x_tf, np_answer)
