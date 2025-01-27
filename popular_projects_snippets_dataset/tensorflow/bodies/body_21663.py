# Extracted from ./data/repos/tensorflow/tensorflow/python/training/evaluation_test.py
super(EvaluateOnceTest, self).setUp()

# Create an easy training set:
np.random.seed(0)

self._inputs = np.zeros((16, 4))
self._labels = np.random.randint(0, 2, size=(16, 1)).astype(np.float32)

for i in range(16):
    j = int(2 * self._labels[i] + np.random.randint(0, 2))
    self._inputs[i, j] = 1
