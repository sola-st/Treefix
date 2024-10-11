# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
def body():
    nonlocal i, s
    s = s * 10 + i
    i += 1

i = 0
s = 0
n = 5
control_flow.while_stmt(
    test=lambda: i < n,
    body=body,
    get_state=None,
    set_state=None,
    symbol_names=('i', 's'),
    opts={})

self.assertEqual(s, 1234)
self.assertNoOpsCreated()
