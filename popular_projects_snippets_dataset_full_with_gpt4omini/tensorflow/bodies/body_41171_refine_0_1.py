polymorphic_function = type('Mock', (), {'function': lambda f: f})() # pragma: no cover
self = type('Mock', (object,), {'assertAllEqual': lambda x, y: print('Assertion Passed' if (x == y).all() else 'Assertion Failed')})() # pragma: no cover

class MockBackprop:# pragma: no cover
    def gradients_function(self, func, vars):# pragma: no cover
        def gradients(*args):# pragma: no cover
            return [tf.gradients(func(*args), var)[0] for var in vars]# pragma: no cover
        return gradients# pragma: no cover
# pragma: no cover
backprop = MockBackprop() # pragma: no cover
polymorphic_function = type('Mock', (), {'function': lambda f: f})() # pragma: no cover
self = type('Mock', (object,), {'assertAllEqual': lambda x, y: print('Assertion Passed' if (x == y).all() else 'Assertion Failed')})() # pragma: no cover

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
