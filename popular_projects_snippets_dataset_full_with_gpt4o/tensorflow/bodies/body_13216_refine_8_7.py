class MockFunctionalOps:# pragma: no cover
    @staticmethod# pragma: no cover
    def fake_param(dtype, shape):# pragma: no cover
        return tf.constant(0, dtype=dtype, shape=shape)# pragma: no cover
gen_functional_ops = MockFunctionalOps() # pragma: no cover
def _convert_dynamic_dimension_to_zero(shape):# pragma: no cover
    return [dim if dim is not None else 0 for dim in shape] # pragma: no cover

class MockFuncGraph:# pragma: no cover
    def as_default(self):# pragma: no cover
        return tf.Graph().as_default()# pragma: no cover
func_graph = MockFuncGraph() # pragma: no cover
def _convert_dynamic_dimension_to_zero(shape):# pragma: no cover
    return [dim if dim is not None else 0 for dim in shape] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
from l3.Runtime import _l_
"""Creates FakeParams for the XLA case."""
with func_graph.as_default():
    _l_(16865)

    aux = [
        gen_functional_ops.fake_param(
            dtype=t.dtype, shape=_convert_dynamic_dimension_to_zero(t.shape))
        for t in template_tensors]
    _l_(16864)
    exit(aux)
