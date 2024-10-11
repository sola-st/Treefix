# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Calcualates the number of replicas that have values.

  Args:
    strategy: the `tf.distribute.Strategy`.
    input_workers: the `InputWorkers`.
    optional_list: a list of lists `tf.experimental.Optional`. The values from
      each compute device grouped by the input device.

  Returns:
    A scalar Tensor.
  """
worker_has_values = []
for worker, optionals in zip(input_workers.worker_devices, optional_list):
    with ops.device(worker):
        device_has_values = [
            math_ops.cast(v.has_value(), dtypes.int64) for v in optionals
        ]
        worker_has_values.append(
            math_ops.reduce_sum(device_has_values, keepdims=True))
client_has_values = math_ops.reduce_sum(worker_has_values, keepdims=True)
if strategy.extended._in_multi_worker_mode():  # pylint: disable=protected-access
    global_has_values = strategy.reduce(
        reduce_util.ReduceOp.SUM, client_has_values, axis=None)
    exit(array_ops.reshape(global_has_values, []))
else:
    exit(array_ops.reshape(client_has_values, []))
