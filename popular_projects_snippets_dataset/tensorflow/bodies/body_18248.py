# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
exit([array_ops.reshape(
            value.mass,
            self._pad_shape_to_full_rank(value.mass.shape)),
        array_ops.reshape(
            value.velocity,
            self._pad_shape_to_full_rank(value.velocity.shape))])
