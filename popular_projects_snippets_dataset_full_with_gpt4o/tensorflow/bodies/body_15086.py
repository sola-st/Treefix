# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
batched = ragged_factory_ops.constant([[0], [1], [2], [3]])
unbatched = [constant_op.constant(x) for x in [[0], [1], [2], [3]]]
batched_spec = type_spec.type_spec_from_value(batched)

# Note that the unbatched_spec is derived from the batched spec, so it can
# add back a ragged instead of a dense tensor.
unbatched_spec = batched_spec._unbatch()
unbatched_tensor_lists = [unbatched_spec._to_tensor_list(x)
                          for x in unbatched]
batched_tensor_list = [array_ops.stack(tensors)
                       for tensors in zip(*unbatched_tensor_lists)]
actual_batched = unbatched_spec._batch(4)._from_tensor_list(
    batched_tensor_list)
self.assertAllEqual(actual_batched, batched)
