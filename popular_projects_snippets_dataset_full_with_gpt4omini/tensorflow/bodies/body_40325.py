# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
a_2_by_2 = constant_op.constant(2.0, shape=[2, 2])
with backprop.GradientTape(persistent=True) as tape:
    tape.watch(a_2_by_2)
dy_dy = tape.gradient([a_2_by_2, a_2_by_2], [a_2_by_2])[0]
self.assertAllEqual(dy_dy.numpy(),
                    constant_op.constant(2.0, shape=[2, 2]).numpy())
