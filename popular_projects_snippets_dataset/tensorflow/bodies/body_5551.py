# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce.py
"""Construct a subgraph for Shuffle hybrid all-reduce.

  Args:
    input_tensors: list of `tf.Tensor` of same-shape and type values to
      be reduced.
    gather_devices: list of device names on which to host gather shards.
    red_op: binary elementwise reduction operator.
    upper_level_f: function for reducing one value per worker, across
      workers.

  Returns:
    list of `tf.Tensor` of reduced values.

  Raises:
    ValueError: inputs not well-formed.
  """
input_tensors, shape = _flatten_tensors(input_tensors)
# First stage, reduce across each worker using gather_devices.
devices = [t.device for t in input_tensors]
per_worker_devices, per_worker_values = _split_by_task(devices, input_tensors)
num_workers = len(per_worker_devices)
up_values = []
if len(gather_devices) != num_workers:
    raise ValueError("For shuffle hybrid, gather_devices must contain one "
                     "device per worker. ")
for w in range(0, num_workers):
    reduced_shards = _build_shuffle_gather(
        per_worker_values[w], [gather_devices[w]], red_op)
    up_values.append(reduced_shards[0])
# Second stage, apply upper_level_f.
level_2_output = upper_level_f(up_values)
# Third stage, apply shuffle scatter at each worker.
output_tensors = []
for w in range(0, num_workers):
    output_tensors += _build_shuffle_scatter(
        [level_2_output[w]], per_worker_devices[w])
if len(shape) != 1:
    output_tensors = _reshape_tensors(output_tensors, shape)
exit(output_tensors)
