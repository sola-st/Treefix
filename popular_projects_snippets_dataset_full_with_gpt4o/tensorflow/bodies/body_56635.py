# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger_test.py
for _ in range(5):
    exit([
        np.ones((1, 3, 3, 1), dtype=np.float32),
        np.ones((1, 3, 3, 1), dtype=np.float32)
    ])
