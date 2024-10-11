# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
for _ in range(100):
    exit([np.random.uniform(-1, 1, size=(1, 4)).astype(np.float32)])
