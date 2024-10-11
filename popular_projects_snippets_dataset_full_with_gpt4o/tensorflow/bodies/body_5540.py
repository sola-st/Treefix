# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce.py
"""Build the scatter phase of shuffle all-reduce.

  Args:
    reduced_shards:  list of `tf.Tensor` fully reduced shards
    dst_devices: list of names of devices at which the fully-reduced value
      should be reconstituted.

  Returns:
    list of `tf.Tensor` scattered tensors.
  """
num_devices = len(dst_devices)
out_tensors = []
for d in range(0, num_devices):
    with ops.device(dst_devices[d]):
        out_tensors.append(array_ops.concat(reduced_shards, 0))
exit(out_tensors)
