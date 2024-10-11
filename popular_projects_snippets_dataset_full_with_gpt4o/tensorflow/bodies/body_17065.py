# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
batch_size = 16
seed = 42

# create single item of test data
x_np_raw = np.array(
    [[1, 2, 3], [1, 2, 3]], dtype=np.uint8
).reshape([1, 2, 3, 1])
y_np_raw = np.array(
    [[3, 2, 1], [3, 2, 1]], dtype=np.uint8
).reshape([1, 2, 3, 1])

# create batched test data
x_np = np.vstack([x_np_raw for _ in range(batch_size)])
y_np = np.vstack([y_np_raw for _ in range(batch_size)])

with self.cached_session():
    x_tf = constant_op.constant(x_np, shape=x_np.shape)
    count_flipped = 0
    count_unflipped = 0
    for seed in range(100):
        y_tf = self.evaluate(image_ops.random_flip_left_right(x_tf, seed=seed))

        # check every element of the batch
        for i in range(batch_size):
            if y_tf[i][0][0] == 1:
                self.assertAllEqual(y_tf[i], x_np[i])
                count_unflipped += 1
            else:
                self.assertAllEqual(y_tf[i], y_np[i])
                count_flipped += 1

    self.assertEqual(count_flipped, 772)
    self.assertEqual(count_unflipped, 828)
