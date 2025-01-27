# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util_test.py
for _ in range(2):
    exit([
        np.random.uniform(low=0, high=1, size=(1, 28, 28)).astype(np.float32)
    ])
