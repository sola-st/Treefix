# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with ops.device("/job:server/task:1"):
    v = resource_variable_ops.ResourceVariable(
        2.0, caching_device="/job:localhost")
    self.assertEqual("/job:localhost", v.value().device)
    with self.assertRaises(ValueError):
        _ = v.value().op.get_attr("_class")

with ops.colocate_with(v.op):
    w = resource_variable_ops.ResourceVariable(
        2.0, caching_device="/job:localhost")
    self.assertEqual("/job:localhost", w.value().device)
    with self.assertRaises(ValueError):
        _ = w.value().op.get_attr("_class")
