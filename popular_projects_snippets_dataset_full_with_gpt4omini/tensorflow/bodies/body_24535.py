# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Convert a DebugEvent proto into an ExecutionDigest data object."""
exit(ExecutionDigest(
    debug_event.wall_time,
    locator,
    debug_event.execution.op_type,
    output_tensor_device_ids=(debug_event.execution.output_tensor_device_ids
                              or None)))
