# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_type_spec_test.py
if not tf2.enabled():
    self.skipTest("DistributedIterator CompositeTensor support is only "
                  "present in TF 2.0 only.")

dataset = dataset_ops.DatasetV2.range(10).batch(2)

distribution.extended.experimental_enable_get_next_as_optional = (
    enable_get_next_as_optional)

dist_dataset = distribution.experimental_distribute_dataset(dataset)
with distribution.scope():
    iterator = iter(dist_dataset)
    _check_type_spec_structure(iterator)

spec = iterator._type_spec

tensor_list = spec._to_components(iterator)
re_iterator = spec._from_components(tensor_list)

self.assertEqual(iterator._input_workers, re_iterator._input_workers)
self.assertAllEqual(iterator._iterators, re_iterator._iterators)
