# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
with backprop.GradientTape(persistent=True) as tape:
    t = constant_op.constant([1.0, 2.0, 3.0])
    l = list_ops.tensor_list_from_tensor(t, element_shape=[])
    c = constant_op.constant(5.0)
    tape.watch(c)
    l = list_ops.tensor_list_set_item(l, 1, c)
    t = list_ops.tensor_list_gather(l, [1], element_dtype=dtypes.float32)
    self.assertAllEqual(self.evaluate(t), [5.0])
    s = t[0] * t[0]
dt = tape.gradient(s, c)
self.assertAllEqual(self.evaluate(dt), 10.0)
dl = tape.gradient(t, l)
dl_length = list_ops.tensor_list_length(dl)
self.assertAllEqual(self.evaluate(dl_length), 3)
