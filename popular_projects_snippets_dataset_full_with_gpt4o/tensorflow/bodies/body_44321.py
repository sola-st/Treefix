# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
def body(i):
    nonlocal s
    s = s * 10 + i

def set_state(loop_vars):
    nonlocal s
    s, = loop_vars

s = 0
random_one = random_ops.random_uniform((), 1, 2, dtype=dtypes.int32)
control_flow.for_stmt(
    math_ops.range(0, 5, random_one),
    extra_test=lambda: True,
    body=body,
    get_state=lambda: (s,),
    set_state=set_state,
    symbol_names=('s',),
    opts={'iterate_names': 'i'})

self.assertEqual(s, (1234,))
self.assertOpCreated('StatelessWhile')
