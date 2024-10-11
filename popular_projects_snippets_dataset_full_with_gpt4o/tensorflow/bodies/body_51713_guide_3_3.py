class MockBuildSignatureDef: # pragma: no cover
    @staticmethod # pragma: no cover
    def build_signature_def(inputs, outputs): # pragma: no cover
        return {'inputs': inputs, 'outputs': outputs} # pragma: no cover
 # pragma: no cover
class MockBuildTensorInfo: # pragma: no cover
    @staticmethod # pragma: no cover
    def build_tensor_info(tensor): # pragma: no cover
        return {'name': tensor.name, 'dtype': tensor.dtype.name, 'shape': tensor.shape.as_list()} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_test.py
from l3.Runtime import _l_
g = ops.Graph()
_l_(19554)
with g.as_default():
    _l_(19560)

    x = variables.VariableV1(5, name="x")
    _l_(19555)
    y = variables.VariableV1(11, name="y")
    _l_(19556)
    z = x + y
    _l_(19557)

    foo_sig_def = signature_def_utils.build_signature_def({
        "foo_input": utils.build_tensor_info(x)
    }, {"foo_output": utils.build_tensor_info(z)})
    _l_(19558)
    bar_sig_def = signature_def_utils.build_signature_def({
        "bar_x": utils.build_tensor_info(x),
        "bar_y": utils.build_tensor_info(y)
    }, {"bar_z": utils.build_tensor_info(z)})
    _l_(19559)
aux = (g, {"foo": foo_sig_def, "bar": bar_sig_def}, y)
_l_(19561)
exit(aux)
