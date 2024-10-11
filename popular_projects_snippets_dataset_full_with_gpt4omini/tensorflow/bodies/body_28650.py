# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
with test.mock.patch.object(warnings, "warn") as mock_log:
    dataset_ops.Dataset.range(0).interleave(
        lambda x: dataset_ops.Dataset.range(0), cycle_length=2)
    self.assertEmpty(mock_log.call_args_list)
