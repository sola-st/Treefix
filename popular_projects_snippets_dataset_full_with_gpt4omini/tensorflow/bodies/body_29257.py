# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/structure_test.py
batched_value = value_fn()
s = structure.type_spec_from_value(batched_value)
batched_tensor_list = structure.to_batched_tensor_list(s, batched_value)

# The batch dimension is 2 for all of the test cases.
# NOTE(mrry): `tf.shape()` does not currently work for the DT_VARIANT
# tensors in which we store sparse tensors.
for t in batched_tensor_list:
    if t.dtype != dtypes.variant:
        self.assertEqual(2, self.evaluate(array_ops.shape(t)[0]))

    # Test that the 0th element from the unbatched tensor is equal to the
    # expected value.
expected_element_0 = self.evaluate(element_0_fn())
unbatched_s = nest.map_structure(
    lambda component_spec: component_spec._unbatch(), s)
actual_element_0 = structure.from_tensor_list(
    unbatched_s, [t[0] for t in batched_tensor_list])

for expected, actual in zip(
    nest.flatten(expected_element_0), nest.flatten(actual_element_0)):
    self.assertValuesEqual(expected, actual)
