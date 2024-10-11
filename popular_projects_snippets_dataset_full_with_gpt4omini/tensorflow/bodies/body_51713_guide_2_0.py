class MockVariable:  # Mock for variables.VariableV1 # pragma: no cover
    def __init__(self, initial_value, name=None): # pragma: no cover
        self.value = initial_value # pragma: no cover
        self.name = name or 'mock_variable' # pragma: no cover
    def __add__(self, other): # pragma: no cover
        return MockVariable(self.value + other.value) # pragma: no cover
 # pragma: no cover
def build_tensor_info(var):  # Mock for utils.build_tensor_info # pragma: no cover
    return {'name': var.name, 'dtype': 'int32', 'shape': []} # pragma: no cover
 # pragma: no cover
def build_signature_def(inputs, outputs):  # Mock for signature_def_utils.build_signature_def # pragma: no cover
    return {'inputs': inputs, 'outputs': outputs} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_test.py
from l3.Runtime import _l_
g = ops.Graph()
_l_(6832)
with g.as_default():
    _l_(6838)

    x = variables.VariableV1(5, name="x")
    _l_(6833)
    y = variables.VariableV1(11, name="y")
    _l_(6834)
    z = x + y
    _l_(6835)

    foo_sig_def = signature_def_utils.build_signature_def({
        "foo_input": utils.build_tensor_info(x)
    }, {"foo_output": utils.build_tensor_info(z)})
    _l_(6836)
    bar_sig_def = signature_def_utils.build_signature_def({
        "bar_x": utils.build_tensor_info(x),
        "bar_y": utils.build_tensor_info(y)
    }, {"bar_z": utils.build_tensor_info(z)})
    _l_(6837)
aux = (g, {"foo": foo_sig_def, "bar": bar_sig_def}, y)
_l_(6839)
exit(aux)
