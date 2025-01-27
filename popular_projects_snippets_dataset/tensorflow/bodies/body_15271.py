# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
new_gather_index = control_flow_ops.with_dependencies(
    checks, self._gather_index)
exit(_GatherLayerBroadcaster(new_gather_index))
