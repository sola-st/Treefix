self = type('Mock', (object,), {'assertAllEqual': lambda s, x, y: None})() # pragma: no cover

nn_grad = None # pragma: no cover
self = type('Mock', (object,), {'assertAllEqual': lambda s, x, y: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py

# This test needs nn_grad imported. We could just disable the lint error,
# but this way if the test is deleted we'll know the import isn't needed.
from l3.Runtime import _l_
_ = nn_grad
_l_(21623)

v = variables.Variable(1.)
_l_(21624)

@polymorphic_function.function
def f(labels, logits):
    _l_(21626)

    aux = polymorphic_function.function(
        nn_ops.sparse_softmax_cross_entropy_with_logits)(
            labels=labels, logits=logits + v)
    _l_(21625)
    exit(aux)

@polymorphic_function.function
def f_grad():
    _l_(21632)

    with backprop.GradientTape() as tape:
        _l_(21630)

        logits = constant_op.constant([1., 2.])
        _l_(21627)
        tape.watch(logits)
        _l_(21628)
        out = f(constant_op.constant(1), logits)
        _l_(21629)
    aux = tape.gradient(out, logits)
    _l_(21631)
    exit(aux)
# Mainly we want to check that the function builds despite
# sparse_softmax_cross_entropy_with_logits not having a second-order
# gradient defined.
self.assertAllEqual([2], f_grad().shape)
_l_(21633)
