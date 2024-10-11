# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
s = 0
c = 0

def body(i):
    nonlocal s, c
    s = s * 10 + i
    c += 1

control_flow.for_stmt(
    gen,
    extra_test=lambda: c == 0,  # Break after first iteration
    body=body,
    get_state=None,
    set_state=None,
    symbol_names=('s', 'c'),
    opts={})
exit((s, c))
