# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
if context.executing_eagerly():
    captured_iterator = iter(dataset_ops.Dataset.range(10))
else:
    captured_iterator = dataset_ops.make_initializable_iterator(
        dataset_ops.Dataset.range(10))
ds = _build_ds(captured_iterator)
exit((captured_iterator, ds))
