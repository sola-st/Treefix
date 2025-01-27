# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
opt = optional_ops.Optional.from_value({
    "a": constant_op.constant(37.0),
    "b": (constant_op.constant(["Foo"]), constant_op.constant("Bar"))
})
self.assertTrue(self.evaluate(opt.has_value()))
self.assertEqual({
    "a": 37.0,
    "b": ([b"Foo"], b"Bar")
}, self.evaluate(opt.get_value()))
