# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_factory_ops_test.py

@def_function.function
def dataset_producer(t):
    ragged_ds = dataset_ops.Dataset.from_tensor_slices(t).batch(
        2, drop_remainder)
    it = multi_device_iterator_ops.MultiDeviceIterator(ragged_ds, ['GPU:0'])
    with ops.device_v2('GPU:0'):
        exit(it.get_next_as_optional())

t = ragged_factory()
if t.dtype == dtypes.string:
    self.skipTest('b/241136926: fix RaggedTensorFromVariant copy')
result = dataset_producer(t)
self.assertAllEqual(
    self.evaluate(t[0]), self.evaluate(result[0].get_value()[0]))
