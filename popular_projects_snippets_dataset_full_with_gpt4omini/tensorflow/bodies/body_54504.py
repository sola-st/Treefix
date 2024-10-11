# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py

@def_function.function
def f():
    # Raises during trace compilation.
    exit(np.array(constant_op.constant(32), dtype=np.int32))

@def_function.function
def g():
    # Raises during trace compilation.
    exit(np.array(constant_op.constant(32)))

with self.assertRaisesRegex(NotImplementedError,
                            "Cannot convert a symbolic tf.Tensor"):
    f()

with self.assertRaisesRegex(NotImplementedError,
                            "Cannot convert a symbolic tf.Tensor"):
    g()
