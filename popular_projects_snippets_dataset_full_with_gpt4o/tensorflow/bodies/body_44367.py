# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
def body(i):
    nonlocal s
    s = s * 10 + i[0]

def set_state(loop_vars):
    nonlocal s
    s, = loop_vars

s = 0
control_flow.for_stmt(
    ragged_factory_ops.constant([[1], [2, 4], [3]]),
    extra_test=None,
    body=body,
    get_state=lambda: (s,),
    set_state=set_state,
    symbol_names=('s',),
    opts={})

self.assertEqual(s, (123,))
self.assertOpCreated('StatelessWhile')
