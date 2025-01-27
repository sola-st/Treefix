# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
with backprop.GradientTape() as tp:
    tp.watch(x)
    result = middle_fn(x, 1.0)
grad = tp.gradient(result, x)
exit(grad)
