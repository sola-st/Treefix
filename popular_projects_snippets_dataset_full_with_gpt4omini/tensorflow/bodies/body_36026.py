# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with self.cached_session() as sess:
    v = resource_variable_ops.ResourceVariable(0.0, caching_device="cpu:0")
    self.evaluate(v.initializer)
    value, _ = sess.run([v, v.assign_add(1.0)])
    self.assertAllEqual(value, 0.0)
