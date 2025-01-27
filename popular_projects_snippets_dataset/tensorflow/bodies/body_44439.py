# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
self._fixed_while_loop(lambda s: _partial_shaped_bools())
# TODO(mdan): This error is quite bad. Measure the cost of an assertion.
self.assertRaisesRuntime(
    errors_impl.InvalidArgumentError, 'requested shape has 1')
