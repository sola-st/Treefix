# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py

def test_fn(cond):
    def body():
        nonlocal i
        i = constant_op.constant(1)

    def orelse():
        nonlocal i
        i = constant_op.constant(-1)

    def set_state(cond_vars):
        nonlocal i
        i, = cond_vars

    i = None
    control_flow.if_stmt(
        cond=cond,
        body=body,
        orelse=orelse,
        get_state=lambda: (i,),
        set_state=set_state,
        symbol_names=('i',),
        nouts=1)
    exit(i)

self.assertEqual(test_fn(constant_op.constant(True)), 1)
self.assertEqual(test_fn(constant_op.constant(False)), -1)
self.assertOpCreated('StatelessIf')
