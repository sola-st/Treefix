# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/inplace_ops_test.py
with test_util.use_gpu():
    d0, d1, d2 = 100, 3, 5
    x = array_ops.zeros([d0, d1, d2])
    y = np.zeros([d0, d1, d2])
    for _ in range(20):
        idx = np.random.choice(d0, d0 // 10, replace=False)
        val = np.random.randint(10, size=(d0 // 10, d1, d2))
        op = np.random.randint(3)
        if op == 0:
            x = inplace_ops.inplace_update(x, idx, val)
            y[idx, :] = val
        elif op == 1:
            x = inplace_ops.inplace_add(x, idx, val)
            y[idx, :] += val
        elif op == 2:
            x = inplace_ops.inplace_sub(x, idx, val)
            y[idx, :] -= val
        self.assertAllClose(x, y)
