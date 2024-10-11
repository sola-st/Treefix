# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/sparse_batch_test.py
components = np.random.randint(5, size=(40,)).astype(np.int32)

num_outputs = len(components) // 4
verify_fn(self, lambda: self._build_dataset(components), num_outputs)
