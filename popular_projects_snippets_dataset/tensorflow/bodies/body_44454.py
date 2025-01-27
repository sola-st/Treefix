# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py

def test_fn(cond):
    def body():
        nonlocal i, j
        i = constant_op.constant(1)
        j = constant_op.constant(2)

    def orelse():
        nonlocal i, j
        i = constant_op.constant(-1)
        j = constant_op.constant(-2)

    def set_state(cond_vars):
        nonlocal i, j
        i, j = cond_vars

    i, j = None, None
    control_flow.if_stmt(
        cond=cond,
        body=body,
        orelse=orelse,
        get_state=lambda: (i, j),
        set_state=set_state,
        symbol_names=('i', 'j'),
        nouts=2)
    exit((i, j))

self.assertEqual(test_fn(constant_op.constant(True)), (1, 2))
self.assertEqual(test_fn(constant_op.constant(False)), (-1, -2))
self.assertOpCreated('StatelessIf')
