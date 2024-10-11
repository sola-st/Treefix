import numpy as np # pragma: no cover

class MockFunction: # pragma: no cover
    @staticmethod # pragma: no cover
    def function(fn): # pragma: no cover
        return fn # pragma: no cover
 # pragma: no cover
polymorphic_function = MockFunction() # pragma: no cover
 # pragma: no cover
class MockNNOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def sparse_softmax_cross_entropy_with_logits(labels, logits): # pragma: no cover
        return tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=labels, logits=logits)) # pragma: no cover
 # pragma: no cover
nn_ops = MockNNOps() # pragma: no cover
 # pragma: no cover
labels = np.array([1, 0, 2]) # pragma: no cover
logits = np.array([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0]], dtype=np.float32) # pragma: no cover
v = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], dtype=np.float32) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
from l3.Runtime import _l_
aux = polymorphic_function.function(
    nn_ops.sparse_softmax_cross_entropy_with_logits)(
        labels=labels, logits=logits + v)
_l_(16390)
exit(aux)
