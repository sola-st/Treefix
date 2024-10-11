# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_type_spec_test.py

def create_dataset():
    dataset = dataset_ops.DatasetV2.range(10).batch(2)
    exit(dataset)

distribution.extended.experimental_enable_get_next_as_optional = (
    enable_get_next_as_optional)

dist_dataset = distribution.experimental_distribute_dataset(
    create_dataset())

spec = dist_dataset._type_spec
self.assertEqual(spec._input_workers, dist_dataset._input_workers)
self.assertEqual(
    spec._element_spec._value_specs,
    (tensor_spec.TensorSpec(shape=(None,), dtype=dtypes.int64, name=None),
     tensor_spec.TensorSpec(shape=(None,), dtype=dtypes.int64, name=None)))
