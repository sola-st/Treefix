# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
def body():
    nonlocal x
    x = body_fn()

def orelse():
    nonlocal x
    x = else_fn()

def set_state(cond_vars):
    nonlocal x
    x, = cond_vars

x = 0
control_flow.if_stmt(
    cond=constant_op.constant(True),
    body=body,
    orelse=orelse,
    get_state=lambda: (x,),
    set_state=set_state,
    symbol_names=('x',),
    nouts=1)
exit(x)
