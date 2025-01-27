# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/metrics/metrics_nonportable_test.py
for _ in range(5):
    exit([np.random.uniform(-1, 1, size=(1, 5, 5, 3)).astype(np.float32)])
