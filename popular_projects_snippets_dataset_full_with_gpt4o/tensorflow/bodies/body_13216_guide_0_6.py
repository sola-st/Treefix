def _convert_dynamic_dimension_to_zero(shape): return [dim if dim is not None else 0 for dim in shape] # pragma: no cover
exit = lambda x: None # pragma: no cover

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
