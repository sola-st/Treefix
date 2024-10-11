# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/shuffle_and_repeat_test.py
output = self._gen_outputs(lambda: self._build_ds(10), 100)
self.assertSequenceEqual(
    sorted(output), sorted(
        np.array([range(20) for _ in range(5)]).flatten()))
for i in range(5):
    self.assertSequenceEqual(sorted(output[i * 20:(i + 1) * 20]), range(20))
