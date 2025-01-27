# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/matching_files_dataset_test.py
"""Test the MatchingFiles dataset using the suffixes of filename."""

filenames = ['a.txt', 'b.py', 'c.py', 'd.pyc']
self._touchTempFiles(filenames)

dataset = matching_files.MatchingFilesDataset(
    os.path.join(self.tmp_dir, '*.py'))
self.assertDatasetProduces(
    dataset,
    expected_output=[
        compat.as_bytes(os.path.join(self.tmp_dir, filename))
        for filename in filenames[1:-1]
    ],
    assert_items_equal=True)
