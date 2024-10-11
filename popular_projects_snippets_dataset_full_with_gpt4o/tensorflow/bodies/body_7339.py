# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_type_spec_test.py
dataset = dataset_ops.DatasetV2.range(10).batch(2)
distribution.extended.experimental_enable_get_next_as_optional = (
    enable_get_next_as_optional)

options = distribute_lib.InputOptions(
    experimental_place_dataset_on_device=
    experimental_place_dataset_on_device,
    experimental_fetch_to_device=experimental_fetch_to_device)

dist_dataset = distribution.experimental_distribute_dataset(
    dataset, options)

spec = dist_dataset._type_spec
self.assertEqual(spec._input_workers, dist_dataset._input_workers)
self.assertEqual(
    spec._element_spec._value_specs,
    (tensor_spec.TensorSpec(shape=(None,), dtype=dtypes.int64, name=None),
     tensor_spec.TensorSpec(shape=(None,), dtype=dtypes.int64, name=None)))
components = spec._to_components(dist_dataset)
re_dist_dataset = spec._from_components(components)

self.assertEqual(dist_dataset._input_workers,
                 re_dist_dataset._input_workers)
self.assertAllEqual(dist_dataset._cloned_datasets,
                    re_dist_dataset._cloned_datasets)
self.assertEqual(dist_dataset._element_spec, re_dist_dataset._element_spec)
self.assertEqual(dist_dataset._enable_get_next_as_optional,
                 re_dist_dataset._enable_get_next_as_optional)
self.assertEqual(dist_dataset._options, re_dist_dataset._options)
