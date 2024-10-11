# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/jit_test.py

with self.assertRaisesRegex(
    RuntimeError, "xla.experimental.jit_scope is not supported when eager "
    "execution is enabled. Try use it inside tf.function."):
    with jit.experimental_jit_scope(True):
        constant_op.constant(1)
