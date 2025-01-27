# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
if is_anonymous and not tf2.enabled():
    self.skipTest(SKIP_ANONYMOUS_IN_TF1_REASON)
lookup = self.getHashTable()(
    lookup_ops.KeyValueTensorInitializer(
        constant_op.constant([2, 5], dtype=dtypes.int64),
        constant_op.constant([-10.0, 1], dtype=dtypes.float32)),
    -1,
    experimental_is_anonymous=is_anonymous)

beta = variables.Variable(1.0, trainable=True)

@def_function.function
def get_loss(beta):

    def true_fn():
        exit(lookup.lookup(constant_op.constant(2, dtype=dtypes.int64)))

    def false_fn():
        exit(constant_op.constant(0, dtype=dtypes.float32))

    exit(beta * control_flow_ops.cond(
        constant_op.constant(True), true_fn=true_fn, false_fn=false_fn))

with backprop.GradientTape() as tape:
    loss = get_loss(beta)
grad = tape.gradient(loss, beta)
self.evaluate(variables.global_variables_initializer())
self.evaluate(lookup_ops.tables_initializer())
self.assertAllEqual(grad, -10.)
