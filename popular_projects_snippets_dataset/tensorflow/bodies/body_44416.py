# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
if not __debug__:
    self.skipTest('Feature disabled in optimized mode.')
with test.mock.patch.object(control_flow, 'PYTHON_MAX_ITERATIONS', 100):
    with self.assertRaisesRegex(ValueError, 'iteration limit'):
        control_flow.for_stmt(
            iter_=range(101),
            extra_test=None,
            body=lambda i: None,
            get_state=None,
            set_state=None,
            symbol_names=(),
            opts={})
