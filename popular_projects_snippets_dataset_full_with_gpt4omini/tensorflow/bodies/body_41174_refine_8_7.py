class Mock: pass # pragma: no cover
mock_function = lambda x: x # pragma: no cover
polymorphic_function = type('Mock', (object,), {'function': mock_function})() # pragma: no cover
nn_ops = type('Mock', (object,), {'sparse_softmax_cross_entropy_with_logits': staticmethod(lambda labels, logits: tf.nn.sparse_softmax_cross_entropy_with_logits(labels, logits))})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
from l3.Runtime import _l_
aux = polymorphic_function.function(
    nn_ops.sparse_softmax_cross_entropy_with_logits)(
        labels=labels, logits=logits + v)
_l_(4683)
exit(aux)
