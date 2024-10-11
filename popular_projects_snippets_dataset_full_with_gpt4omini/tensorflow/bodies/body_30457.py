# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
# Numpy does not support padding strings so we compare padding manually.
x = ops.convert_to_tensor([["Hello", "World"],
                           ["Goodnight", "Moon"]])

constant = array_ops.pad(x, [[1, 0], [0, 1]], mode="CONSTANT",
                         constant_values="PAD")
reflect = array_ops.pad(x, [[1, 0], [0, 1]], mode="REFLECT",
                        constant_values="PAD")
symmetric = array_ops.pad(x, [[1, 0], [0, 1]], mode="SYMMETRIC",
                          constant_values="PAD")
with test_util.use_gpu():
    self.assertAllEqual(
        [[b"PAD", b"PAD", b"PAD"], [b"Hello", b"World", b"PAD"],
         [b"Goodnight", b"Moon", b"PAD"]], self.evaluate(constant))
    self.assertAllEqual([[b"Goodnight", b"Moon", b"Goodnight"],
                         [b"Hello", b"World", b"Hello"],
                         [b"Goodnight", b"Moon", b"Goodnight"]],
                        self.evaluate(reflect))
    self.assertAllEqual(
        [[b"Hello", b"World", b"World"], [b"Hello", b"World", b"World"],
         [b"Goodnight", b"Moon", b"Moon"]], self.evaluate(symmetric))
