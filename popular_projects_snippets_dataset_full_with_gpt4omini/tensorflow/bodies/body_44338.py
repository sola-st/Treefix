# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
s = 0

def body(i):
    nonlocal s
    s = s * 10 + i

control_flow.for_stmt(
    gen,
    extra_test=lambda: False,  # Break before loop
    body=body,
    get_state=None,
    set_state=None,
    symbol_names=('s',),
    opts={})
exit(s)
