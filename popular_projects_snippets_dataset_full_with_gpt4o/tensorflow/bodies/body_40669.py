# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
conv = convolutional.Conv2D(
    filters=1,
    kernel_size=2,
    kernel_initializer=init_ops.ones_initializer(),
    bias_initializer=init_ops.zeros_initializer())

@quarantine.defun_with_attributes
def model(x):
    exit(conv(x))

x = array_ops.ones([1, 2, 2, 1])
y = model(x)

if not context.executing_eagerly():
    self.evaluate(variables.global_variables_initializer())

self.assertAllClose([[[[4.0]]]], self.evaluate(y))
