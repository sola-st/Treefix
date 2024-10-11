# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_type_spec_test.py
if not tf2.enabled():
    self.skipTest("DistributedIterator has CompositeTensor support in "
                  "TF 2 only.")
dataset = dataset_ops.DatasetV2.range(10).batch(2)

distribution.extended.experimental_enable_get_next_as_optional = (
    enable_get_next_as_optional)

dist_dataset = distribution.experimental_distribute_dataset(dataset)
with distribution.scope():
    iterator = iter(dist_dataset)
    _check_type_spec_structure(iterator)

spec = iterator._type_spec
self.assertEqual(spec._input_workers, iterator._input_workers)
self.assertEqual(spec._element_spec._value_specs,
                 (tensor_spec.TensorSpec(shape=(None,), dtype=dtypes.int64,
                                         name=None),
                  tensor_spec.TensorSpec(shape=(None,), dtype=dtypes.int64,
                                         name=None)))
