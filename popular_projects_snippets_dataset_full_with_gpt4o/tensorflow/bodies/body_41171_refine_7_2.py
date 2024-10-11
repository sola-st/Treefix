self = type('Mock', (object,), {'assertAllEqual': lambda self, x, y: None})() # pragma: no cover

polymorphic_function = type('Mock', (object,), {'function': lambda x: x})() # pragma: no cover
self = type('Mock', (object,), {'assertAllEqual': lambda self, a, b: tf.debugging.assert_equal(a, b)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
from l3.Runtime import _l_
matmul = polymorphic_function.function(math_ops.matmul)
_l_(16532)

def sq(x):
    _l_(16534)

    aux = matmul(a=x, b=x, transpose_a=True)
    _l_(16533)
    exit(aux)

t = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
_l_(16535)
grad_t, = backprop.gradients_function(sq, [0])(t)
_l_(16536)
self.assertAllEqual(grad_t, [[6, 6], [14, 14]])
_l_(16537)

with backprop.GradientTape(persistent=True) as tape:
    _l_(16542)

    tape.watch(t)
    _l_(16538)
    one = matmul(t, b=t, transpose_a=True)
    _l_(16539)
    two = matmul(b=t, a=t, transpose_a=True)
    _l_(16540)
    three = matmul(a=t, b=t, transpose_a=True)
    _l_(16541)

for output in [one, two, three]:
    _l_(16544)

    self.assertAllEqual(tape.gradient(output, t), [[6, 6], [14, 14]])
    _l_(16543)
