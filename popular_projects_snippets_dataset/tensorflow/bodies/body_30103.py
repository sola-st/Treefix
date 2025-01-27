# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
for reverse_f in [array_ops.reverse_v2, array_ops.reverse]:
    for outer_size in list(range(50)) + [100000]:
        for middle_size in (1, 2):
            with self.subTest(
                reverse_f=reverse_f,
                outer_size=outer_size,
                middle_size=middle_size,
                use_gpu=True):
                x_np = np.reshape(
                    np.arange(outer_size * middle_size * 3, dtype=np.float32),
                    newshape=(outer_size, middle_size, 3))
                x_tf = self.evaluate(reverse_f(x_np, [0]))
                np_answer = x_np[::-1, :, :]
                self.assertAllEqual(x_tf, np_answer)
