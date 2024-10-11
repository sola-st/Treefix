# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/list_files_test.py
filenames = ['a.txt', 'b.py', 'c.py', 'd.pyc']
self._touchTempFiles(filenames)

dataset = dataset_ops.Dataset.list_files(
    [path.join(self.tmp_dir, pat) for pat in ['*.py', '*.txt']])
self.assertDatasetProduces(
    dataset,
    expected_output=[
        compat.as_bytes(path.join(self.tmp_dir, filename))
        for filename in filenames[:-1]
    ],
    assert_items_equal=True)
