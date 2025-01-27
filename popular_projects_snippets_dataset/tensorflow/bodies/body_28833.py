# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/list_files_test.py
filenames = ['b', 'c', 'a']
self._touchTempFiles(filenames)

dataset = dataset_ops.Dataset.list_files(
    path.join(self.tmp_dir, '*'), shuffle=False)
self.assertDatasetProduces(
    dataset,
    expected_output=[
        compat.as_bytes(path.join(self.tmp_dir, filename))
        for filename in sorted(filenames)
    ])
