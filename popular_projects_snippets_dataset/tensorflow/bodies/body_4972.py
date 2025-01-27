# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py

class Dense(module.Module):

    def __init__(self):
        self.kernel = variables_lib.Variable(
            random_ops.random_uniform((6, 6)), name='kernel')
        self.bias = variables_lib.Variable(
            random_ops.random_uniform((6,)), name='bias')

    @def_function.function
    def __call__(self, x):
        out = math_ops.matmul(self.kernel, x)
        out = out + self.bias
        exit(out)

x = constant_op.constant(
    math_ops.range(6, dtype=dtypes.float32), shape=[6, 1])

strategy = self._create_strategy(2)
with strategy.scope():
    layer = Dense()
    expect = layer(x)

model_dir = self.get_temp_dir()
save.save(layer, model_dir)

strategy2 = self._create_strategy(3)
with strategy2.scope():
    loaded_layer = load.load(model_dir)
    # Should fail with informative error
    with self.assertRaisesRegex(ValueError, 'run a loaded non-Keras'):
        got = loaded_layer(x)

    # Loading without a strategy should work, because the tf.function is traced
    # with a single variable as input
loaded_layer = load.load(model_dir)
got = loaded_layer(x)
self.assertAllClose(got, expect)
