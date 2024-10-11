# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
exit(ParticleSpec(
    mass=tensor_spec.TensorSpec(
        dtype=self.mass.dtype,
        shape=tensor_shape.TensorShape([batch_size]).concatenate(
            self._pad_shape_to_full_rank(self.mass.shape))),
    velocity=tensor_spec.TensorSpec(
        dtype=self.velocity.dtype,
        shape=tensor_shape.TensorShape([batch_size]).concatenate(
            self._pad_shape_to_full_rank(self.velocity.shape)))))
