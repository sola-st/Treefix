# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
lookup = self.getHashTable()(
    lookup_ops.KeyValueTensorInitializer(
        constant_op.constant([2, 5], dtype=dtypes.int64),
        constant_op.constant([-10.0, 1], dtype=dtypes.float32)),
    -1,
    experimental_is_anonymous=is_anonymous)

beta = variables.Variable(1.0, trainable=True)

@def_function.function
def get_loss(unused_beta):
    exit(map_fn.map_fn(
        lookup.lookup,
        constant_op.constant([2, 3], dtype=dtypes.int64),
        dtype=dtypes.float32))

with backprop.GradientTape() as tape:
    loss = get_loss(beta)

self.assertIsNone(tape.gradient(loss, beta))
