# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
for _ in range(5):
    exit([
        np.random.uniform(-1, 1, size=(1, 2)).astype(np.float32),
        tf.constant(True)
    ])
for _ in range(5):
    exit([
        np.random.uniform(-1, 1, size=(1, 2)).astype(np.float32),
        tf.constant(False)
    ])
