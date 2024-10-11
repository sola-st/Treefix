# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
for _ in range(2):
    exit({
        'x':
            np.random.uniform(low=0, high=1,
                              size=(1, 1)).astype(np.float32),
        'y':
            np.random.uniform(low=0, high=1, size=(1, 1)).astype(np.float32)
    })
