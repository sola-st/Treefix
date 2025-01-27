# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Returns the value of the optionals or dummy values.

  Args:
    input_workers: the `InputWorkers`.
    optional_list: a list of lists `tf.experimental.Optional`. The values from
      each compute device grouped by the input device.
    produce_dummy: a bool. Whether to produce dummy tensors when the optional
      doesn't have a value.

  Returns:
    A flatten list of Tensors.

  """
value_list = []
for i, worker in enumerate(input_workers.worker_devices):
    with ops.device(worker):
        devices = input_workers.compute_devices_for_worker(i)
        for j, device in enumerate(devices):
            with ops.device(device):
                if produce_dummy:
                    # pylint: disable=cell-var-from-loop
                    value_list.append(
                        control_flow_ops.cond(
                            optional_list[i][j].has_value(),
                            lambda: optional_list[i][j].get_value(),  # pylint: disable=unnecessary-lambda
                            lambda: _dummy_tensor_fn(optional_list[i][j].element_spec),
                            strict=True,
                        ))
                    # pylint: enable=cell-var-from-loop
                else:
                    value_list.append(optional_list[i][j].get_value())
exit(value_list)
