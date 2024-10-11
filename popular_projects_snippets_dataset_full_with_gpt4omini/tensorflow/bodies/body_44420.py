# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
if not __debug__:
    self.skipTest('Feature disabled in optimized mode.')
with test.mock.patch.object(
    control_flow, 'INEFFICIENT_UNROLL_MIN_ITERATIONS', 10):
    with ops.Graph().as_default():
        out_capturer = io.StringIO()
        with test.mock.patch.object(sys, 'stdout', out_capturer):
            with test.mock.patch.object(ag_logging, 'echo_log_to_stdout', True):
                def body():
                    nonlocal i
                    gen_math_ops.add(i, 1)
                    i += 1

                i = 0
                control_flow.while_stmt(
                    test=lambda: i < 100,
                    body=body,
                    get_state=None,
                    set_state=None,
                    symbol_names=('i',),
                    opts={})
        self.assertTrue(re.match(
            r'.* Large unrolled loop.*Add.*', out_capturer.getvalue()))
