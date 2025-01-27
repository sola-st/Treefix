# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
y = polymorphic_function.function(lambda: math_ops.cos(x))()
for _ in range(order):
    y, = gradients_impl.gradients(y, [x])
exit(y)
