# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
result = middle_fn(x, 1.0)
exit(gradients_impl.gradients(result, [x])[0])
