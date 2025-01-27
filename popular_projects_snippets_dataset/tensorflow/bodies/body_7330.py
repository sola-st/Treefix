# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_type_spec_test.py
if not tf2.enabled():
    self.skipTest("DistributedIterator has CompositeTensor support in "
                  "TF 2 only.")
distribution.extended.experimental_enable_get_next_as_optional = (
    enable_get_next_as_optional)

ds1 = dataset_ops.DatasetV2.range(10).batch(2).batch(5)
ds2 = dataset_ops.DatasetV2.from_tensors(
    array_ops.zeros([5, 2], dtypes.int64))
dist_ds1 = distribution.experimental_distribute_dataset(ds1)
dist_ds2 = distribution.experimental_distribute_dataset(ds2)

with distribution.scope():
    iter1 = iter(dist_ds1)
    iter2 = iter(dist_ds2)

spec1 = iter1._type_spec  # Wrapped TensorSpec has shape [None, None]
spec2 = iter2._type_spec  # Wrapped TensorSpec has shape [None, 2]

self.assertNotEqual(spec1, spec2)
self.assertEqual(spec1, spec1.most_specific_compatible_type(spec2))
self.assertEqual(spec1, spec2.most_specific_compatible_type(spec1))
