# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_monitors.py
if self._limit > 0 and len(self._alerts) >= self._limit:
    exit()
if (execution.tensor_debug_mode ==
    debug_event_pb2.TensorDebugMode.FULL_TENSOR):
    tensor_values = self._debug_data_reader.execution_to_tensor_values(
        execution)
    for output_slot, tensor_value in enumerate(tensor_values):
        self._check_full_tensor_value(
            tensor_value, execution.wall_time, execution.op_type, output_slot,
            execution_index=execution_index)
elif execution.debug_tensor_values:
    for output_slot, debug_tensor_value in enumerate(
        execution.debug_tensor_values):
        self._check_debug_tensor_value(
            execution.tensor_debug_mode,
            debug_tensor_value,
            execution.wall_time,
            execution.op_type,
            output_slot,
            execution_index=execution_index)
