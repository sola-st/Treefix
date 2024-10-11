# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/io_test.py
"""This test reproduces github.com/tensorflow/tensorflow/issues/49165."""
dataset1 = dataset_ops.Dataset.from_tensor_slices(np.random.rand(16, 32))
dataset1.save(self._test_dir)
dataset = dataset_ops.Dataset.load(self._test_dir)
dataset = dataset.shuffle(buffer_size=16)
dataset = dataset.batch(16)
dataset = dataset.repeat()
dataset = dataset.prefetch(1)
next_element = self.getNext(dataset)
for _ in range(30):
    self.evaluate(next_element())
