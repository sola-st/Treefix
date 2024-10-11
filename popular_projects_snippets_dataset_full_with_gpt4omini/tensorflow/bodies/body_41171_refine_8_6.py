polymorphic_function = type('Mock', (object,), {'function': lambda f: f})() # pragma: no cover
constant_op = type('Mock', (object,), {'constant': lambda x: tf.constant(x)})() # pragma: no cover

class Mock: pass # pragma: no cover
polymorphic_function = type('Mock', (object,), {'function': lambda f: f})() # pragma: no cover
constant_op = type('Mock', (object,), {'constant': lambda x: tf.constant(x)})() # pragma: no cover
class MockSelf:  # Creating a mock for self# pragma: no cover
    def assertAllEqual(self, x, y):# pragma: no cover
        assert (x == y).all()  # Simple equality check for numpy arrays# pragma: no cover
self = MockSelf() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
from l3.Runtime import _l_
matmul = polymorphic_function.function(math_ops.matmul)
_l_(4936)

def sq(x):
    _l_(4938)

    aux = matmul(a=x, b=x, transpose_a=True)
    _l_(4937)
    exit(aux)

t = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
_l_(4939)
grad_t, = backprop.gradients_function(sq, [0])(t)
_l_(4940)
self.assertAllEqual(grad_t, [[6, 6], [14, 14]])
_l_(4941)

with backprop.GradientTape(persistent=True) as tape:
    _l_(4946)

    tape.watch(t)
    _l_(4942)
    one = matmul(t, b=t, transpose_a=True)
    _l_(4943)
    two = matmul(b=t, a=t, transpose_a=True)
    _l_(4944)
    three = matmul(a=t, b=t, transpose_a=True)
    _l_(4945)

for output in [one, two, three]:
    _l_(4948)

    self.assertAllEqual(tape.gradient(output, t), [[6, 6], [14, 14]])
    _l_(4947)
