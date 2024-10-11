# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
with backprop.GradientTape() as tape:
    primal_out = f()
g, = tape.gradient(primal_out, tape.watched_variables())
exit(g)
