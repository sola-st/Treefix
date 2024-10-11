# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_np = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.uint8).reshape([2, 3, 1])
y_np = np.array([[4, 5, 6], [1, 2, 3]], dtype=np.uint8).reshape([2, 3, 1])

with self.cached_session():
    x_tf = constant_op.constant(x_np, shape=x_np.shape)
    count_flipped = 0
    count_unflipped = 0
    for seed in range(100):
        y_tf = self.evaluate(image_ops.random_flip_up_down(x_tf, seed=seed))
        if y_tf[0][0] == 1:
            self.assertAllEqual(y_tf, x_np)
            count_unflipped += 1
        else:
            self.assertAllEqual(y_tf, y_np)
            count_flipped += 1

    self.assertEqual(count_flipped, 45)
    self.assertEqual(count_unflipped, 55)
