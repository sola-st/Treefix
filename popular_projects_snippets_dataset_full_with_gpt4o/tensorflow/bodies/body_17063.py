# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with test_util.use_gpu():
    x_np = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.uint8).reshape([2, 3, 1])
    y_np = np.array([[3, 2, 1], [6, 5, 4]], dtype=np.uint8).reshape([2, 3, 1])
    if "RandomFlipUpDown" in self.id():
        y_np = np.array(
            [[4, 5, 6], [1, 2, 3]], dtype=np.uint8).reshape([2, 3, 1])

    x_tf = constant_op.constant(x_np, shape=x_np.shape)

    iterations = 2
    flip_counts = [None for _ in range(iterations)]
    flip_sequences = ["" for _ in range(iterations)]
    test_seed = (1, 2)
    split_seeds = stateless_random_ops.split(test_seed, 10)
    seeds_list = self.evaluate(split_seeds)
    for i in range(iterations):
        count_flipped = 0
        count_unflipped = 0
        flip_seq = ""
        for seed in seeds_list:
            y_tf = func(x_tf, seed=seed)
            y_tf_eval = self.evaluate(y_tf)
            if y_tf_eval[0][0] == 1:
                self.assertAllEqual(y_tf_eval, x_np)
                count_unflipped += 1
                flip_seq += "U"
            else:
                self.assertAllEqual(y_tf_eval, y_np)
                count_flipped += 1
                flip_seq += "F"

        flip_counts[i] = (count_flipped, count_unflipped)
        flip_sequences[i] = flip_seq

    # Verify that results are deterministic.
    for i in range(1, iterations):
        self.assertAllEqual(flip_counts[0], flip_counts[i])
        self.assertAllEqual(flip_sequences[0], flip_sequences[i])
