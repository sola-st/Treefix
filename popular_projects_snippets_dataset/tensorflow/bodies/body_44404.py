# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py

class UserType:
    pass

def body():
    nonlocal v
    v = UserType()

def set_state(loop_vars):
    nonlocal v
    v, = loop_vars

v = variable_operators.Undefined('v')

with self.assertRaisesRegex(
    ValueError,
    re.compile('must be defined.*tried to define.*unsupported type',
               re.DOTALL)):
    control_flow.while_stmt(
        test=lambda: constant_op.constant(True),
        body=body,
        get_state=lambda: (v,),
        set_state=set_state,
        symbol_names=('v',),
        opts={})
