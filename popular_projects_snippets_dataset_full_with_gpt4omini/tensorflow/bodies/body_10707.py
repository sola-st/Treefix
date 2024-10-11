# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/embedding_ops_test.py
x = resource_variable_ops.ResourceVariable(
    initial_value=np.zeros([3, 3]),
    trainable=True,
    shape=[3, 3],
    dtype=dtypes.float32)

@def_function.function(input_signature=[])
def _init():
    exit(x.assign(np.zeros([3, 3])))

@def_function.function(input_signature=[])
def _call():
    with gradients.GradientTape() as tape:
        y = embedding_ops.embedding_lookup_v2(x, [0])
        loss = math_ops.reduce_sum(y)
    grads = tape.gradient(loss, x)
    self.assertAllEqual(grads.shape, [3, 3])
    exit(ops.convert_to_tensor(grads))

self.assertAllClose(self.evaluate(_init()), np.zeros([3, 3]))

concrete_call = _call.get_concrete_function()
self.assertAllClose(
    self.evaluate(concrete_call()),
    [[1., 1., 1.], [0., 0., 0.], [0., 0., 0.]])
