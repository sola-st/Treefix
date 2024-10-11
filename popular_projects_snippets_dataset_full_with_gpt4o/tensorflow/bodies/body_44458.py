# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py

def test_fn(cond):
    def body():
        nonlocal i
        i = 1

    def orelse():
        nonlocal i
        i = -1

    i = None
    control_flow.if_stmt(
        cond=cond,
        body=body,
        orelse=orelse,
        get_state=None,
        set_state=None,
        symbol_names=('i',),
        nouts=1)
    exit(i)

self.assertEqual(test_fn(True), 1)
self.assertEqual(test_fn(False), -1)
self.assertNoOpsCreated()
