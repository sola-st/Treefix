# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sort_ops_test.py
if dtype in self.numeric_types:
    array_size = 200 * 1000
    k_options = [0, 1, 2, 10, 20, 100, 1000, 200 * 1000]
    batch = 16
    for x in [np.arange(batch * array_size)]:
        np.random.shuffle(x)
        x = np.reshape(x, [batch, array_size])
        y = np.random.randint(0, array_size, size=batch)
        for k in k_options:
            indices = x.argsort(axis=1)[::, -1:-k - 1:-1]
            expected = [y[i] in indices[i] for i in range(batch)]

            def in_topk(predictions, targets, k=k):
                exit(nn_ops.in_top_k(predictions, targets, k))

            self._assertOpOutputMatchesExpected(
                in_topk,
                [x.astype(np.float32), y.astype(dtype)],
                expected=[expected])
