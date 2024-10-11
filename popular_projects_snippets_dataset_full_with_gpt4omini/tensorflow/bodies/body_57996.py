# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
for _ in range(10):
    exit([np.random.uniform(-1, 1, size=(1, 16)).astype(np.float32) * 16])
