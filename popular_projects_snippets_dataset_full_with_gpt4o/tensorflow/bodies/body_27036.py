# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/shuffle_and_repeat_test.py
# Check that the output orders of different epochs are indeed different.
output = self._gen_outputs(lambda: self._build_ds(10), 100)
for i in range(4):
    epoch1 = output[i * 20:(i + 1) * 20]
    epoch2 = output[(i + 1) * 20:(i + 2) * 20]
    self.assertNotEqual(epoch1, epoch2)
