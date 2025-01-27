# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/shuffle_and_repeat_test.py
num_epochs = 1000 * 1000
# Each element being shuffled and repeated has shape (100,). This will OOM
# or timeout if we actually load everything into the buffer.
ds = dataset_ops.Dataset.range(500).batch(100).apply(
    shuffle_ops.shuffle_and_repeat(
        buffer_size=5 * num_epochs, count=num_epochs))
# Verify two epochs worth of output.
output = self._gen_outputs(lambda: ds, 2 * 5, verify_exhausted=False)
for i in range(2):
    sorted_epoch = sorted(
        output[i * 5:(i + 1) * 5], key=lambda batch: batch[0])
    self.assertAllEqual(sorted_epoch, np.arange(500).reshape([5, 100]))
