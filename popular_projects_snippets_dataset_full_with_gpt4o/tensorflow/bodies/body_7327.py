# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_type_spec_test.py
distribution.extended.experimental_enable_get_next_as_optional = (
    enable_get_next_as_optional)
ds = dataset_ops.DatasetV2.from_tensor_slices(
    np.ones([9, 12]).astype(np.float32)).batch(
        4, drop_remainder=drop_remainder)
ds = distribution.experimental_distribute_dataset(ds)
_check_type_spec_structure(iter(ds))
element_spec = ds.element_spec
iter_element_spec = iter(ds).element_spec
nest.assert_same_structure(element_spec, iter_element_spec)
self.assertAllEqual(
    nest.flatten(element_spec), nest.flatten(iter_element_spec))

@def_function.function(input_signature=[element_spec])
def process_inputs(inputs):
    distribution.run(lambda inputs: inputs, args=(inputs,))

for x in ds:
    process_inputs(x)
