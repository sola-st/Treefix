# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
for _ in range(5):
    exit([
        np.random.uniform(-1, 1, size=(3)).astype(np.float32),
        np.random.uniform(-1, 1, size=(3)).astype(np.float32)
    ])
