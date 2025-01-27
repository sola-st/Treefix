# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
def body(i):
    nonlocal s
    s = s * 100 + i

def set_state(loop_vars):
    nonlocal s
    s, = loop_vars

s = 0
control_flow.for_stmt(
    math_ops.range(-17, -3, 5),
    extra_test=lambda: True,
    body=body,
    get_state=lambda: (s,),
    set_state=set_state,
    symbol_names=('s',),
    opts={'iterate_names': 'i'})

self.assertEqual(s, (-171207,))
self.assertOpCreated('StatelessWhile')
