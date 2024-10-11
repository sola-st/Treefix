def _convert_dynamic_dimension_to_zero(shape): return [0] * len(shape) # pragma: no cover
class MockGenFunctionalOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def fake_param(dtype, shape): # pragma: no cover
        return f'fake_param(dtype={dtype}, shape={shape})' # pragma: no cover
gen_functional_ops = MockGenFunctionalOps() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
from l3.Runtime import _l_
"""Creates FakeParams for the XLA case."""
with func_graph.as_default():
    _l_(5337)

    aux = [
        gen_functional_ops.fake_param(
            dtype=t.dtype, shape=_convert_dynamic_dimension_to_zero(t.shape))
        for t in template_tensors]
    _l_(5336)
    exit(aux)
