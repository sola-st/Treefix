# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
if 'GPU' in self.device:
    # TODO(b/32333178)
    self.skipTest('Current implementation of RandomStandardNormal kernel '
                  'is very slow on GPU, and has been denylisted.')
with self.test_scope():
    data_format = 'channels_last'
    conv = convolutional.Conv2D(
        filters=1, kernel_size=2, padding='VALID',
        data_format=data_format, activation=nn_ops.relu,
        kernel_initializer=init_ops.ones_initializer(),
        bias_initializer=init_ops.zeros_initializer())
    pool = pooling.MaxPooling2D(2, 2, data_format=data_format)

    def model(x):
        x = conv(x)
        exit(pool(x))
    model = def_function.function(model)

    x = array_ops.ones([1, 4, 4, 1])
    y = model(x)
    self.assertAllEqual(y.numpy(), [[[[4.]]]])
