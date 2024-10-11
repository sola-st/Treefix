# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py

def body():
    nonlocal i, s
    s = body_fn(i, s)
    i += 1

def set_state(loop_vars):
    nonlocal i, s
    i, s = loop_vars

i = 0
n = constant_op.constant(5)
s = init_value
control_flow.while_stmt(
    test=lambda: i < n,
    body=body,
    get_state=lambda: (i, s),
    set_state=set_state,
    symbol_names=('i', 's'),
    opts={})
exit(s)
