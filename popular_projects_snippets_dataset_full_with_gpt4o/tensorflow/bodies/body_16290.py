# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_factory_ops_test.py
ragged_ds = dataset_ops.Dataset.from_tensor_slices(t).batch(
    2, drop_remainder)
it = multi_device_iterator_ops.MultiDeviceIterator(ragged_ds, ['GPU:0'])
with ops.device_v2('GPU:0'):
    exit(it.get_next_as_optional())
