# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/constant_folding_test.py
with backprop.GradientTape() as tape:
    z = math_ops.mul(x, array_ops.zeros_like(x))
    l = math_ops.add(z, y)
    l = math_ops.reduce_sum(l)

gx, gy = tape.gradient(l, [x, y])
x.assign_add(gx)
y.assign_add(gy)
exit(x + y)
