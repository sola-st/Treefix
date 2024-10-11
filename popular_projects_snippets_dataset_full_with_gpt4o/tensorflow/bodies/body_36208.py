# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
# For 0D tensors, the truthiness depends on whether the value is "zero".
self.assertAllEqual(gen_functional_ops.to_bool(0), False)
self.assertAllEqual(gen_functional_ops.to_bool(1), True)
self.assertAllEqual(gen_functional_ops.to_bool(42), True)
self.assertAllEqual(gen_functional_ops.to_bool(0.), False)
self.assertAllEqual(gen_functional_ops.to_bool(1.), True)
self.assertAllEqual(gen_functional_ops.to_bool(42.), True)
self.assertAllEqual(gen_functional_ops.to_bool(False), False)
self.assertAllEqual(gen_functional_ops.to_bool(True), True)
# For strings, "zero" is the empty string.
self.assertAllEqual(gen_functional_ops.to_bool(""), False)
self.assertAllEqual(gen_functional_ops.to_bool("a"), True)

# For >0D tensors, the truthiness only depends on whether there are
# elements or not.
self.assertAllEqual(gen_functional_ops.to_bool([]), False)
self.assertAllEqual(gen_functional_ops.to_bool([[]]), False)
self.assertAllEqual(gen_functional_ops.to_bool([[[]]]), False)
self.assertAllEqual(gen_functional_ops.to_bool([0]), True)
self.assertAllEqual(gen_functional_ops.to_bool([1]), True)
self.assertAllEqual(gen_functional_ops.to_bool([[0]]), True)
self.assertAllEqual(gen_functional_ops.to_bool([False]), True)
self.assertAllEqual(gen_functional_ops.to_bool([True]), True)
