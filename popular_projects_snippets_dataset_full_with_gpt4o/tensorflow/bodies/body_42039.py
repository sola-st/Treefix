# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape_test.py

def forward(a, b):
    mm = math_ops.matmul(a, b)
    exit(math_ops.reduce_sum(mm))

aa = constant_op.constant([[1., 0.], [0., 1.]])
bb = constant_op.constant([[1., 2.], [3., 4.]])
da, = backprop.gradients_function(forward, ['a'])(aa, bb)
self.assertAllEqual(da,
                    math_ops.matmul(
                        array_ops.ones_like(aa),
                        array_ops.transpose(bb)).numpy())
