import numpy as np # pragma: no cover

func_graph = type('MockFuncGraph', (object,), {'as_default': lambda self: ops.Graph().as_default()})() # pragma: no cover
template_tensors = [type('MockTensor', (object,), {'dtype': np.float32, 'shape': (10, 10)})()] # pragma: no cover
gen_functional_ops = type('MockGenFunctionalOps', (object,), {'fake_param': lambda dtype, shape: f'fake_param({dtype}, {shape})'}) # pragma: no cover
_convert_dynamic_dimension_to_zero = lambda shape: [dim if dim is not None else 0 for dim in shape] # pragma: no cover

_convert_dynamic_dimension_to_zero = lambda shape: [0 if dim is None else dim for dim in shape] # pragma: no cover
gen_functional_ops = type('Mock', (object,), {'fake_param': lambda dtype, shape: tf.zeros(shape, dtype)}) # pragma: no cover

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
