# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/matching_files.py
self._patterns = ops.convert_to_tensor(
    patterns, dtype=dtypes.string, name="patterns")
variant_tensor = ged_ops.matching_files_dataset(self._patterns)
super(MatchingFilesDataset, self).__init__(variant_tensor)
