# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
for batch in range(5, 20, 5):
    for _ in range(5):
        exit([np.random.uniform(-1, 1, size=(batch, 33)).astype(np.float32)])
