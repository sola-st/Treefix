# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
batched = ragged_factory_ops.constant([[0], [1], [2], [3]])
unbatched = [constant_op.constant(x) for x in [[0], [1], [2], [3]]]
batched_spec = type_spec.type_spec_from_value(batched)

# Note that the unbatched_spec is derived from the batched spec, so it can
# add back a ragged instead of a dense tensor.
unbatched_spec = batched_spec._unbatch()
batched_tensor_list = batched_spec._to_batched_tensor_list(batched)
unbatched_tensor_lists = zip(
    *[array_ops.unstack(tensor) for tensor in batched_tensor_list])
actual_unbatched = [
    batched_spec._unbatch()._from_tensor_list(tensor_list)
    for tensor_list in unbatched_tensor_lists]
self.assertLen(actual_unbatched, len(unbatched))
for x in actual_unbatched:
    self.assertTrue(unbatched_spec.is_compatible_with(x))

for (actual, expected) in zip(actual_unbatched, unbatched):
    self.assertAllEqual(actual, expected)
