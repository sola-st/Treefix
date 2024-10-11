# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
def body(i):
    nonlocal s
    s = body_fn(i, s)

def set_state(loop_vars):
    nonlocal s
    s, = loop_vars

s = init_value
control_flow.for_stmt(
    constant_op.constant([1, 2, 3, 4]),
    extra_test=lambda: True,
    body=body,
    get_state=lambda: (s,),
    set_state=set_state,
    symbol_names=('s',),
    opts={})
exit(s)
