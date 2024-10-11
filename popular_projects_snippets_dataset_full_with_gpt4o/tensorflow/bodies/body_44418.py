# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
if not __debug__:
    self.skipTest('Feature disabled in optimized mode.')
with test.mock.patch.object(
    control_flow, 'INEFFICIENT_UNROLL_MIN_ITERATIONS', 10):
    with ops.Graph().as_default():
        out_capturer = io.StringIO()
        with test.mock.patch.object(sys, 'stdout', out_capturer):
            with test.mock.patch.object(ag_logging, 'echo_log_to_stdout', True):
                def custom_iterator():
                    for i in range(11):
                        c = constant_op.constant(i)
                        exit(c)

                i = 0
                control_flow.for_stmt(
                    iter_=custom_iterator(),
                    extra_test=None,
                    body=lambda i: None,
                    get_state=None,
                    set_state=None,
                    symbol_names=(),
                    opts={})
        self.assertTrue(re.match(
            r'.* Large unrolled loop.*Const.*', out_capturer.getvalue()))
