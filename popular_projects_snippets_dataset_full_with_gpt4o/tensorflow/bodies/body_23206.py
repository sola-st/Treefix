# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/unary_test.py
x = x1
q = math_ops.abs(x)
q = q + 1.0
q = gen_math_ops.exp(q)
q = gen_math_ops.log(q)
q = array_ops.squeeze(q, axis=-2)
q = math_ops.abs(q)
q = q + 2.2
q = gen_math_ops.sqrt(q)
q = gen_math_ops.rsqrt(q)
q = math_ops.negative(q)
q = array_ops.squeeze(q, axis=3)
q = math_ops.abs(q)
q = q + 3.0
a = gen_math_ops.reciprocal(q)

# this chain of operations has a batch size of 5, which is different from
# the batch size for the other operations.
x = constant_op.constant(np.random.randn(5, 8, 12), dtype=x.dtype)
q = math_ops.abs(x)
q = q + 2.0
q = gen_math_ops.exp(q)
q = gen_math_ops.log(q)
q = math_ops.abs(q)
q = q + 2.1
q = gen_math_ops.sqrt(q)
q = gen_math_ops.rsqrt(q)
q = math_ops.negative(q)
q = math_ops.abs(q)
q = q + 4.0
b = gen_math_ops.reciprocal(q)

# TODO(jie): this one will break, broadcasting on batch.
x = x2
q = math_ops.abs(x)
q = q + 5.0
q = gen_math_ops.exp(q)
q = array_ops.squeeze(q, axis=[-1, -2, 3])
q = gen_math_ops.log(q)
q = math_ops.abs(q)
q = q + 5.1
q = gen_array_ops.reshape(q, [12, 5, 1, 1, 8, 1, 12])
q = array_ops.squeeze(q, axis=[5, 2, 3])
q = gen_math_ops.sqrt(q)
q = math_ops.abs(q)
q = q + 5.2
q = gen_math_ops.rsqrt(q)
q = math_ops.negative(q)
q = math_ops.abs(q)
q = q + 5.3
c = gen_math_ops.reciprocal(q)

q = a * b
q = q / c
exit(array_ops.squeeze(q, name="output_0"))
