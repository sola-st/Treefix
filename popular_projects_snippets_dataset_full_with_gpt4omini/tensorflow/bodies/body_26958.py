# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/csv_dataset_test.py
record_defaults = [constant_op.constant([[0]], dtype=dtypes.int64)] * 4
inputs = [[',,,', '1,1,1,', ',2,2,2']]

if context.executing_eagerly():
    err_spec = errors.InvalidArgumentError, (
        'Each record default should be at '
        'most rank 1')
else:
    err_spec = ValueError, 'Shape must be at most rank 1 but is rank 2'

with self.assertRaisesWithPredicateMatch(*err_spec):
    self._test_dataset(
        inputs, [[0, 0, 0, 0], [1, 1, 1, 0], [0, 2, 2, 2]],
        record_defaults=record_defaults)
