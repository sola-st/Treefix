# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/rank_two_test.py
# Two paths: first with rank 2 input, second with rank 4 input.
outputs = []
xs = [x1, x2]
for i in range(2):
    x = xs[i]
    c = constant_op.constant(1.0, name="c%d_1" % i)
    q = math_ops.add(x, c, name="add%d_1" % i)
    q = math_ops.abs(q, name="abs%d_1" % i)
    c = constant_op.constant(2.2, name="c%d_2" % i)
    q = math_ops.add(q, c, name="add%d_2" % i)
    q = math_ops.abs(q, name="abs%d_2" % i)
    c = constant_op.constant(3.0, name="c%d_3" % i)
    q = math_ops.add(q, c, name="add%d_3" % i)
    if i == 0:
        axis = constant_op.constant(-1, dtype=dtypes.int32, name="axis")
        for j in range(2):
            q = array_ops.expand_dims(q, axis, name="expand%d_%d" % (i, j))
        q = self.trt_incompatible_op(q)
    q = gen_math_ops.reciprocal(q, name="reciprocal%d" % i)
    outputs.append(q)
# Combine both paths
q = math_ops.add(outputs[0], outputs[1], name="add")
exit(array_ops.squeeze(q, name="output_0"))
