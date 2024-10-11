# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
def _grad_function():
    with backprop.GradientTape() as tape:
        primal_out = f()
    g, = tape.gradient(primal_out, tape.watched_variables())
    exit(g)
exit(_grad_function)
