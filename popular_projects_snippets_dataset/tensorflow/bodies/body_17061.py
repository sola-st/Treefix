# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Test random flip with single seed (stateful).
with ops.Graph().as_default():
    x_np = np.array([[1, 2, 3], [1, 2, 3]], dtype=np.uint8).reshape([2, 3, 1])
    y_np = np.array([[3, 2, 1], [3, 2, 1]], dtype=np.uint8).reshape([2, 3, 1])
    seed = 42

    with self.cached_session():
        x_tf = constant_op.constant(x_np, shape=x_np.shape)
        y = image_ops.random_flip_left_right(x_tf, seed=seed)
        self.assertTrue(y.op.name.startswith("random_flip_left_right"))

        count_flipped = 0
        count_unflipped = 0
        for _ in range(100):
            y_tf = self.evaluate(y)
            if y_tf[0][0] == 1:
                self.assertAllEqual(y_tf, x_np)
                count_unflipped += 1
            else:
                self.assertAllEqual(y_tf, y_np)
                count_flipped += 1

        # 100 trials
        # Mean: 50
        # Std Dev: ~5
        # Six Sigma: 50 - (5 * 6) = 20
        self.assertGreaterEqual(count_flipped, 20)
        self.assertGreaterEqual(count_unflipped, 20)
