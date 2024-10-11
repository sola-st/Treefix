# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py

def body():
    nonlocal i, s
    i = constant_op.constant(2)
    raise ValueError('testing')
    s = i ** 5  # pylint: disable=unreachable

def set_state(loop_vars):
    nonlocal i, s
    i, s = loop_vars

i = variable_operators.Undefined('i')
s = constant_op.constant(0)

with self.assertRaisesRegex(
    ValueError,
    re.compile('must be defined.*tried to define.*testing', re.DOTALL)):
    control_flow.while_stmt(
        test=lambda: math_ops.equal(s, 0),
        body=body,
        get_state=lambda: (i, s),
        set_state=set_state,
        symbol_names=('i', 's'),
        opts={})
