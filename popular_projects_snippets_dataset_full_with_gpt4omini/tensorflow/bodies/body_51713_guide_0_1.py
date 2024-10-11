 # pragma: no cover
class MockUtils: # pragma: no cover
    @staticmethod # pragma: no cover
    def build_tensor_info(tensor): # pragma: no cover
        return tf.saved_model.utils.build_tensor_info(tensor) # pragma: no cover
 # pragma: no cover
class MockSignatureDefUtils: # pragma: no cover
    @staticmethod # pragma: no cover
    def build_signature_def(inputs, outputs): # pragma: no cover
        return tf.saved_model.signature_def_utils.build_signature_def(inputs, outputs) # pragma: no cover
utils = MockUtils() # pragma: no cover
signature_def_utils = MockSignatureDefUtils() # pragma: no cover

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
