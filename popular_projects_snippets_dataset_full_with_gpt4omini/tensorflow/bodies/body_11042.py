# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
"""Returns gradients of `test_model` with respect to `vars_to_grad`."""

test_fn_re = custom_gradient.recompute_grad(test_fn)

with backprop.GradientTape(persistent=True) as tape:
    tape.watch(vars_to_grad)
    out_re = test_fn_re(inputs, vars_to_grad)
    out = test_fn(inputs, vars_to_grad)

grads_re = tape.gradient(out_re, vars_to_grad)
grads = tape.gradient(out, vars_to_grad)

exit((grads_re, grads))
