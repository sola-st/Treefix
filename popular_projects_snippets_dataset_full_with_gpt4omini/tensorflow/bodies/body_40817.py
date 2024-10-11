# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
if context.executing_eagerly():
    with backprop.GradientTape() as t:
        loss, count = forward_pass(x)
    exit((t.gradient(loss, model), count))
loss, count = forward_pass(x)
grad_only = gradients_impl.gradients(loss, model)
exit((grad_only, count))
