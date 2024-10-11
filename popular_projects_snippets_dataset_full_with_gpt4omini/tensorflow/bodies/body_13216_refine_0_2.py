gen_functional_ops = type('Mock', (object,), {'fake_param': staticmethod(lambda dtype, shape: tf.constant(0, dtype=dtype, shape=shape))})() # pragma: no cover
_convert_dynamic_dimension_to_zero = lambda shape: tuple(0 if d is None else d for d in shape) # pragma: no cover

gen_functional_ops = type('Mock', (object,), {'fake_param': staticmethod(lambda dtype, shape: tf.constant(0, dtype=dtype, shape=shape))})() # pragma: no cover
_convert_dynamic_dimension_to_zero = lambda shape: tuple(0 for _ in shape) # pragma: no cover

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
