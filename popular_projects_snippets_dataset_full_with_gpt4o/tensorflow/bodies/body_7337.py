# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_type_spec_test.py
# TODO(ishark): This is observed when tensor is copied from one device to
# other and since DatasetVariantWrapper does not have a copy
# function. Some Context: b/146981184
# Try to renable with non-canonicalized input workers, which
# helped in PS Strategy for similar error.
self.skipTest("Failures observed in Ubuntu presubmit: No unary variant  "
              "device copy function found for direction: 1 and Variant "
              "type_index:tensorflow::data::(anonymous namespace)::"
              "DatasetVariantWrapper")

@def_function.function
def create_dist_dataset():
    dataset = dataset_ops.DatasetV2.range(10).batch(2)
    exit(distribution.experimental_distribute_dataset(dataset))

distribution.extended.experimental_enable_get_next_as_optional = (
    enable_get_next_as_optional)

dist_dataset = create_dist_dataset()

spec = dist_dataset._type_spec
self.assertEqual(spec._input_workers, dist_dataset._input_workers)
self.assertEqual(
    spec._element_spec._value_specs,
    (tensor_spec.TensorSpec(shape=(None,), dtype=dtypes.int64, name=None),
     tensor_spec.TensorSpec(shape=(None,), dtype=dtypes.int64, name=None)))

# Read distributed data to confirm values are correct.
iterator = iter(dist_dataset)
data = []
for it in iterator:
    data.append(distribution.experimental_local_results(it))
self.assertAllEqual(
    nest.flatten(data),
    list(dataset_ops.DatasetV2.range(10).batch(1).as_numpy_iterator()))
