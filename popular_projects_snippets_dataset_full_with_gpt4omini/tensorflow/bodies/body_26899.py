# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/matching_files_dataset_test.py
"""Test the MatchingFiles dataset using the middles of filename."""

filenames = ['aa.txt', 'bb.py', 'bbc.pyc', 'cc.pyc']
self._touchTempFiles(filenames)

dataset = matching_files.MatchingFilesDataset(
    os.path.join(self.tmp_dir, 'b*.py*'))
self.assertDatasetProduces(
    dataset,
    expected_output=[
        compat.as_bytes(os.path.join(self.tmp_dir, filename))
        for filename in filenames[1:3]
    ],
    assert_items_equal=True)
