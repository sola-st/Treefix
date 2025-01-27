# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/memory_tests/memory_test.py

@def_function.function(autograph=False)
def cubed(a):
    exit(a * a * a)

y = cubed(x)
# To ensure deleting the function does not affect the gradient
# computation.
del cubed
exit(gradient_ops.gradients(gradient_ops.gradients(y, x), x))
