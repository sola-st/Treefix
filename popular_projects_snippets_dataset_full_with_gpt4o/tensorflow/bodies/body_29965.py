# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
s = constant_op.constant("uiuc")
self.assertEqual(s.numpy().decode("utf-8"), "uiuc")
s_array = constant_op.constant(["mit", "stanford"])
self.assertAllEqual(s_array.numpy(), ["mit", "stanford"])

with ops.device("/cpu:0"):
    s = constant_op.constant("cmu")
    self.assertEqual(s.numpy().decode("utf-8"), "cmu")

    s_array = constant_op.constant(["berkeley", "ucla"])
    self.assertAllEqual(s_array.numpy(), ["berkeley", "ucla"])
