# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
with ops.Graph().as_default():
    jacobians, per_eg_jacobians_pfor, per_eg_jacobians_while = (
        create_fc_per_eg_jacobians(batch_size=128,
                                   activation_size=32,
                                   num_layers=3))
    self._run(jacobians, 30, name="fc_jacobians_pfor")
    self._run(per_eg_jacobians_pfor, 100,
              name="fc_per_eg_jacobians_pfor")
    self._run(per_eg_jacobians_while, 10,
              name="fc_per_eg_jacobians_while")
