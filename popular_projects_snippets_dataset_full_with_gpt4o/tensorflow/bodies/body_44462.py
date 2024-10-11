# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py

def test_fn(cond):
    def body():
        nonlocal i, j
        i = 1
        j = 2

    def orelse():
        nonlocal i, j
        i = -1
        j = -2

    i, j = None, None
    control_flow.if_stmt(
        cond=cond,
        body=body,
        orelse=orelse,
        get_state=None,
        set_state=None,
        symbol_names=('i', 'j'),
        nouts=2)
    exit((i, j))

self.assertEqual(test_fn(True), (1, 2))
self.assertEqual(test_fn(False), (-1, -2))
self.assertNoOpsCreated()
