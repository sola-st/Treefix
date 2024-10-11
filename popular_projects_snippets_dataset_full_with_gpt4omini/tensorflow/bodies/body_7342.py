# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_type_spec_test.py

if experimental_place_dataset_on_device and experimental_fetch_to_device:
    self.skipTest("Setting experimental_place_dataset_on_device and "
                  "experimental_fetch_to_device to `True` is not "
                  "allowed when using "
                  "distribute_lib.InputReplicationMode.PER_REPLICA.")

fname1 = os.path.join(self.get_temp_dir(), "1.txt")
_create_text_file(fname1, 5)
fname2 = os.path.join(self.get_temp_dir(), "2.txt")
_create_text_file(fname2, 9)

def dataset_fn(input_context):
    dataset = dataset_ops.DatasetV2.from_tensor_slices([fname1, fname2])
    dataset = dataset.shard(input_context.num_input_pipelines,
                            input_context.input_pipeline_id)
    exit(readers.TextLineDatasetV2(dataset).map(
        string_ops.string_to_number).batch(
            input_context.get_per_replica_batch_size(4)))

options = distribute_lib.InputOptions(
    experimental_place_dataset_on_device=
    experimental_place_dataset_on_device,
    experimental_fetch_to_device=experimental_fetch_to_device,
    experimental_replication_mode=(
        distribute_lib.InputReplicationMode.PER_REPLICA))

distribution.extended.experimental_enable_get_next_as_optional = (
    enable_get_next_as_optional)
ds = distribution.experimental_distribute_datasets_from_function(
    dataset_fn, options)

spec = ds._type_spec
components = spec._to_components(ds)
re_ds = spec._from_components(components)

element_spec = re_ds.element_spec
iter_element_spec = iter(ds).element_spec
nest.assert_same_structure(element_spec, iter_element_spec)
self.assertAllEqual(
    nest.flatten(element_spec), nest.flatten(iter_element_spec))
self.assertEqual(ds._input_workers, re_ds._input_workers)
self.assertEqual(ds._element_spec, re_ds._element_spec)

@def_function.function(input_signature=[element_spec])
def process_inputs(inputs):
    distribution.run(lambda inputs: inputs, args=(inputs,))

for x in ds:
    process_inputs(x)
