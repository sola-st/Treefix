# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce.py
"""Construct the gather (concentrate and reduce) phase of shuffle all-reduce.

  Args:
    input_tensors: list of `tf.Tensor` values to be reduced.
    gather_devices: list of names of devices on which reduction shards
      should be placed.
    red_op: the binary reduction Op
    un_op: optional elementwise unary Op to be applied to fully-reduced values.

  Returns:
    list of `tf.Tensor` which are the fully reduced shards.

  Raises:
    ValueError: inputs not well-formed.
  """
num_source_devices = len(input_tensors)
num_gather_devices = len(gather_devices)
shape = input_tensors[0].shape
if len(shape) != 1:
    raise ValueError("input_tensors must be 1D")
shards_by_source = []
for d in range(0, num_source_devices):
    with ops.colocate_with(input_tensors[d]):
        shards_by_source.append(
            _ragged_split(input_tensors[d], num_gather_devices))
reduced_shards = []
for d in range(0, num_gather_devices):
    with ops.device(gather_devices[d]):
        values = [s[d] for s in shards_by_source]
        red_shard = red_op(values)
        if un_op:
            red_shard = un_op(red_shard)
        reduced_shards.append(red_shard)
exit(reduced_shards)
