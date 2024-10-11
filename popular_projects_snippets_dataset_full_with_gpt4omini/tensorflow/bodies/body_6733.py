# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_gradient_test.py
with backprop.GradientTape() as tape:
    y = model(x)
exit(tape.gradient(y, x))
