polymorphic_function = type('Mock', (object,), {'function': lambda self, x: x})() # pragma: no cover
self = type('Mock', (object,), {'assertAllEqual': lambda self, x, y: print('Assertion:', x == y)})() # pragma: no cover
nn_ops = type('Mock', (object,), {'sparse_softmax_cross_entropy_with_logits': lambda labels, logits: tf.reduce_sum(logits)})() # pragma: no cover

polymorphic_function = type('Mock', (object,), {'function': lambda x: x}) # pragma: no cover
self = type('Mock', (object,), {'assertAllEqual': staticmethod(lambda x, y: print('Assertion:', x == y))}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py

# This test needs nn_grad imported. We could just disable the lint error,
# but this way if the test is deleted we'll know the import isn't needed.
from l3.Runtime import _l_
_ = nn_grad
_l_(9261)

v = variables.Variable(1.)
_l_(9262)

@polymorphic_function.function
def f(labels, logits):
    _l_(9264)

    aux = polymorphic_function.function(
        nn_ops.sparse_softmax_cross_entropy_with_logits)(
            labels=labels, logits=logits + v)
    _l_(9263)
    exit(aux)

@polymorphic_function.function
def f_grad():
    _l_(9270)

    with backprop.GradientTape() as tape:
        _l_(9268)

        logits = constant_op.constant([1., 2.])
        _l_(9265)
        tape.watch(logits)
        _l_(9266)
        out = f(constant_op.constant(1), logits)
        _l_(9267)
    aux = tape.gradient(out, logits)
    _l_(9269)
    exit(aux)
# Mainly we want to check that the function builds despite
# sparse_softmax_cross_entropy_with_logits not having a second-order
# gradient defined.
self.assertAllEqual([2], f_grad().shape)
_l_(9271)
