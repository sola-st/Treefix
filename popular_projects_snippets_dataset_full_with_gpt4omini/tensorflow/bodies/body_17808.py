# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
jacobians, per_eg_jacobians_pfor, per_eg_jacobians_while = (
    create_fc_per_eg_jacobians(batch_size=8,
                               activation_size=4,
                               num_layers=2))
self.run_and_assert_equal(jacobians, per_eg_jacobians_pfor,
                          rtol=2e-3, atol=1e-3)
self.run_and_assert_equal(jacobians, per_eg_jacobians_while,
                          rtol=2e-3, atol=1e-3)
