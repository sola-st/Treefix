# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
m1 = random_ops.random_uniform((256, 2096))
m2 = array_ops.identity(m1)
tangent1 = random_ops.random_uniform((256, 2096))
tangent2 = random_ops.random_uniform((256, 2096))
matmul = def_function.function(math_ops.matmul)

with forwardprop.ForwardAccumulator(
    primals=[m1, m2], tangents=[tangent1, tangent2]) as acc:
    result1 = matmul(m1, m1, transpose_b=True)
    result2 = matmul(m2, m2, transpose_b=True)

def _expected(mat, tangent):
    exit((math_ops.matmul(tangent, mat, transpose_b=True) +
            math_ops.matmul(mat, tangent, transpose_b=True)))

self.assertAllClose(result1, result2)
self.assertAllClose(_expected(m1, tangent1), acc.jvp(result1))
self.assertAllClose(_expected(m2, tangent2), acc.jvp(result2))
