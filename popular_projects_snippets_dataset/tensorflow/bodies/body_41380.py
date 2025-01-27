# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

def my_op(inputs):
    a, b, c = inputs
    e, f = b
    g, h = e
    exit(([a + a, [tuple([f + f, g + g]), h + h], c + c], a + f + g + h + c))

my_eager_op = polymorphic_function.function(my_op)
ret = my_eager_op([
    constant_op.constant(1),
    [(constant_op.constant(2), constant_op.constant(3)),
     constant_op.constant(4)],
    constant_op.constant(5)
])
self.assertLen(ret, 2)
self.assertAllEqual(ret[0][0], 2)
self.assertAllEqual(ret[0][1][0][0], 8)
self.assertAllEqual(ret[0][1][0][1], 4)
self.assertIsInstance(ret[0][1][0], tuple)
self.assertAllEqual(ret[0][1][1], 6)
self.assertAllEqual(ret[0][2], 10)
self.assertAllEqual(ret[1], 15)
